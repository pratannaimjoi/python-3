# -*- coding: utf-8 -*-
'''
Free to use, all credits belong to me, Zero Cool.
Do not sell or rent it!
© 2018 Hello World
'''
from important import *

# Setup Argparse
parser = argparse.ArgumentParser(description='Selfbot Hello World')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()


# Login Client
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
try:
    print ('##----- LOGIN CLIENT -----##')
    line = None
    if args.apptype:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            line = LINE(idOrToken, args.passwd, appType=args.apptype, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(line.authToken)
            tokenFile.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('++ Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('++ Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath = Path('authToken.txt')
            if tokenPath.exists():
                tokenFile = tokenPath.open('r')
            else:
                tokenFile = tokenPath.open('w+')
            savedAuthToken = tokenFile.read().strip()
            authToken = savedAuthToken if savedAuthToken and not args.token else args.token
            idOrToken = authToken if authToken else args.email
            try:
                line = LINE(idOrToken, args.passwd, appType=appType, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
                tokenFile.close()
                tokenFile = tokenPath.open('w+')
                tokenFile.write(line.authToken)
                tokenFile.close()
                break
            except TalkException as talk_error:
                print ('++ Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('++ Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)
except Exception as error:
    print ('++ Error : %s' % str(error))
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

if line:
    print ('++ Auth Token : %s' % line.authToken)
    print ('++ Timeline Token : %s' % line.tl.channelAccessToken)
    print ('##----- LOGIN CLIENT (Success) -----##')
else:
    sys.exit('##----- LOGIN CLIENT (Failed) -----##')

myMid = line.profile.mid
programStart = time.time()
oepoll = OEPoll(line)
tmp_text = []
lurking = {}

settings = livejson.File('setting.json', True, False, 4)

bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}

# Backup profile
profile = line.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId

# Check Json Data
if not settings:
    print ('##----- LOAD DEFAULT JSON -----##')
    try:
        default_settings = line.server.getJson('https://17hosting.id/default.json')
        settings.update(default_settings)
        print ('##----- LOAD DEFAULT JSON (Success) -----##')
    except Exception:
        print ('##----- LOAD DEFAULT JSON (Failed) -----##')

def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))

def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text.format(key=key.title())
    return helpMsg

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def mentionMembers(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention Members 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 Hello World 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def cloneProfile(mid):
    contact = line.getContact(mid)
    profile = line.getProfile()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile(profile)
    if contact.pictureStatus:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture(pict)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    line.updateProfile(profile)
    if settings['myProfile']['pictureStatus']:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'])
        line.updateProfilePicture(pict)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'logoutbot':
        line.sendMessage(to, 'Bot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    el
                line.sendMessage (ถึง, ' setkey การเปิดใช้งานสำเร็จ' )
        elif texttl ==  'ปิด' :
            หาก ไม่มีการตั้งค่า [ ' setKey ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, 'ล้มเหลวในการยกเลิกการใช้งาน setkey, setkey ปิดใช้งานแล้ว' )
            อื่น :
                settings [ ' setKey ' ] [ ' status ' ] =  เท็จ
                line.sendMessage (ถึง, ' setkey ปิดการใช้งานสำเร็จ' )
        อื่น :
            settings [ ' setKey ' ] [ ' key ' ] = texttl
            line.sendMessage (เป็น, 'เปลี่ยนการตั้งค่าความสำเร็จเป็น ( % s ) '  % textt)
    elif cmd.startswith ( ' autoadd ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ( '  ' )
        res =  ' ╭───「เพิ่มอัตโนมัติ」'
        res + =  ' \ n ├สถานะ: '  + bool_dict [การตั้งค่า [ ' autoAdd ' ] [ 'สถานะ' ]] [ 1 ]
        res + =  ' \ n ├ตอบกลับ: '  + bool_dict [การตั้งค่า [ ' autoAdd ' ] [ 'ตอบกลับ' ]] [ 0 ]
        res + =  ' \ n ├ข้อความตอบกลับ: '  +การตั้งค่า [ ' autoAdd ' ] [ 'ข้อความ' ]
        res + =  ' \ n ├การใช้งาน: '
        ละเอียด+ =  ' \ n │• {สำคัญ} AutoAdd '
        res + =  ' \ n │• {key} เพิ่มอัตโนมัติ <เปิด / ปิด> '
        res + =  ' \ n │• {key}ตอบกลับอัตโนมัติเพิ่ม <เปิด / ปิด> '
        res + =  ' \ n │• {key} AutoAdd <message> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        ถ้า cmd ==  ' autoadd ' :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl ==  'เปิด' :
            หากการตั้งค่า [ ' autoAdd ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, ' Autoadd ทำงานอยู่แล้ว' )
            อื่น :
                settings [ ' autoAdd ' ] [ ' status ' ] =  จริง
                line.sendMessage (ถึง, 'เปิดใช้งานการเพิ่มอัตโนมัติที่สำเร็จ' )
        elif texttl ==  'ปิด' :
            หาก ไม่มีการตั้งค่า [ ' autoAdd ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, ' Autoadd ปิดใช้งานแล้ว' )
            อื่น :
                การตั้งค่า [ ' autoAdd ' ] [ 'สถานะ' ] =  เท็จ
                line.sendMessage (ถึง, 'ปิดการใช้งานอัตโนมัติที่สำเร็จแล้ว' )
        elif cond [ 0 ] .lower () ==  'คำตอบ' :
            หาก len (cond) <  2 :
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ())))
            ถ้า cond [ 1 ] .lower () ==  ' on ' :
                หากการตั้งค่า [ ' autoAdd ' ] [ 'ตอบกลับ' ]:
                    line.sendMessage (ถึง, 'ข้อความตอบกลับ autoadd เปิดใช้งานแล้ว' )
                อื่น :
                    settings [ ' autoAdd ' ] [ ' reply ' ] =  จริง
                    line.sendMessage (ถึง, 'ความสำเร็จเปิดใช้งานข้อความตอบกลับอัตโนมัติเพิ่ม' )
            elif cond [ 1 ] .lower () ==  ' off ' :
                หาก ไม่มีการตั้งค่า [ ' autoAdd ' ] [ 'ตอบกลับ' ]:
                    line.sendMessage (ถึง, 'ข้อความตอบกลับ autoadd ปิดใช้งานแล้ว' )
                อื่น :
                    settings [ ' autoAdd ' ] [ ' reply ' ] =  เท็จ
                    line.sendMessage (ถึง, 'ปิดการใช้งานข้อความตอบกลับอัตโนมัติเพิ่มความสำเร็จ' )
            อื่น :
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        อื่น :
            settings [ ' autoAdd ' ] [ ' message ' ] = textt
            line.sendMessage(to, 'Success change autoadd message to `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Join 」'
        res += '\n├ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───「 Hello World 」'
        if cmd == 'autojoin':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already active')
            else:
                settings['autoJoin']['status'] = True
                line.sendMessage(to, 'Success activated autojoin')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already deactive')
            else:
                settings['autoJoin']['status'] = False
                line.sendMessage(to, 'Success deactivated autojoin')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already active')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendMessage(to, 'Success activate reply message autojoin')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already deactive')
                else:
                    settings [ ' autoJoin ' ] [ ' reply ' ] =  เท็จ
                    line.sendMessage (ถึง, 'สำเร็จปิดการตอบข้อความอัตโนมัติเข้าร่วม' )
            อื่น :
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif cond [ 0 ] .lower () ==  ' ticket ' :
            หาก len (cond) <  2 :
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ())))
            ถ้า cond [ 1 ] .lower () ==  ' on ' :
                หากการตั้งค่า [ ' autoJoin ' ] [ 'ตั๋ว' ]:
                    line.sendMessage (ถึง'ตั๋วอัตโนมัติเข้าร่วมแล้วใช้งานอยู่' )
                อื่น :
                    การตั้งค่า [ ' autoJoin ' ] [ 'ตั๋ว' ] =  จริง
                    line.sendMessage (ถึง, 'ความสำเร็จเปิดใช้งานตั๋วอัตโนมัติเข้าร่วม' )
            elif cond [ 1 ] .lower () ==  ' off ' :
                หาก ไม่มีการตั้งค่า [ ' autoJoin ' ] [ 'ตั๋ว' ]:
                    line.sendMessage (ถึง, 'ตั๋วเข้าร่วมอัตโนมัติปิดใช้งานแล้ว' )
                อื่น :
                    การตั้งค่า [ ' autoJoin ' ] [ 'ตั๋ว' ] =  เท็จ
                    line.sendMessage (ถึง'ประสบความสำเร็จในการปิดใช้งานตั๋วอัตโนมัติเข้าร่วม' )
            อื่น :
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        อื่น :
            settings [ ' autoJoin ' ] [ ' message ' ] = textt
            line.sendMessage (ถึง'ความสำเร็จของการเปลี่ยนแปลงข้อความ autojoin จะ ` % s ` '  % textt)
    elif cmd.startswith ( ' autorespondmention ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res =  ' ╭───「ตอบกลับอัตโนมัติ」'
        res + =  ' \ n ├สถานะ: '  + bool_dict [การตั้งค่า [ ' autoRespondMention ' ] [ 'สถานะ' ]] [ 1 ]
        res + =  ' \ n ├ข้อความตอบกลับ: '  +การตั้งค่า [ ' autoRespondMention ' ] [ 'ข้อความ' ]
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key} AutoRespondMention '
        res + =  ' \ n │• {key} AutoRespondMention <เปิด / ปิด> '
        res + =  ' \ n │• {key} AutoRespondMention <message> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        หาก cmd ==  'การตอบกลับอัตโนมัติ' :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl ==  'เปิด' :
            หากการตั้งค่า [ ' autoRespondMention ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, 'การตอบกลับอัตโนมัติพร้อมทำงานแล้ว' )
            อื่น :
                settings [ ' autoRespondMention ' ] [ ' status ' ] =  จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานระบบตอบกลับอัตโนมัติที่ประสบความสำเร็จ' )
        elif texttl ==  'ปิด' :
            หาก ไม่มีการตั้งค่า [ ' autoRespondMention ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, 'การตอบกลับอัตโนมัติพร้อมใช้งานแล้ว' )
            อื่น :
                settings [ ' autoRespondMention ' ] [ ' status ' ] =  เท็จ
                line.sendMessage (ถึง, 'การปิดการตอบกลับอัตโนมัติที่ประสบความสำเร็จ' )
        อื่น :
            settings [ ' autoRespondMention ' ] [ ' message ' ] = textt
            line.sendMessage (ถึง'ความสำเร็จของการเปลี่ยนแปลงข้อความ autorespondmention จะ ` % s ` '  % textt)
    elif cmd.startswith ( ' autorespond ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res =  ' ╭───「ตอบกลับอัตโนมัติ」'
        res + =  ' \ n ├สถานะ: '  + bool_dict [การตั้งค่า [ ' autoRespond ' ] [ 'สถานะ' ]] [ 1 ]
        res + =  ' \ n ├ข้อความตอบกลับ: '  +การตั้งค่า [ ' autoRespond ' ] [ 'ข้อความ' ]
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key} การตอบกลับอัตโนมัติ'
        res + =  ' \ n │• {key} การตอบกลับอัตโนมัติ <เปิด / ปิด> '
        res + =  ' \ n │• {key} AutoRespond <message> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        ถ้า cmd ==  'ตอบกลับอัตโนมัติ' :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl ==  'เปิด' :
            หากการตั้งค่า [ ' autoRespond ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, ' Autorespond ที่ใช้งานอยู่แล้ว' )
            อื่น :
                การตั้งค่า [ ' autoRespond ' ] [ 'สถานะ' ] =  จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานระบบตอบกลับอัตโนมัติที่ประสบความสำเร็จ' )
        elif texttl ==  'ปิด' :
            หาก ไม่มีการตั้งค่า [ ' autoRespond ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, ' Autorespond deactive เรียบร้อยแล้ว' )
            อื่น :
       ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, profile.displayName)
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น :
                    line.sendMessage (ถึง, 'ชื่อที่แสดงขโมยล้มเหลว, ไม่มีผู้ใช้รายหนึ่งกล่าวถึง' )
            elifตำราl.startswith ( 'ชีวภาพ' ):
                res =  ' ╭───「ข้อความสถานะ」'
                ไม่=  0
                ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                    กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                    หาก len (กล่าวถึง [ ' MENTIONEES ' ]) ==  1 :
                        รายละเอียด= line.getContact (กล่าวถึง [ ' MENTIONEES ' ] [ 0 ] [ ' M ' ])
                        return line.sendMessage (ถึง, '「ข้อความสถานะ」\ n '  +  str (profile.statusMessage)
                    สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                        mid =พูดถึง [ ' M ' ]
                        profile = line.getContact (กลาง)
                        ไม่มี+ =  1
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ใช่, profile.statusMessage)
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น :
                    line.sendMessage (ถึง, 'ข้อความสถานะการขโมยที่ล้มเหลวไม่มีผู้ใช้รายหนึ่งพูดถึง' )
            elifตำราl.startswith ( ' pict ' ):
                res =  ' ╭───「สถานะภาพ」'
                ไม่=  0
                ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                    กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                    หาก len (กล่าวถึง [ ' MENTIONEES ' ]) ==  1 :
                        รายละเอียด= line.getContact (กล่าวถึง [ ' MENTIONEES ' ] [ 0 ] [ ' M ' ])
                        ถ้า profile.pictureStatus:
                            path =  ' http://dl.profile.line-cdn.net/ '  + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            return line.sendMessage (ถึง, '「สถานะภาพ」\ n '  +เส้นทาง)
                        อื่น :
                            กลับ line.sendMessage (ไป'ไม่ขโมยสถานะภาพผู้ใช้ ` % s ` doesn \' t มีสถานะภาพ'  % profile.displayName)
                    สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                        mid =พูดถึง [ ' M ' ]
                        profile = line.getContact (กลาง)
                        ไม่มี+ =  1
                        ถ้า profile.pictureStatus:
                            path =  ' http://dl.profile.line-cdn.net/ '  + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, เส้นทาง)
                        อื่น :
                            ละเอียด+ =  ' \ n │ %ฉัน ไม่พบ'  %ไม่
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น :
                    line.sendMessage (ถึง, 'ล้มเหลวในการขโมยสถานะภาพ, ไม่มีผู้ใช้คนใดพูดถึง' )
            elifตำราl.startswith ( 'ปก' ):
                res =  ' ╭───「รูปภาพหน้าปก」'
                ไม่=  0
                ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                    กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                    หาก len (กล่าวถึง [ ' MENTIONEES ' ]) ==  1 :
                        mid =กล่าวถึง [ ' MENTIONEES ' ] [ 0 ] [ ' M ' ]
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        line.sendMessage (ถึง, '「รูปภาพปก」\ n '  +  str (ปก))
                    สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                        mid =พูดถึง [ ' M ' ]
                        ไม่มี+ =  1
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, ปิดบัง)
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น :
                    line.sendMessage (ถึง, 'ภาพปกขโมยที่ล้มเหลว, ไม่มีผู้ใช้คนใดพูดถึง' )
            อื่น :
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        อื่น :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
    elif cmd.startswith ( 'เลียนแบบ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        เป้าหมาย=  ' '
        หากการตั้งค่า [ 'เลียนแบบ' ] [ 'เป้าหมาย' ]:
            ไม่=  0
            สำหรับเป้าหมายสถานะในการตั้งค่า [ ' mimic ' ] [ ' target ' ] .items ():
                ไม่มี+ =  1
                ลอง :
                    name = line.getContact (target) .displayName
                ยกเว้น TalkException:
                    ชื่อ=  'ไม่ทราบ'
                เป้าหมาย+ =  ' \ n │ %ฉัน % s // % s '  % (ไม่, ชื่อ, bool_dict [สถานะ] [ 1 ])
        อื่น :
            เป้าหมาย+ =  ' \ n │ไม่มีอะไรเลย'
        res =  ' ╭───「เลียนแบบ」'
        res + =  ' \ n ├สถานะ: '  + bool_dict [การตั้งค่า [ 'เลียนแบบ' ] [ 'สถานะ' ]] [ 1 ]
        res + =  ' \ n ├รายการ: '
        res + =เป้าหมาย
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key}เลียนแบบ'
        res + =  ' \ n │• {key}เลียนแบบ <เปิด / ปิด> '
        res + =  ' \ n │• {key}เลียนแบบการตั้งค่าใหม่'
        res + =  ' \ n │• {key}เลียนแบบการเพิ่ม <mention> '
        res + =  ' \ n │• {key}ล้อเลียน Del <mention> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        ถ้า cmd ==  'เลียนแบบ' :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl ==  'เปิด' :
            หากการตั้งค่า [ 'เลียนแบบ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, 'เลียนแบบใช้งานอยู่แล้ว' )
            อื่น :
                settings [ ' mimic ' ] [ ' status ' ] =  จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานสำเร็จแล้วเลียนแบบ' )
        elif texttl ==  'ปิด' :
            หาก ไม่มีการตั้งค่า [ 'เลียนแบบ' ] [ 'สถานะ' ]:
                line.sendMessage (ถึง, 'เลียนแบบเรียบร้อยแล้ว' )
            อื่น :
                settings [ ' mimic ' ] [ ' status ' ] =  False
                line.sendMessage (ถึง'ความสำเร็จปิดใช้งานการเลียนแบบ' )
        elif texttl ==  'รีเซ็ต' :
            settings [ ' mimic ' ] [ ' target ' ] = {}
            line.sendMessage (เป็น, 'การรีเซ็ตรายการเลียนแบบสำเร็จ' )
        elif texttl.startswith ( 'เพิ่ม' ):
            res =  ' ╭───「เลียนแบบ」'
            res + =  ' \ n ├สถานะ: เพิ่มเป้าหมาย'
            res + =  ' \ n ├เพิ่มแล้ว: '
            ไม่=  0
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    settings [ ' mimic ' ] [ ' target ' ] [mid] =  จริง
                    ไม่มี+ =  1
                    ลอง :
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
                res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น :
                line.sendMessage (ถึง, 'ล้มเหลวเพิ่มเป้าหมายเลียนแบบ, ไม่มีผู้ใช้หนึ่งคนพูดถึง' )
        elif texttl.startswith ( ' del ' ):
            res =  ' ╭───「เลียนแบบ」'
            res + =  ' \ n ├สถานะ: ลบเป้าหมาย'
            res + =  ' \ n ├ลบแล้ว: '
            ไม่=  0
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    หากอยู่ในช่วงกลางของการตั้งค่า [ 'เลียนแบบ' ] [ 'เป้าหมาย' ]:
                        settings [ ' mimic ' ] [ ' target ' ] [mid] =  False
                    ไม่มี+ =  1
                    ลอง :
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
                res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น :
                line.sendMessage (ถึง, 'ล้มเหลวในการลอกเลียนแบบเป้าหมาย, ไม่มีผู้ใช้คนใดพูดถึง' )
        อื่น :
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
    elif cmd.startswith ( 'ออกอากาศ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ( '  ' )
        res =  ' ╭───「 Broadcast 」'
        res + =  ' \ n ├ประเภทการออกอากาศ: '
        res + =  ' \ n │ 1: เพื่อน'
        res + =  ' \ n │ 2: กลุ่ม'
        res + =  ' \ n │ 0: ทั้งหมด'
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key} Broadcast '
        res + =  ' \ n │• {key} Broadcast <type> <message> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        หาก cmd ==  'ออกอากาศ' :
            line.sendMessage (ถึง, parsingRes (res) .format ( key = setKey.title ()))
        elif cond [ 0 ] ==  ' 1 ' :
            หาก len (cond) <  2 :
                return line.sendMessage (ถึง, 'ไม่สามารถออกอากาศ, ตรวจไม่พบข้อความ' )
            res =  '「ออกอากาศ」\ n '
            res + = textt [ 2 :]
            res + =  ' \ n \ n「สวัสดีชาวโลก」'
            เป้าหมาย= line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง :
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น Talk                      
       line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep ( 0.8 )
            line.sendMessage (ไปยัง'สำเร็จการกระจายไปยังกลุ่มทั้งหมดส่งไปยัง% iกลุ่ม'  %  len (เป้าหมาย))
        elif cond [ 0 ] ==  ' 0 ' :
            หาก len (cond) <  2 :
                return line.sendMessage (ถึง, 'ไม่สามารถออกอากาศ, ตรวจไม่พบข้อความ' )
            res =  '「ออกอากาศ」\ n '
            res + = textt [ 2 :]
            res + =  ' \ n \ n「สวัสดีชาวโลก」'
            เป้าหมาย= line.getGroupIdsJoined () + line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง :
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep ( 0.8 )
            line.sendMessage (ไปยัง'ประสบความสำเร็จในการถ่ายทอดไปยังกลุ่มและเพื่อนทั้งหมดส่งไปยัง% iกลุ่มและเพื่อน ๆ'  %  len (เป้าหมาย))
        อื่น :
            line.sendMessage (ถึง, parsingRes (res) .format ( key = setKey.title ()))
    elif cmd.startswith ( ' friendlist ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getAllContactIds ()
        cids.sort ()
        cnames = []
        ress = []
        res =  ' ╭───「รายชื่อเพื่อน」'
        res + =  ' \ n ├รายการ: '
        ถ้า cids:
            รายชื่อ= []
            ไม่=  0
            หาก len (cids) >  200 :
                parsed_len =  len (cids) // 200 + 1
                หาจุดอยู่ใน ช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด* 200 : (จุด+ 1 ) * 200 ]:
                        ลอง :
                            contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี+ =  1
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ( ' \ n ' ): res = res [ 1 :]
                        if point ! = parsed_len -  1 :
                            ress.append (ความละเอียดสูง)
                    if point ! = parsed_len -  1 :
                        res =  ' '
            อื่น :
                สำหรับ cid ใน cids:
                    ลอง :
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี+ =  1
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น :
            res + =  ' \ n │ไม่มีอะไร'
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key} FriendList '
        res + =  ' \ n │• {key}ข้อมูล FriendList <num / name> '
        res + =  ' \ n │• {key} FriendList เพิ่ม <mention> '
        res + =  ' \ n │• {key} รายชื่อเพื่อน Del <พูดถึง / num / ชื่อ / ทั้งหมด> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        ress.append (ความละเอียดสูง)
        หาก cmd ==  'รายชื่อเพื่อน' :
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl.startswith ( ' info ' ):
            ตำรา= textt [ 5 :]. แยก ( ' , ' )
            ถ้า ไม่ใช่ cids:
                return line.sendMessage (ถึง'เพื่อนที่แสดงข้อมูลล้มเหลวไม่มีเพื่อนอยู่ในรายการ' )
            สำหรับ texxt ในข้อความ:
                num =  ไม่มี
                ชื่อ=  ไม่มี
                ลอง :
                    num =  int (texxt)
                ยกเว้น ValueError :
                    ชื่อ= texxt
                if num ! =  ไม่มี :
                    contact =รายชื่อ [NUM -  1 ]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, ' http://dl.profile.line-cdn.net/ '  + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res =  ' ╭───「ข้อมูลติดต่อ」'
                    res + =  ' \ n ├ MID: '  + contact.mid
                    res + =  ' \ n ├ชื่อที่แสดง: '  +  str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + =  ' \ n ├แทนที่ชื่อที่แสดง: '  +  str (contact.displayNameOverridden)
                    res + =  ' \ n ├ข้อความสถานะ: '  +  str (contact.statusMessage)
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                ชื่อelif ! =  ไม่มี :
                    หากชื่อใน cnames:
รายชื่อ                        ผู้ติดต่อ= [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, ' http://dl.profile.line-cdn.net/ '  + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res =  ' ╭───「ข้อมูลติดต่อ」'
                        res + =  ' \ n ├ MID: '  + contact.mid
                        res + =  ' \ n ├ชื่อที่แสดง: '  +  str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + =  ' \ n ├แทนที่ชื่อที่แสดง: '  +  str (contact.displayNameOverridden)
                        res + =  ' \ n ├ข้อความสถานะ: '  +  str (contact.statusMessage)
                        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                        line.sendMessage (ถึง, parsingRes (res))
        elif texttl.startswith ( 'เพิ่ม' ):
            res =  ' ╭───「รายชื่อเพื่อน」'
            res + =  ' \ n ├สถานะ: เพิ่มเพื่อน'
            res + =  ' \ n ├เพิ่มแล้ว: '
            ไม่=  0
            เพิ่ม= []
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.findAndAddContactsByMid (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                    added.append (กลาง)
                หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
                res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น :
                line.sendMessage (ถึง, 'ล้มเหลวในการเพิ่มผู้ติดต่อไปยังรายชื่อเพื่อนไม่มีผู้ใช้หนึ่งคนที่กล่าวถึง' )
        elif texttl.startswith ( ' del ' ):
            ตำรา= textt [ 4 :]. split ( ' , ' )
            ถ้า ไม่ใช่ cids:
                return line.sendMessage (ถึง, 'ไม่สามารถลบผู้ติดต่อจากรายชื่อเพื่อนไม่มีเพื่อนในรายการ' )
            res =  ' ╭───「รายชื่อเพื่อน」'
            res + =  ' \ n ├สถานะ: เพื่อนสนิท'
            res + =  ' \ n ├ลบแล้ว: '
            ไม่=  0
            ลบแล้ว= []
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    ถ้ากลางไม่ได้ ใน CID ด้วยหรือกลางในการลบ:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.deleteContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num =  ไม่มี
                ชื่อ=  ไม่มี
                ลอง :
                    num =  int (texxt)
                ยกเว้น ValueError :
                    ชื่อ= texxt
                if num ! =  ไม่มี :
                    contact =รายชื่อ [NUM -  1 ]
                    ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.deleteContact (contact.mid)
                        name = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                    deleted.append (contact.mid)
                ชื่อelif ! =  ไม่มี :
                    หากชื่อใน cnames:
รายชื่อ                        ผู้ติดต่อ= [cnames.index (ชื่อ)]
                        ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี+ =  1
                        ลอง :
                            line.deleteContact (contact.mid)
                            name = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ=  'ไม่ทราบ'
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () ==  'ทั้งหมด' :
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี+ =  1
                            ลอง :
                                line.deleteContact (contact.mid)
                                name = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ=  'ไม่ทราบ'
                            ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep ( 0.8 )
                    อื่น :
                        line.sendMessage (ถึง, 'เพื่อนที่ล้มเหลวด้วยชื่อ ` % s`, ชื่อไม่ได้อยู่ในรายการ♪ '  %ชื่อ)
            หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
            res + =  ' \ n ╰───「สวัสดีชาวโลก」'
            line.sendMessage (ถึง, res)
        อื่น :
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
    elif cmd.startswith ( ' blocklist ' ):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getBlockedContactIds ()
        cids.sort ()
        cnames = []
        ress = []
        res =  ' ╭───「รายการบล็อก」'
        res + =  ' \ n ├รายการ: '
        ถ้า cids:
            รายชื่อ= []
            ไม่=  0
            หาก len (cids) >  200 :
                parsed_len =  len (cids) // 200 + 1
                หาจุดอยู่ใน ช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด* 200 : (จุด+ 1 ) * 200 ]:
                        ลอง :
                            contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี+ =  1
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ( ' \ n ' ): res = res [ 1 :]
                        if point ! = parsed_len -  1 :
                            ress.append (ความละเอียดสูง)
                    if point ! = parsed_len -  1 :
                        res =  ' '
            อื่น :
                สำหรับ cid ใน cids:
                    ลอง :
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี+ =  1
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น :
            res + =  ' \ n │ไม่มีอะไร'
        res + =  ' \ n ├การใช้งาน: '
        res + =  ' \ n │• {key} BlockList '
        res + =  ' \ n │• {key}ข้อมูลบล็อกลิสต์ <num / name> '
        res + =  ' \ n │• {key} BlockList เพิ่ม <mention> '
        res + =  ' \ n │• {key} BlockList Del <พูดถึง / num / name / all> '
        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd ==  ' blocklist ' :
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
        elif texttl.startswith ( ' info ' ):
            ตำรา= textt [ 5 :]. แยก ( ' , ' )
            ถ้า ไม่ใช่ cids:
                return line.sendMessage (ไปที่, 'การแสดงข้อมูลล้มเหลวผู้ใช้ที่ถูกบล็อก, ไม่มีผู้ใช้ในรายการ' )
            สำหรับ texxt ในข้อความ:
                num =  ไม่มี
                ชื่อ=  ไม่มี
                ลอง :
                    num =  int (texxt)
                ยกเว้น ValueError :
                    ชื่อ= texxt
                if num ! =  ไม่มี :
                    contact =รายชื่อ [NUM -  1 ]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, ' http://dl.profile.line-cdn.net/ '  + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res =  ' ╭───「ข้อมูลติดต่อ」'
                    res + =  ' \ n ├ MID: '  + contact.mid
                    res + =  ' \ n ├ชื่อที่แสดง: '  +  str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + =  ' \ n ├แทนที่ชื่อที่แสดง: '  +  str (contact.displayNameOverridden)
                    res + =  ' \ n ├ข้อความสถานะ: '  +  str (contact.statusMessage)
                    res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                ชื่อelif ! =  ไม่มี :
                    หากชื่อใน cnames:
รายชื่อ                        ผู้ติดต่อ= [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, ' http://dl.profile.line-cdn.net/ '  + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res =  ' ╭───「ข้อมูลติดต่อ」'
                        res + =  ' \ n ├ MID: '  + contact.mid
                        res + =  ' \ n ├ชื่อที่แสดง: '  +  str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + =  ' \ n ├แทนที่ชื่อที่แสดง: '  +  str (contact.displayNameOverridden)
                        res + =  ' \ n ├ข้อความสถานะ: '  +  str (contact.statusMessage)
                        res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                        line.sendMessage (ถึง, parsingRes (res))
        elif texttl.startswith ( 'เพิ่ม' ):
            res =  ' ╭───「รายการบล็อก」'
            res + =  ' \ n ├สถานะ: เพิ่มบล็อก'
            res + =  ' \ n ├เพิ่มแล้ว: '
            ไม่=  0
            เพิ่ม= []
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.blockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                    added.append (กลาง)
                หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
                res + =  ' \ n ╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น :
                line.sendMessage (ถึง, 'ผู้ติดต่อบล็อกไม่สำเร็จ, ไม่มีผู้ใช้รายใดพูดถึง' )
        elif texttl.startswith ( ' del ' ):
            ตำรา= textt [ 4 :]. split ( ' , ' )
            ถ้า ไม่ใช่ cids:
                return line.sendMessage (ถึง, 'ไม่สามารถปลดบล็อคผู้ติดต่อ, ไม่มีผู้ใช้ในรายการ' )
            res =  ' ╭───「รายการบล็อก」'
            res + =  ' \ n ├สถานะ: Del Block '
            res + =  ' \ n ├ลบแล้ว: '
            ไม่=  0
            ลบแล้ว= []
            ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys ():
                กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                สำหรับการกล่าวถึงในการกล่าวถึง [ ' MENTIONEES ' ]:
                    mid =พูดถึง [ ' M ' ]
                    ถ้ากลางไม่ได้ ใน CID ด้วยหรือกลางในการลบ:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.unblockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num =  ไม่มี
                ชื่อ=  ไม่มี
                ลอง :
                    num =  int (texxt)
                ยกเว้น ValueError :
                    ชื่อ= texxt
                if num ! =  ไม่มี :
                    contact =รายชื่อ [NUM -  1 ]
                    ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี+ =  1
                    ลอง :
                        line.unblockContact (contact.mid)
                        name = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ=  'ไม่ทราบ'
                    ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                             deleted.append (contact.mid)
                ชื่อelif ! =  ไม่มี :
                    หากชื่อใน cnames:
รายชื่อ                        ผู้ติดต่อ= [cnames.index (ชื่อ)]
                        ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี+ =  1
                        ลอง :
                            line.unblockContact (contact.mid)
                            name = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ=  'ไม่ทราบ'
                        ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () ==  'ทั้งหมด' :
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            ถ้า contact.mid ไม่ได้ อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี+ =  1
                            ลอง :
                                line.unblockContact (contact.mid)
                                name = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ=  'ไม่ทราบ'
                            ละเอียด+ =  ' \ n │ %ฉัน % s '  % (ไม่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep ( 0.8 )
                    อื่น :
                        line.sendMessage (ถึง, 'ล้มเหลวในการปลดบล็อกผู้ใช้ที่มีชื่อ ` % s ', ชื่อไม่ได้อยู่ในรายการ♪ '  %ชื่อ)
            หากไม่มี==  0 : res + =  ' \ n │ไม่มีอะไร'
            res + =  ' \ n ╰───「สวัสดีชาวโลก」'
            line.sendMessage (ถึง, res)
        อื่น :
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict ( key = setKey.title ()))
    elif cmd ==  ' mentionall ' :
        สมาชิก= []
        ถ้า msg.toType ==  1 :
            room = line.getCompactRoom (ถึง)
            members = [mem.mid สำหรับ mem ใน room.contacts]
        elif msg.toType ==  2 :
            group = line.getCompactGroup (ถึง)
            สมาชิก= [mem.mid สำหรับ mem ใน group.members]
        อื่น :
            return line.sendMessage (ถึง'สมาชิกที่ไม่ได้กล่าวถึงทั้งหมดใช้คำสั่งนี้เฉพาะห้องแชทหรือกลุ่ม' )
        ถ้าสมาชิก:
            พูดถึงสมาชิก (ถึงสมาชิก)
    elif cmd ==  ' groupinfo ' :
        if msg.toType != 2: return line.sendMessage(to, 'Failed display group info, use this command only on group chat')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「 Group Info 」'
        res += '\n├ ID : ' + group.id
        res += '\n├ Name : ' + group.name
        res += '\n├ Creator : ' + gcreator
        res += '\n├ Created Time : ' + created
        res += '\n├ Member Count : ' + str(len(group.members))
        res += '\n├ Pending Count : ' + str(pendings)
        res += '\n├ QR Status : ' + qr
        res += '\n├ Ticket : ' + ticket
        res += '\n╰───「 Hello World 」'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendMessage(to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───「 Group List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───「 Hello World 」'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendMessage(to, 'Failed leave group, nothing group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            line.leaveGroup(gid)
                            leaved.append(gid)
                            time.sleep(0.8)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave all group ♪')
                    else:
                        line.sendMessage(to, 'Failed leave group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───「 Invitation List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───「 Hello World 」'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendMessage(to, 'Failed accept group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    ชื่อ= texxt
                if num ! =  ไม่มี :
                    ถ้า num <=  len (กลุ่ม) และ num >  0 :
                        group =กลุ่ม [NUM -  1 ]
    

