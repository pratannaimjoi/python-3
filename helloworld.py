      # - * - การเข้ารหัส: utf-8 - * -
'''
ฟรีเครดิตทุกอย่างเป็นของฉัน Zero Cool
อย่าขายหรือให้เช่า!
© 2018 Hello World
'''
จากการนำเข้าที่สำคัญ *

# การตั้งค่าการโต้แย้ง
parser = argparse.ArgumentParser (description = 'Selfbot Hello World')
parser.add_argument ('- t', '- token', พิมพ์ = str, metavar = '', ต้องการ = False, help = 'Token | ตัวอย่าง: Exxxx')
parser.add_argument ('- e', '--email', พิมพ์ = str, default = '', metavar = '', จำเป็น = False, help = 'ที่อยู่อีเมล | ตัวอย่าง: example@xxx.xx')
parser.add_argument ('- p', '--passwd', พิมพ์ = str, default = '', metavar = '', ต้องการ = False, help = 'รหัสผ่าน | ตัวอย่าง: xxxx')
parser.add_argument ('- a', '--apptype', ชนิด = str, default = '', metavar = '', ต้องการ = False, ตัวเลือก = รายการ (ApplicationType._NAMES_TO_VALUES), ช่วย = 'ประเภทแอปพลิเคชัน | ตัวอย่าง: ChromeOS ')
parser.add_argument ('- s', '--systemname', ประเภท = str, default = '', metavar = '', ต้องการ = False, help = 'ชื่อระบบ | ตัวอย่าง: Chrome_OS')
parser.add_argument ('- c', '--channelid', พิมพ์ = str, default = '', metavar = '', จำเป็น = False, help = 'ID ช่องทาง | ตัวอย่าง: 1341209950')
parser.add_argument ('- T', '--traceback', พิมพ์ = str2bool, nargs = '?', default = False, metavar = '', จำเป็น = False, const = True, ตัวเลือก = [True, False], help = 'ใช้ Traceback | การใช้: จริง / เท็จ')
parser.add_argument ('- S', '--showqr', ชนิด = str2bool, nargs = '?', ค่าเริ่มต้น = False, metavar = '', ต้องการ = เท็จ, const = True, ตัวเลือก = [True, False], help = 'แสดง QR | การใช้: จริง / เท็จ')
args = parser.parse_args ()


# ลูกค้าเข้าสู่ระบบ
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
ลอง:
    พิมพ์ ('## ----- ลูกค้าเข้าสู่ระบบ ----- ##')
    บรรทัด = ไม่มี
    ถ้า args.apptype:
        tokenPath = เส้นทาง ('authToken.txt')
        ถ้า tokenPath.exists ():
            tokenFile = tokenPath.open ('r')
        อื่น:
            tokenFile = tokenPath.open ('w +')
        saveAuthToken = tokenFile.read (). strip ()
        authToken = saveAuthToken ถ้า saveAuthToken ไม่ใช่ args.token args.token อื่น
        idOrToken = authToken ถ้า authToken เป็นอื่น args.email
        ลอง:
            บรรทัด = LINE (idOrToken, args.passwd, appType = args.apptype, systemName = args.systemname, channelId = args.channelid, showQr = args.showqr)
            tokenFile.close ()
            tokenFile = tokenPath.open ('w +')
            tokenFile.write (line.authToken)
            tokenFile.close ()
        ยกเว้น TalkException ในฐานะ talk_error:
            ถ้า args.traceback: traceback.print_tb (talk_error .__ traceback__)
            sys.exit ('++ ข้อผิดพลาด:% s'% talk_error.reason.replace ('_', ''))
        ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
            ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
            sys.exit ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
    อื่น:
        สำหรับ appType ใน listAppType:
            tokenPath = เส้นทาง ('authToken.txt')
            ถ้า tokenPath.exists ():
                tokenFile = tokenPath.open ('r')
            อื่น:
                tokenFile = tokenPath.open ('w +')
            saveAuthToken = tokenFile.read (). strip ()
            authToken = saveAuthToken ถ้า saveAuthToken ไม่ใช่ args.token args.token อื่น
            idOrToken = authToken ถ้า authToken เป็นอื่น args.email
            ลอง:
                บรรทัด = LINE (idOrToken, args.passwd, appType = appType, systemName = args.systemname, channelId = args.channelid, showQr = args.showqr)
                tokenFile.close ()
                tokenFile = tokenPath.open ('w +')
                tokenFile.write (line.authToken)
                tokenFile.close ()
                หยุด
            ยกเว้น TalkException ในฐานะ talk_error:
                พิมพ์ ('++ ข้อผิดพลาด:% s'% talk_error.reason.replace ('_', ''))
                ถ้า args.traceback: traceback.print_tb (talk_error .__ traceback__)
                ถ้า talk_error.code == 1:
                    ต่อ
                sys.exit (1)
            ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
                พิมพ์ ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
                ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
                sys.exit (1)
ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
    พิมพ์ ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
    ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
    sys.exit (1)

ถ้าบรรทัด:
    พิมพ์ ('++ Auth Token:% s'% line.authToken)
    พิมพ์ ('++ Timeline Token:% s'% line.tl.channelAccessToken)
    พิมพ์ ('## ----- เข้าสู่ระบบลูกค้า (สำเร็จ) ----- ##')
อื่น:
    sys.exit ('## ----- ลูกค้าเข้าสู่ระบบ (ล้มเหลว) ----- ##')

myMid = line.profile.mid
programStart = time.time ()
oepoll = OEPoll (บรรทัด)
tmp_text = []
lurking = {}

settings = livejson.File ('setting.json', จริง, เท็จ, 4)

bool_dict = {
    จริง: ['ใช่', 'ใช้งานอยู่', 'สำเร็จ', 'เปิด', 'เปิด'],
    เท็จ: ['ไม่', 'ไม่ทำงาน', 'ล้มเหลว', 'ปิด', 'ปิด']
}

# โปรไฟล์สำรอง
profile = line.getContact (myMid)
settings ['myProfile'] ['displayName'] = profile.displayName
settings ['myProfile'] ['statusMessage'] = profile.statusMessage
settings ['myProfile'] ['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail ['result'] ['objectId']
settings ['myProfile'] ['coverId'] = coverId

# ตรวจสอบข้อมูล Json
หากไม่ได้ตั้งค่า:
    พิมพ์ ('## ----- โหลดเริ่มต้น JSON ----- ##')
    ลอง:
        default_settings = line.server.getJson ('https://17hosting.id/default.json')
        settings.update (default_settings)
        พิมพ์ ('## ----- โหลด DEFAULT JSON (สำเร็จ) ----- ##')
    ยกเว้นข้อยกเว้น:
        พิมพ์ ('## ----- โหลดเริ่มต้น JSON (ล้มเหลว) ----- ##')

def restartProgram ():
    พิมพ์ ('## ----- PROGRAM RESTARTED ----- ##')
    python = sys.executable
    os.execl (python, python, * sys.argv)

def logError (ข้อผิดพลาดเขียน = True):
    errid = str (random.randint (100, 999))
    filee = open ('tmp / ข้อผิดพลาด /% s.txt'% errid, 'w') ถ้าเขียนอื่นไม่มี
    ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
    ถ้าเขียน:
        traceback.print_tb (ข้อผิดพลาด. _ traceback__, ไฟล์ = filee)
        filee.close ()
        ด้วย open ('errorLog.txt', 'a') เป็น e:
            e.write ('\ n% s:% s'% (ผิดพลาด, str (ข้อผิดพลาด)))
    พิมพ์ ('++ ข้อผิดพลาด: {error}'. รูปแบบ (error = error))

คำสั่ง def (ข้อความ):
    pesan = text.lower ()
    หากการตั้งค่า ['setKey'] ['สถานะ']:
        ถ้า pesan.startswith (ตั้งค่า ['setKey'] ['คีย์']):
            cmd = pesan.replace (การตั้งค่า ['setKey'] ['คีย์'], '')
        อื่น:
            cmd = 'คำสั่งที่ไม่ได้กำหนด'
    อื่น:
        cmd = text.lower ()
    ผลตอบแทน cmd

def genImageB64 (เส้นทาง):
    ด้วย open (path, 'rb') เป็น img_file:
        encode_str = img_file.read ()
        b64img = base64.b64encode (encode_str)
        return b64img.decode ('utf-8')

def genUrlB64 (url):
    return base64.b64encode (url.encode ('utf-8')). decode ('utf-8')

def removeCmd (text, key = ''):
    ถ้าคีย์ == '':
        setKey = '' หากไม่ได้ตั้งค่า ['setKey'] ['สถานะ'] การตั้งค่าอื่น ['setKey'] ['คีย์']
    อื่น:
        setKey = สำคัญ
    text_ = text [len (setKey):]
    sep = text_.split ('')
    ส่งคืนข้อความ _ [len (sep [0] + ''):]

def multiCommand (cmd, list_cmd = []):
    ถ้าเป็น True ใน [cmd.startswith (c) สำหรับ c ใน list_cmd]:
        กลับ True
    อื่น:
        กลับเท็จ

def replaceAll (ข้อความ, dic):
    ลอง:
        rep_this = dic.items ()
    ยกเว้น:
        rep_this = dic.iteritems ()
    สำหรับฉัน, j ใน rep_this:
        text = text.replace (i, j)
    ส่งคืนข้อความ

def help ():
    key = '' หากไม่ได้ตั้งค่า ['setKey'] ['สถานะ'] การตั้งค่าอื่น ['setKey'] ['คีย์']
    ด้วย open ('help.txt', 'r') เป็น f:
        text = f.read ()
    helpMsg = text.format (key = key.title ())
    กลับมาช่วยเหลือ MS

def parsingRes (res):
    ผลลัพธ์ = ''
    textt = res.split ('\ n')
    สำหรับข้อความใน textt:
        หาก True ไม่อยู่ใน [text.startswith (s) สำหรับ s ใน ['╭', '├', '│', '╰']]:
            result + = '\ n│' + ข้อความ
        อื่น:
            หากข้อความ == textt [0]:
                ผลลัพธ์ + = ข้อความ
            อื่น:
                ผลลัพธ์ + = '\ n' + ข้อความ
    ส่งคืนผลลัพธ์

def กล่าวถึงสมาชิก (ถึง, mids = []):
    ถ้า myMid เป็น mids: mids.remove (myMid)
    parsed_len = len (กลาง) // 20 + 1
    result = '╭───「พูดถึงสมาชิก」 \ n'
    พูดถึง = '@zeroxyuuki \ n'
    ไม่ = 0
    หาจุดอยู่ในช่วง (parsed_len):
        ผู้กล่าวถึง = []
        สำหรับ mid in mids [จุด * 20: (จุด + 1) * 20]:
            ไม่มี + = 1
            ผลลัพธ์ + = '│% i % s '% (ไม่พูดถึง)
            slen = len (ผลลัพธ์) - 12
            elen = len (ผลลัพธ์) + 3
            พูดถึง. ผนวก ({'S': str (slen), 'E': str (elen - 4), 'M': mid})
            ถ้า mid == mids [-1]:
                ผลลัพธ์ + = '╰───「 Hello World 」 \ n'
        ถ้าผลลัพธ์:
            ถ้า result.endswith ('\ n'): result = result [: - 1]
            line.sendMessage (ถึง, ผลลัพธ์, {'MENTION': json.dumps ({'MENTIONEES': กล่าวถึง}}), 0)
        ผลลัพธ์ = ''

def cloneProfile (กลาง):
    contact = line.getContact (กลาง)
    profile = line.getProfile ()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile (รายละเอียด)
    หากผู้ติดต่อรูปภาพสถานะ:
        pict = line.downloadFileURL ('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture (PICT)
    coverId = line.getProfileDetail (กลาง) ['ผลลัพธ์'] ['objectId']
    line.updateProfileCoverById (coverId)

def backupProfile ():
    profile = line.getContact (myMid)
    settings ['myProfile'] ['displayName'] = profile.displayName
    settings ['myProfile'] ['pictureStatus'] = profile.pictureStatus
    settings ['myProfile'] ['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail () ['ผลลัพธ์'] ['objectId']
    settings ['myProfile'] ['coverId'] = str (coverId)

def restoreProfile ():
    profile = line.getProfile ()
    profile.displayName = settings ['myProfile'] ['displayName']
    profile.statusMessage = settings ['myProfile'] ['statusMessage']
    line.updateProfile (รายละเอียด)
    หากการตั้งค่า ['myProfile'] ['pictureStatus']:
        pict = line.downloadFileURL ('http://dl.profile.line-cdn.net/' + การตั้งค่า ['myProfile'] ['pictureStatus'])
        line.updateProfilePicture (PICT)
    coverId = settings ['myProfile'] ['coverId']
    line.updateProfileCoverById (coverId)

def executeCmd (msg, ข้อความ, txt, cmd, msg_id, ผู้รับ, ผู้ส่ง, ถึง, setKey):
    หาก cmd == 'logoutbot':
        line.sendMessage (ถึง, 'Bot จะออกจากระบบ')
        sys.exit ('## ----- โปรแกรมหยุด ----- ##')
    elif cmd == 'logoutdevicee':
        line.logout ()
        sys.exit ('## ----- ลูกค้า LOGOUT ----- ##')
    elif cmd == 'เริ่มต้นใหม่':
        line.sendMessage (ถึง, 'Bot จะรีสตาร์ทโปรดรอจนกว่า bot จะทำงานได้ operate')
        settings ['restartPoint'] = ถึง
        restartProgram ()
    elif cmd == 'ความช่วยเหลือ':
        line.sendReplyMessage (msg_id, ถึง, help ())
    elif cmd == 'speed':
        start = time.time ()
        line.sendMessage (ถึง, 'การตรวจสอบความเร็ว')
        elapse = time.time () - เริ่ม
        line.sendMessage (ถึง, 'การส่งข้อความความเร็วใช้เวลา% s วินาที'% str (ผ่านไป))
    elif cmd == 'me':
        line.sendContact (ถึง, myMid)
    elif cmd == 'runtime':
        runtime = time.time () - programStart
        line.sendMessage (ถึง, 'Bot ทำงานแล้วใน' + format_timespan (runtime))
    elif cmd == 'ผู้แต่ง':
        line.sendMessage (ถึง 'ผู้เขียนคือ linepy')
    elif cmd == 'about':
        res = '╭───「เกี่ยวกับ」'
        res + = '\ n├ประเภท: Selfbot Hello World'
        res + = '\ n├เวอร์ชัน: 3.0.8'
        res + = '\ n├ Library: linepy (Python)'
        res + = '\ n├ผู้สร้าง: Zero Cool'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        line.sendMessage (ถึง, res)
    elif cmd == 'สถานะ':
        res = '╭───「สถานะ」'
        res + = '\ n├เพิ่มอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoAdd'] ['สถานะ']] [1]
        res + = '\ n├การเข้าร่วมอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoJoin'] ['สถานะ']] [1]
        res + = '\ n├การตอบกลับอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRespond'] ['สถานะ']] [1]
        res + = '\ n├พูดถึงการตอบกลับอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRespondMention'] ['สถานะ']] [1]
        res + = '\ n├อ่านอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRead']] [1]
        res + = '\ n├คีย์การตั้งค่า:' + bool_dict [การตั้งค่า ['setKey'] ['สถานะ']] [1]
        res + = '\ n├เลียนแบบ:' + bool_dict [การตั้งค่า ['เลียนแบบ'] ['สถานะ']] [1]
        res + = '\ n├ทักทายเข้าร่วม:' + bool_dict [การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']] [1]
        res + = '\ n├ลาการทักทาย:' + bool_dict [การตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']] [1]
        res + = '\ n├ตรวจสอบรายชื่อผู้ติดต่อ:' + bool_dict [การตั้งค่า ['checkContact']] [1]
        res + = '\ n├ตรวจสอบโพสต์:' + bool_dict [การตั้งค่า ['checkPost']] [1]
        res + = '\ n├ตรวจสอบสติ๊กเกอร์:' + bool_dict [การตั้งค่า ['checkSticker']] [1]
        res + = '\ n╰───「สวัสดีชาวโลก」'
        line.sendMessage (ถึง, parsingRes (res))
    elif cmd == 'ยกเลิก':
        aborted = เท็จ
        ถ้าจะอยู่ในการตั้งค่า ['changeGroupPicture']:
            การตั้งค่า [ 'changeGroupPicture']. ลบ (เพื่อ)
            line.sendMessage (เป็น, 'เปลี่ยนรูปภาพกลุ่มถูกยกเลิก')
            aborted = True
        หากการตั้งค่า ['changePictureProfile']:
            settings ['changePictureProfile'] = เท็จ
            line.sendMessage (เป็น, 'เปลี่ยนโปรไฟล์ภาพที่ถูกยกเลิก')
            aborted = True
        หากการตั้งค่า ['changeCoverProfile']:
            settings ['changeCoverProfile'] = เท็จ
            line.sendMessage (เป็น, 'เปลี่ยนหน้าปกที่ยกเลิกโปรไฟล์')
            aborted = True
        หากไม่ถูกยกเลิก:
            line.sendMessage (ไปที่ 'ล้มเหลวล้มเหลวไม่มีอะไรจะยกเลิก')
    elif cmd.startswith ('ข้อผิดพลาด'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「ข้อผิดพลาด」'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│•ข้อผิดพลาด {key}'
        res + = '\ n│• {key} บันทึกข้อผิดพลาด'
        res + = '\ n│• {key} การรีเซ็ตข้อผิดพลาด'
        res + = '\ n│• {key} รายละเอียดข้อผิดพลาด <errid>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        หาก cmd == 'ข้อผิดพลาด':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif cond [0] .lower () == 'บันทึก':
            ลอง:
                filee = open ('errorLog.txt', 'r')
            ยกเว้น FileNotFoundError:
                return line.sendMessage (ไปที่ 'ล้มเหลวในการแสดงข้อผิดพลาดบันทึกไฟล์ข้อผิดพลาดไม่พบ')
            ข้อผิดพลาด = [err.strip () สำหรับข้อผิดพลาดใน filee.readlines ()]
            filee.close ()
            หากไม่ใช่ข้อผิดพลาด: ส่งคืน line.sendMessage (ไปที่ 'ล้มเหลวในการแสดงข้อผิดพลาดบันทึกข้อผิดพลาดที่ว่างเปล่าบันทึก')
            res = '╭───「บันทึกข้อผิดพลาด」'
            res + = '\ n├รายการ:'
            parsed_len = len (ข้อผิดพลาด) // 200 + 1
            ไม่ = 0
            หาจุดอยู่ในช่วง (parsed_len):
                สำหรับข้อผิดพลาดในข้อผิดพลาด [จุด * 200: (จุด + 1) * 200]:
                    ถ้าไม่ใช่ข้อผิดพลาด: ดำเนินการต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่ผิดพลาด)
                    หากข้อผิดพลาด == ข้อผิดพลาด [-1]:
                        res + = '\ n╰───「สวัสดีชาวโลก」'
                ถ้า res:
                    ถ้า res.startswith ('\ n'): res = res [1:]
                    line.sendMessage (ถึง, res)
                res = ''
        elif cond [0] .lower () == 'รีเซ็ต':
            filee = open ('errorLog.txt', 'w')
            filee.write ( '')
            filee.close ()
            shutil.rmtree ('tmp / errors /', ign_errors = True)
            os.system ('mkdir tmp / ข้อผิดพลาด')
            line.sendMessage (เป็น 'บันทึกข้อผิดพลาดในการรีเซ็ตสำเร็จ')
        elif cond [0] .lower () == 'detail':
            หาก len (cond) <2:
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ())))
            errid = cond [1]
            หาก os.path.exists ('tmp / errors /% s.txt'% errid):
                ด้วย open ('tmp / errors /% s.txt'% errid, 'r') เป็น f:
                    line.sendMessage (ถึง, f.read ())
            อื่น:
                return line.sendMessage (ถึง, 'ข้อผิดพลาดของรายละเอียดการแสดงผล, ข้อผิดพลาดไม่ถูกต้อง')
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif txt.startswith ('setkey'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「การตั้งค่าคีย์」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['setKey'] ['สถานะ']] [1]
        res + = '\ n├ Key:' + settings ['setKey'] ['key']. title ()
        res + = '\ n├การใช้งาน:'
        res + = '\ n│•ปุ่มกด'
        res + = '\ n│• Setkey <on / off>'
        res + = '\ n│• Setkey <key>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า txt == 'setkey':
            line.sendMessage (ถึง, parsingRes (res))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['setKey'] ['สถานะ']:
                line.sendMessage (ถึง, 'ล้มเหลวในการเปิดใช้งาน setkey, setkey ทำงานอยู่แล้ว')
            อื่น:
                settings ['setKey'] ['status'] = จริง
                line.sendMessage (ถึง, 'setkey การเปิดใช้งานสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['setKey'] ['สถานะ']:
                line.sendMessage (ถึง, 'ล้มเหลวในการยกเลิกการใช้งาน setkey, setkey ปิดใช้งานแล้ว')
            อื่น:
                settings ['setKey'] ['status'] = เท็จ
                line.sendMessage (ถึง, 'setkey ปิดการใช้งานสำเร็จ')
        อื่น:
            settings ['setKey'] ['key'] = texttl
            line.sendMessage (เป็น, 'เปลี่ยนการตั้งค่าความสำเร็จเป็น (% s)'% textt)
    elif cmd.startswith ('autoadd'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「เพิ่มอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoAdd'] ['สถานะ']] [1]
        res + = '\ n├ตอบกลับ:' + bool_dict [การตั้งค่า ['autoAdd'] ['ตอบกลับ']] [0]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoAdd'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} เพิ่มอัตโนมัติ'
        res + = '\ n│• {key} เพิ่มอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} ตอบกลับอัตโนมัติเพิ่ม <เปิด / ปิด>'
        res + = '\ n│• {key} AutoAdd <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'autoadd':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoAdd'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autoadd ทำงานอยู่แล้ว')
            อื่น:
                settings ['autoAdd'] ['status'] = จริง
                line.sendMessage (ถึง, 'เปิดใช้งานการเพิ่มอัตโนมัติที่สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoAdd'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autoadd ปิดใช้งานแล้ว')
            อื่น:
                การตั้งค่า ['autoAdd'] ['สถานะ'] = เท็จ
                line.sendMessage (ถึง, 'ปิดการใช้งานอัตโนมัติที่สำเร็จแล้ว')
        elif cond [0] .lower () == 'คำตอบ':
            หาก len (cond) <2:
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ())))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoAdd'] ['ตอบกลับ']:
                    line.sendMessage (ถึง, 'ข้อความตอบกลับ autoadd เปิดใช้งานแล้ว')
                อื่น:
                    settings ['autoAdd'] ['reply'] = จริง
                    line.sendMessage (ถึง, 'ความสำเร็จเปิดใช้งานข้อความตอบกลับอัตโนมัติเพิ่ม')
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoAdd'] ['ตอบกลับ']:
                    line.sendMessage (ถึง, 'ข้อความตอบกลับ autoadd ปิดใช้งานแล้ว')
                อื่น:
                    settings ['autoAdd'] ['reply'] = เท็จ
                    line.sendMessage (ถึง, 'ปิดการใช้งานข้อความตอบกลับอัตโนมัติเพิ่มความสำเร็จ')
            อื่น:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            settings ['autoAdd'] ['message'] = textt
            line.sendMessage (เป็น, 'เปลี่ยนข้อความอัตโนมัติให้เป็น `% s`'% textt ได้สำเร็จ)
    elif cmd.startswith ('autojoin'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「เข้าร่วมอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoJoin'] ['สถานะ']] [1]
        res + = '\ n├ตอบกลับ:' + bool_dict [การตั้งค่า ['autoJoin'] ['ตอบกลับ']] [0]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoJoin'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} AutoJoin'
        res + = '\ n│• {key} AutoJoin <เปิด / ปิด>'
        res + = '\ n│• {key} ตั๋วเข้าร่วมอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} ตอบกลับเข้าร่วมอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} AutoJoin <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'autojoin':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoJoin'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autojoin ทำงานอยู่แล้ว')
            อื่น:
                การตั้งค่า ['autoJoin'] ['สถานะ'] = จริง
                line.sendMessage (ถึง, 'เปิดใช้งาน autojoin สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoJoin'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autojoin ถูกปิดใช้งานแล้ว')
            อื่น:
                การตั้งค่า ['autoJoin'] ['สถานะ'] = เท็จ
                line.sendMessage (ไปยัง 'ปิดการใช้งานความสำเร็จอัตโนมัติ')
        elif cond [0] .lower () == 'คำตอบ':
            หาก len (cond) <2:
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ())))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                    line.sendMessage (ถึง, 'ตอบกลับข้อความอัตโนมัติเข้าร่วมอยู่แล้ว')
                อื่น:
                    settings ['autoJoin'] ['reply'] = จริง
                    line.sendMessage (ถึง, 'สำเร็จเปิดใช้งานข้อความตอบกลับอัตโนมัติเข้าร่วม')
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                    line.sendMessage (ถึง, 'ตอบข้อความอัตโนมัติเข้าร่วมแล้วปิดการใช้งาน')
                อื่น:
                    settings ['autoJoin'] ['reply'] = เท็จ
                    line.sendMessage (ถึง, 'สำเร็จปิดการตอบข้อความอัตโนมัติเข้าร่วม')
            อื่น:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif cond [0] .lower () == 'ticket':
            หาก len (cond) <2:
                ส่งคืน line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ())))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    line.sendMessage (ถึง 'ตั๋วอัตโนมัติเข้าร่วมแล้วใช้งานอยู่')
                อื่น:
                    การตั้งค่า ['autoJoin'] ['ตั๋ว'] = จริง
                    line.sendMessage (ถึง, 'ความสำเร็จเปิดใช้งานตั๋วอัตโนมัติเข้าร่วม')
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    line.sendMessage (ถึง, 'ตั๋วเข้าร่วมอัตโนมัติปิดใช้งานแล้ว')
                อื่น:
                    การตั้งค่า ['autoJoin'] ['ตั๋ว'] = เท็จ
                    line.sendMessage (ถึง 'ประสบความสำเร็จในการปิดใช้งานตั๋วอัตโนมัติเข้าร่วม')
            อื่น:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            settings ['autoJoin'] ['message'] = textt
            line.sendMessage (เป็น 'เปลี่ยนข้อความอัตโนมัติให้เป็น'% s` '% textt ได้สำเร็จ)
    elif cmd.startswith ('autorespondmention'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「ตอบกลับอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoRespondMention'] ['สถานะ']] [1]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoRespondMention'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} AutoRespondMention'
        res + = '\ n│• {key} AutoRespondMention <เปิด / ปิด>'
        res + = '\ n│• {key} AutoRespondMention <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        หาก cmd == 'การตอบกลับอัตโนมัติ':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoRespondMention'] ['สถานะ']:
                line.sendMessage (ถึง, 'การตอบกลับอัตโนมัติพร้อมทำงานแล้ว')
            อื่น:
                settings ['autoRespondMention'] ['status'] = จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานระบบตอบกลับอัตโนมัติที่สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRespondMention'] ['สถานะ']:
                line.sendMessage (ถึง, 'การตอบกลับอัตโนมัติพร้อมใช้งานแล้ว')
            อื่น:
                settings ['autoRespondMention'] ['status'] = เท็จ
                line.sendMessage (ถึง, 'การปิดการตอบกลับอัตโนมัติที่ประสบความสำเร็จ')
        อื่น:
            settings ['autoRespondMention'] ['message'] = textt
            line.sendMessage (เป็น, 'เปลี่ยนข้อความตอบกลับอัตโนมัติเป็น'% s ''% textt ได้สำเร็จ)
    elif cmd.startswith ('autorespond'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「ตอบกลับอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoRespond'] ['สถานะ']] [1]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoRespond'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} การตอบกลับอัตโนมัติ'
        res + = '\ n│• {key} การตอบกลับอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} AutoRespond <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'ตอบกลับอัตโนมัติ':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoRespond'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autorespond ที่ใช้งานอยู่แล้ว')
            อื่น:
                การตั้งค่า ['autoRespond'] ['สถานะ'] = จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานระบบตอบกลับอัตโนมัติที่สำเร็จ'
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRespond'] ['สถานะ']:
                line.sendMessage (ถึง, 'Autorespond deactive เรียบร้อยแล้ว')
            อื่น:
                การตั้งค่า ['autoRespond'] ['สถานะ'] = เท็จ
                line.sendMessage (ถึง, 'การปิดการตอบกลับอัตโนมัติที่ประสบความสำเร็จ')
        อื่น:
            การตั้งค่า ['autoRespond'] ['ข้อความ'] = ข้อความ
            line.sendMessage (เป็น, 'เปลี่ยนข้อความตอบกลับอัตโนมัติเป็น `% s`'% textt ได้สำเร็จ)
    elif cmd.startswith ('autoread'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['autoRead']:
                line.sendMessage (ถึง, 'Autoread ทำงานอยู่แล้ว')
            อื่น:
                settings ['autoRead'] = จริง
                line.sendMessage (ถึง, 'การเปิดใช้งาน autoread สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRead']:
                line.sendMessage (ถึง, 'Autoread ปิดใช้งานอยู่แล้ว')
            อื่น:
                settings ['autoRead'] = เท็จ
                line.sendMessage (ไปที่ 'ปิดการใช้งาน Autoread สำเร็จ')
    elif cmd.startswith ('checkcontact'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkContact']:
                line.sendMessage (ถึง, 'Checkcontact เปิดใช้งานแล้ว')
            อื่น:
                settings ['checkContact'] = จริง
                line.sendMessage (ไปยัง 'สำเร็จเปิดใช้งาน checkcontact')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['checkContact']:
                line.sendMessage (ถึง, 'Checkcontact ปิดใช้งานแล้ว')
            อื่น:
                settings ['checkContact'] = เท็จ
                line.sendMessage (ถึง, 'ความสำเร็จในการปิดการใช้งาน checkcontact')
    elif cmd.startswith ('checkpost'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkPost']:
                line.sendMessage (ถึง, 'Checkpost ทำงานอยู่แล้ว')
            อื่น:
                settings ['checkPost'] = จริง
                line.sendMessage (ถึง 'เปิดใช้งานสำเร็จแล้ว')
        elif texttl == 'ปิด':
            หากไม่ได้ตั้งค่า ['checkPost']:
                line.sendMessage (ถึง, 'Checkpost ปิดการใช้งานแล้ว')
            อื่น:
                settings ['checkPost'] = เท็จ
                line.sendMessage (ไปยัง 'เครื่องหมายถูกที่ปิดใช้งานสำเร็จ')
    elif cmd.startswith ('checksticker'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkSticker']:
                line.sendMessage (ถึง, 'Checksticker เปิดใช้งานแล้ว')
            อื่น:
                settings ['checkSticker'] = จริง
                line.sendMessage (ถึง, 'ตัวตรวจสอบการเปิดใช้งานสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['checkSticker']:
                line.sendMessage (ถึง, 'Checksticker ปิดใช้งานแล้ว')
            อื่น:
                settings ['checkSticker'] = เท็จ
                line.sendMessage (ถึง, 'ตัวตรวจสอบความสำเร็จปิดการใช้งาน')
    elif cmd.startswith ('myprofile'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        profile = line.getProfile ()
        res = '╭───「โปรไฟล์ของฉัน」'
        res + = '\ n├ MID:' + profile.mid
        res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
        res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} MyProfile'
        res + = '\ n│• {key} MyProfile MID'
        res + = '\ n│• {key} ชื่อ MyProfile'
        res + = '\ n│• {key} MyProfile Bio'
        res + = '\ n│• {key} MyProfile Pict'
        res + = '\ n│• {key} MyProfile Cover'
        res + = '\ n│• {key} MyProfile เปลี่ยนชื่อ <name>'
        res + = '\ n│• {key} MyProfile Change Bio <bio>'
        res + = '\ n│• {key} MyProfile Change Pict'
        res + = '\ n│• {key} MyProfile Change Cover'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'myprofile':
            ถ้า profile.pictureStatus:
                line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'mid':
            line.sendMessage (ถึง, '「 MID 」 \ n' + str (profile.mid))
        elif texttl == 'name':
            line.sendMessage (ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
        elif texttl == 'ชีวภาพ':
            line.sendMessage (ถึง, '「ข้อความสถานะ」 \ n' + str (profile.statusMessage)
        elif texttl == 'pict':
            ถ้า profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL (ไปยังเส้นทาง)
                line.sendMessage (ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
            อื่น:
                line.sendMessage (ถึง, 'สถานะภาพที่แสดงล้มเหลวผู้ใช้ไม่มีสถานะภาพ')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendMessage (ถึง, '「รูปภาพปก」 \ n' + str (ปก))
        elif texttl.startswith ('เปลี่ยน'):
            ตำรา = textt [7:]
            ตำราl = ตำรา.lower ()
            หากตำรา l.startswith ('ชื่อ'):
                ชื่อ = ข้อความ [5:]
                ถ้า len (ชื่อ) <= 20:
                    profile.displayName = ชื่อ
                    line.updateProfile (รายละเอียด)
                    line.sendMessage (เป็น, 'เปลี่ยนชื่อสำเร็จแล้วเปลี่ยนเป็นชื่อ'% s` '%%)
                อื่น:
                    line.sendMessage (เป็น, 'ชื่อที่แสดงเปลี่ยนไม่ได้ความยาวของชื่อต้องไม่เกิน 20')
            elif ตำราl.startswith ('ชีวภาพ'):
                bio = ตำรา [4:]
                หาก len (ประวัติ) <= 500:
                    profile.statusMessage = ชีวภาพ
                    line.updateProfile (รายละเอียด)
                    line.sendMessage (เป็น 'ข้อความแจ้งเตือนการเปลี่ยนสถานะสำเร็จเปลี่ยนเป็น `% s`'% bio)
                อื่น:
                    line.sendMessage (ถึง, 'ข้อความสถานะการเปลี่ยนแปลงล้มเหลวความยาวของไบโอต้องไม่เกิน 500')
            elif ตำราl == 'pict':
                settings ['changePictureProfile'] = จริง
                line.sendMessage (ไปที่ 'กรุณาส่งภาพเพื่อตั้งค่าในโปรไฟล์ภาพพิมพ์' {key} ยกเลิก 'หากต้องการยกเลิก \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัปโหลด image'.format (key = setKey นานเกินไป) หัวข้อ()))
            elif ตำราl == 'ปก':
                settings ['changeCoverProfile'] = จริง
                line.sendMessage (ไปที่ 'กรุณาส่งภาพเพื่อตั้งค่าในโปรไฟล์ปกพิมพ์' {key} ยกเลิก 'หากต้องการยกเลิก \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพ'.format (key = setKey นานเกินไป) หัวข้อ()))
            อื่น:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('profile'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        profile = line.getContact (ถึง) ถ้า msg.toType == 0 ไม่มี
        res = '╭───「โปรไฟล์ของฉัน」'
        หากโปรไฟล์:
            res + = '\ n├ MID:' + profile.mid
            res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
            ถ้า profile.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (profile.displayNameOverridden)
            res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} โปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์กลาง'
        res + = '\ n│• {key} ชื่อโปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์ Bio'
        res + = '\ n│• {key} Pict ของโปรไฟล์'
        res + = '\ n│• {key} หน้าปกโปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์การขโมยโปรไฟล์ <mention>'
        res + = '\ n│• {key} โปรไฟล์ขโมย Mid <mention>'
        res + = '\ n│• {key} ชื่อขโมยโปรไฟล์ <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Bio <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Pict <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Cover <mention>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        หาก cmd == 'โปรไฟล์':
      หากโปรไฟล์:
                ถ้า profile.pictureStatus:
                    line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL (profile.mid)
                line.sendImageWithURL (ถึง, str (ปก))
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'mid':
            ถ้า msg.toType! = 0: return line.sendMessage (ไปที่ 'ผู้ใช้ที่แสดงกลางไม่สำเร็จใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendMessage (ถึง, '「 MID 」 \ n' + str (profile.mid))
        elif texttl == 'name':
            ถ้า msg.toType! = 0: return line.sendMessage (ไปที่ 'ผู้ใช้ที่แสดงกลางไม่สำเร็จใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendMessage (ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
        elif texttl == 'ชีวภาพ':
            ถ้า msg.toType! = 0: return line.sendMessage (ไปที่ 'ผู้ใช้ที่แสดงกลางไม่สำเร็จใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendMessage (ถึง, '「ข้อความสถานะ」 \ n' + str (profile.statusMessage)
        elif texttl == 'pict':
            ถ้า msg.toType! = 0: return line.sendMessage (ไปที่ 'ผู้ใช้ที่แสดงกลางไม่สำเร็จใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            ถ้า profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL (ไปยังเส้นทาง)
                line.sendMessage (ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
            อื่น:
                line.sendMessage (ถึง, 'สถานะภาพที่แสดงล้มเหลวผู้ใช้ไม่มีสถานะภาพ')
        elif texttl == 'cover':
            ถ้า msg.toType! = 0: return line.sendMessage (ไปที่ 'ผู้ใช้ที่แสดงกลางไม่สำเร็จใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendMessage (ถึง, '「รูปภาพปก」 \ n' + str (ปก))
        elif texttl.startswith ('steal'):
            ตำรา = textt [6:]
            ตำราl = ตำรา.lower ()
            หากตำรา l.startswith ('โปรไฟล์'):
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        profile = line.getContact (พูดถึง ['M'])
                        ถ้า profile.pictureStatus:
                            line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL (profile.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「โปรไฟล์」'
                        res + = '\ n├ MID:' + profile.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
                        ถ้า profile.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (profile.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
                        res + = '\ n╰───「สวัสดีชาวโลก」'
                        line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ไม่สามารถขโมยโปรไฟล์, ไม่มีผู้ใช้รายใดพูดถึง')
            elif ตำราl.startswith ('กลาง'):
                res = '╭───「 MID 」'
                ไม่ = 0
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        mid = กล่าวถึง ['MENTIONEES'] [0] ['M']
                        return line.sendMessage (ถึง, '「 MID 」 \ n' + กลาง)
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, กลาง)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ไม่สามารถขโมยกลางไม่มีผู้ใช้คนใดพูดถึง')
            elif ตำราl.startswith ('ชื่อ'):
                res = '╭───「ชื่อที่แสดง」'
                ไม่ = 0
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        return line.sendMessage (ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, profile.displayName)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ชื่อที่แสดงขโมยล้มเหลว, ไม่มีผู้ใช้รายหนึ่งกล่าวถึง')
            elif ตำราl.startswith ('ชีวภาพ'):
                res = '╭───「ข้อความสถานะ」'
                ไม่ = 0
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        return line.sendMessage (ถึง, '「ข้อความสถานะ」 \ n' + str (profile.statusMessage)
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่ใช่, profile.statusMessage)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ข้อความสถานะการขโมยที่ล้มเหลวไม่มีผู้ใช้รายหนึ่งพูดถึง')
            elif ตำราl.startswith ('pict'):
                res = '╭───「สถานะภาพ」'
                ไม่ = 0
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        ถ้า profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            return line.sendMessage (ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
                        อื่น:
                            return line.sendMessage (ไปที่ 'ไม่สามารถขโมยสถานะภาพผู้ใช้ `% s` ไม่ได้มีสถานะภาพ'% profile.displayName)
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        ถ้า profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            res + = '\ n│% i % s '% (ไม่, เส้นทาง)
                        อื่น:
                            res + = '\ n│% i ไม่พบ '% ไม่
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ล้มเหลวในการขโมยสถานะภาพ, ไม่มีผู้ใช้คนใดพูดถึง')
            elif ตำราl.startswith ('ปก'):
                res = '╭───「รูปภาพหน้าปก」'
                ไม่ = 0
                ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        mid = กล่าวถึง ['MENTIONEES'] [0] ['M']
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        line.sendMessage (ถึง, '「รูปภาพปก」 \ n' + str (ปก))
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        ไม่มี + = 1
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res + = '\ n│% i % s '% (ไม่, ปิดบัง)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                อื่น:
                    line.sendMessage (ถึง, 'ภาพปกขโมยที่ล้มเหลว, ไม่มีผู้ใช้คนใดพูดถึง')
            อื่น:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('เลียนแบบ'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        เป้าหมาย = ''
        หากการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย']:
            ไม่ = 0
            สำหรับเป้าหมายสถานะในการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย'] รายการ ():
                ไม่มี + = 1
                ลอง:
                    name = line.getContact (target) .displayName
                ยกเว้น TalkException:
                    ชื่อ = 'ไม่ทราบ'
                เป้าหมาย + = '\ n│% i % s //% s '% (ไม่, ชื่อ, bool_dict [สถานะ] [1])
        อื่น:
            เป้าหมาย + = '\ n│ไม่มีอะไรเลย'
        res = '╭───「เลียนแบบ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['เลียนแบบ'] ['สถานะ']] [1]
        res + = '\ n├รายการ:'
        res + = เป้าหมาย
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} เลียนแบบ'
        res + = '\ n│• {key} เลียนแบบ <เปิด / ปิด>'
        res + = '\ n│• {key} เลียนแบบการตั้งค่าใหม่'
        res + = '\ n│• {key} เลียนแบบการเพิ่ม <mention>'
        res + = '\ n│• {key} ล้อเลียน Del <mention>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'เลียนแบบ':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['เลียนแบบ'] ['สถานะ']:
                line.sendMessage (ถึง, 'เลียนแบบใช้งานอยู่แล้ว')
            อื่น:
                settings ['mimic'] ['status'] = จริง
                line.sendMessage (ถึง, 'การเปิดใช้งานสำเร็จแล้วเลียนแบบ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['เลียนแบบ'] ['สถานะ']:
                line.sendMessage (ถึง, 'เลียนแบบเรียบร้อยแล้ว')
            อื่น:
                settings ['mimic'] ['status'] = False
                line.sendMessage (ถึง 'ความสำเร็จปิดใช้งานการเลียนแบบ')
        elif texttl == 'รีเซ็ต':
            settings ['mimic'] ['target'] = {}
            line.sendMessage (เป็น, 'การรีเซ็ตรายการเลียนแบบสำเร็จ')
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「เลียนแบบ」'
            res + = '\ n├สถานะ: เพิ่มเป้าหมาย'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    settings ['mimic'] ['target'] [mid] = จริง
                    ไม่มี + = 1
                    ลอง:
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น:
                line.sendMessage (ถึง, 'ล้มเหลวเพิ่มเป้าหมายเลียนแบบ, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
        elif texttl.startswith ('del'):
            res = '╭───「เลียนแบบ」'
            res + = '\ n├สถานะ: ลบเป้าหมาย'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    หากอยู่ในช่วงกลางของการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย']:
                        settings ['mimic'] ['target'] [mid] = False
                    ไม่มี + = 1
                    ลอง:
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น:
                line.sendMessage (ถึง, 'ล้มเหลวในการลอกเลียนแบบเป้าหมาย, ไม่มีผู้ใช้คนใดพูดถึง')
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('ออกอากาศ'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「 Broadcast 」'
        res + = '\ n├ประเภทการออกอากาศ:'
        res + = '\ n│ 1: เพื่อน'
        res + = '\ n│ 2: กลุ่ม'
        res + = '\ n│ 0: ทั้งหมด'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} Broadcast'
        res + = '\ n│• {key} Broadcast <type> <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        หาก cmd == 'ออกอากาศ':
            line.sendMessage (ถึง, parsingRes (res) .format (key = setKey.title ()))
        elif cond [0] == '1':
            หาก len (cond) <2:
                return line.sendMessage (ถึง, 'ไม่สามารถออกอากาศ, ตรวจไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「สวัสดีชาวโลก」'
            เป้าหมาย = line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendMessage (ไปยัง 'ประสบความสำเร็จในการออกอากาศให้เพื่อนทุกคนส่งไปยัง% i friends'% len (เป้าหมาย))
        elif cond [0] == '2':
            หาก len (cond) <2:
                return line.sendMessage (ถึง, 'ไม่สามารถออกอากาศ, ตรวจไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「สวัสดีชาวโลก」'
            เป้าหมาย = line.getGroupIdsJoined ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendMessage (ไปยัง 'สำเร็จการกระจายไปยังกลุ่มทั้งหมดส่งไปยัง% i กลุ่ม'% len (เป้าหมาย))
        elif cond [0] == '0':
            หาก len (cond) <2:
                return line.sendMessage (ถึง, 'ไม่สามารถออกอากาศ, ตรวจไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「สวัสดีชาวโลก」'
            เป้าหมาย = line.getGroupIdsJoined () + line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendMessage (ไปยัง 'ประสบความสำเร็จในการถ่ายทอดไปยังกลุ่มและเพื่อนทั้งหมดส่งไปยัง% i กลุ่มและเพื่อน ๆ '% len (เป้าหมาย))
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format (key = setKey.title ()))
    elif cmd.startswith ('friendlist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getAllContactIds ()
        cids.sort ()
        cnames = []
        ress = []
        res = '╭───「รายชื่อเพื่อน」'
        res + = '\ n├รายการ:'
        ถ้า cids:
            รายชื่อ = []
            ไม่ = 0
            หาก len (cids)> 200:
                parsed_len = len (cids) // 200 + 1
                หาจุดอยู่ในช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด * 200: (จุด + 1) * 200]:
                        ลอง:
                            contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับ cid ใน cids:
                    ลอง:
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น:
            res + = '\ n│ไม่มีอะไร'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} FriendList'
        res + = '\ n│• {key} ข้อมูล FriendList <num / name>'
        res + = '\ n│• {key} FriendList เพิ่ม <mention>'
        res + = '\ n│• {key} Del FriendList Del <พูดถึง / num / ชื่อ / ทั้งหมด>
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd == 'รายชื่อเพื่อน':
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('info'):
            ตำรา = textt [5:]. แยก (',')
            ถ้าไม่ใช่ cids:                     
return line.sendMessage (ถึง 'เพื่อนที่แสดงข้อมูลล้มเหลวไม่มีเพื่อนอยู่ในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res = '╭───「ข้อมูลติดต่อ」'
                    res + = '\ n├ MID:' + contact.mid
                    res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                    res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                ชื่อ elif! = ไม่มี:
                    ถ้าชื่อใน cnames:
                        รายชื่อผู้ติดต่อ = [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「ข้อมูลติดต่อ」'
                        res + = '\ n├ MID:' + contact.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                        res + = '\ n╰───「สวัสดีชาวโลก」'
                        line.sendMessage (ถึง, parsingRes (res))
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「รายชื่อเพื่อน」'
            res + = '\ n├สถานะ: เพิ่มเพื่อน'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            เพิ่ม = []
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.findAndAddContactsByMid (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    added.append (กลาง)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น:
                line.sendMessage (ถึง, 'ล้มเหลวในการเพิ่มผู้ติดต่อไปยังรายชื่อเพื่อนไม่มีผู้ใช้หนึ่งคนที่กล่าวถึง')
        elif texttl.startswith ('del'):
            ตำรา = textt [4:]. split (',')
            ถ้าไม่ใช่ cids:
                return line.sendMessage (ถึง, 'ไม่สามารถลบผู้ติดต่อจากรายชื่อเพื่อนไม่มีเพื่อนในรายการ')
            res = '╭───「รายชื่อเพื่อน」'
            res + = '\ n├สถานะ: เพื่อนสนิท'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            ลบแล้ว = []
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ไม่อยู่ใน cids หรือ mid ถูกลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.deleteContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.deleteContact (contact.mid)
                        name = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    deleted.append (contact.mid)
                ชื่อ elif! = ไม่มี:
                    ถ้าชื่อใน cnames:
                        รายชื่อผู้ติดต่อ = [cnames.index (ชื่อ)]
                        ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี + = 1
                        ลอง:
                            line.deleteContact (contact.mid)
                            name = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ = 'ไม่ทราบ'
                        res + = '\ n│% i % s '% (ไม่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี + = 1
                            ลอง:
                                line.deleteContact (contact.mid)
                                name = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep (0.8)
                    อื่น:
                        line.sendMessage (ถึง, 'เพื่อนที่ล้มเหลวด้วยชื่อ `% s`, ชื่อไม่ได้อยู่ในรายการ♪'% ชื่อ)
            หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
            res + = '\ n╰───「สวัสดีชาวโลก」'
            line.sendMessage (ถึง, res)
        อื่น:
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('blocklist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getBlockedContactIds ()
        cids.sort ()
        cnames = []
        ress = []
        res = '╭───「รายการบล็อก」'
        res + = '\ n├รายการ:'
        ถ้า cids:
            รายชื่อ = []
            ไม่ = 0
            หาก len (cids)> 200:
                parsed_len = len (cids) // 200 + 1
                หาจุดอยู่ในช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด * 200: (จุด + 1) * 200]:
                        ลอง:
                            contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับ cid ใน cids:
                    ลอง:
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น:
            res + = '\ n│ไม่มีอะไร'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} BlockList'
        res + = '\ n│• {key} ข้อมูลบล็อกลิสต์ <num / name>'
        res + = '\ n│• {key} BlockList เพิ่ม <mention>'
        res + = '\ n│• {key} BlockList Del <พูดถึง / num / name / all>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd == 'blocklist':
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('info'):
            ตำรา = textt [5:]. แยก (',')
            ถ้าไม่ใช่ cids:
                return line.sendMessage (ไปที่, 'การแสดงข้อมูลล้มเหลวผู้ใช้ที่ถูกบล็อก, ไม่มีผู้ใช้ในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res = '╭───「ข้อมูลติดต่อ」'
                    res + = '\ n├ MID:' + contact.mid
                    res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                    res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
                ชื่อ elif! = ไม่มี:
                    ถ้าชื่อใน cnames:
                        รายชื่อผู้ติดต่อ = [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「ข้อมูลติดต่อ」'
                        res + = '\ n├ MID:' + contact.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                        res + = '\ n╰───「สวัสดีชาวโลก」'
                        line.sendMessage (ถึง, parsingRes (res))
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「รายการบล็อก」'
            res + = '\ n├สถานะ: เพิ่มบล็อก'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            เพิ่ม = []
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.blockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    added.append (กลาง)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「สวัสดีชาวโลก」'
                line.sendMessage (ถึง, res)
            อื่น:
                line.sendMessage (ถึง, 'ผู้ติดต่อบล็อกไม่สำเร็จ, ไม่มีผู้ใช้รายใดพูดถึง')
        elif texttl.startswith ('del'):
            ตำรา = textt [4:]. split (',')
            ถ้าไม่ใช่ cids:
                return line.sendMessage (ถึง, 'ไม่สามารถปลดบล็อคผู้ติดต่อ, ไม่มีผู้ใช้ในรายการ')
            res = '╭───「รายการบล็อก」'
            res + = '\ n├สถานะ: Del Block'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            ลบแล้ว = []
            ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ไม่อยู่ใน cids หรือ mid ถูกลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.unblockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.unblockContact (contact.mid)
                        name = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ชื่อ)
                    deleted.append (contact.mid)
                ชื่อ elif! = ไม่มี:
                    ถ้าชื่อใน cnames:
                        รายชื่อผู้ติดต่อ = [cnames.index (ชื่อ)]
                        ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี + = 1
                        ลอง:
                            line.unblockContact (contact.mid)
                            name = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ = 'ไม่ทราบ'
                        res + = '\ n│% i % s '% (ไม่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            ถ้า contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี + = 1
                            ลอง:
                                line.unblockContact (contact.mid)
                                name = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep (0.8)
                    อื่น:
                        line.sendMessage (ถึง, 'ไม่สามารถปลดบล็อกผู้ใช้ที่มีชื่อ `% s`, ชื่อไม่ได้อยู่ในรายการ♪'% name)
            หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
            res + = '\ n╰───「สวัสดีชาวโลก」'
            line.sendMessage (ถึง, res)
        อื่น:
            สำหรับ res ใน ress:
                line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd == 'พูดถึงทั้งหมด':
        สมาชิก = []
        ถ้า msg.toType == 1:
            room = line.getCompactRoom (ถึง)
            members = [mem.mid สำหรับ mem ใน room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup (ถึง)
            สมาชิก = [mem.mid สำหรับ mem ใน group.members]
        อื่น:
            return line.sendMessage (ถึง 'สมาชิกที่ไม่ได้กล่าวถึงทั้งหมดใช้คำสั่งนี้เฉพาะห้องแชทหรือกลุ่ม')
        ถ้าสมาชิก:
            พูดถึงสมาชิก (ถึงสมาชิก)
    elif cmd == 'groupinfo':
        ถ้า msg.toType! = 2: return line.sendMessage (ถึง, 'ข้อมูลกลุ่มการแสดงผลที่ล้มเหลวใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ลอง:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        ยกเว้น:
            ccreator = ไม่มี
            gcreator = 'ไม่พบ'
        ถ้าไม่ได้เป็นกลุ่ม invitee:
            pendings = 0
        อื่น:
            pendings = len (group.invitee)
        qr = 'ปิด' ถ้า group.preventedJoinByTicket อื่น 'เปิด'
        ถ้า group.preventedJoinByTicket:
            ticket = 'ไม่พบ'
        อื่น:
            ticket = 'https://line.me/R/ti/g/' + str (line.reissueGroupTicket (group.id))
        สร้าง = time.strftime ('% d-% m-% Y% H:% M:% S', time.localtime (int (group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「ข้อมูลกลุ่ม」'
        res + = '\ n├ ID:' + group.id
        res + = '\ n├ชื่อ:' + group.name
        res + = '\ n├ผู้สร้าง:' + gcreator
        res + = '\ n├เวลาที่สร้าง:' + สร้างแล้ว
        res + = '\ n├จำนวนสมาชิก:' + str (len (group.members))
        res + = '\ n├จำนวนที่รอดำเนินการ:' + str (pendings)
        res + = '\ n├สถานะ QR:' + qr
        res + = '\ n├ตั๋ว:' + ตั๋ว
        res + = '\ n╰───「สวัสดีชาวโลก」'
        line.sendImageWithURL (ไปยังเส้นทาง)
        ถ้า ccreator:
            line.sendContact (ถึง, ccreator)
        line.sendMessage (ถึง, res)
    elif cmd.startswith ('grouplist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        gids = line.getGroupIdsJoined ()
        gnames = []
        ress = []
        res = '╭───「รายชื่อกลุ่ม」'
        res + = '\ n├รายการ:'
        ถ้า gids:
            groups = line.getGroups (gids)
            ไม่ = 0
            ถ้า len (กลุ่ม)> 200:
                parsed_len = len (กลุ่ม) // 200 + 1
                หาจุดอยู่ในช่วง (parsed_len):       
สำหรับสมาชิกในสมาชิก [จุด * 200: (จุด + 1) * 200]:
                ไม่มี + = 1
                res + = '\ n│% i % s '% (ไม่, member.displayName)
                ถ้าสมาชิก == สมาชิก [-1]:
                    res + = '\ n╰───「สวัสดีชาวโลก」'
            ถ้า res:
                ถ้า res.startswith ('\ n'): res = res [1:]
                line.sendMessage (ถึง, res)
            res = ''
    elif cmd == 'openqr':
        ถ้า msg.toType! = 2: return line.sendMessage (ถึง, 'ล้มเหลวในการเปิด qr, ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        group.preventedJoinByTicket = False
        line.updateGroup (กลุ่ม)
        line.sendMessage (ไปที่ 'เปิดกลุ่มที่ประสบความสำเร็จคุณต้องระวัง')
    elif cmd == 'closeqr':
        ถ้า msg.toType! = 2: return line.sendMessage (ถึง, 'ล้มเหลวปิด qr, ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        group.preventedJoinByTicket = True
        line.updateGroup (กลุ่ม)
        line.sendMessage (ถึง, 'ความสำเร็จของกลุ่มปิด qr')
    elif cmd.startswith ('changegroupname'):
        ถ้า msg.toType! = 2: return line.sendMessage (ถึง, 'ชื่อกลุ่มการเปลี่ยนแปลงที่ล้มเหลวใช้คำสั่งนี้เฉพาะในการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        gname = removeCmd (ข้อความ setKey)
        ถ้า len (gname)> 50:
            return line.sendMessage (ถึง 'ชื่อกลุ่มการเปลี่ยนแปลงที่ล้มเหลวจำนวนชื่อต้องไม่เกิน 50')
        group.name = gname
        line.updateGroup (กลุ่ม)
        line.sendMessage (เป็น, 'เปลี่ยนชื่อกลุ่มสำเร็จเป็น `% s`'% gname)
    elif cmd == 'changegrouppict':
        ถ้า msg.toType! = 2: return line.sendMessage (ไปที่ 'รูปภาพกลุ่มการเปลี่ยนแปลงที่ล้มเหลวใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        หากไม่อยู่ในการตั้งค่า ['changeGroupPicture']:
            การตั้งค่า [ 'changeGroupPicture']. ผนวก (เพื่อ)
            line.sendMessage (ไปที่ 'โปรดส่งภาพพิมพ์' {key} Abort` หากต้องการยกเลิก \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพ'.format (key = setKey.title)) นานเกินไป
        อื่น:
            line.sendMessage (ไปยัง 'คำสั่งเปิดใช้งานอยู่แล้วโปรดส่งภาพหรือพิมพ์ `{key} ยกเลิก' หากต้องการยกเลิก \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัปโหลด image'.format (key = setKey.title นานเกินไป) ()))
    elif cmd == 'kickall':
        ถ้า msg.toType! = 2: return line.sendMessage (ไปที่ 'ไม่เตะสมาชิกทั้งหมดใช้คำสั่งนี้เฉพาะในการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ถ้าไม่ใช่กลุ่มสมาชิก:
            return line.sendMessage (ถึง, 'ล้มเหลวในการเตะสมาชิกทั้งหมด, ไม่มีสมาชิกในรายการ')
        สำหรับสมาชิกใน group.members:
            ถ้า member.mid == myMid:
                ต่อ
            ลอง:
                line.kickoutFromGroup (ถึง, [member.mid])
            ยกเว้น TalkException ในฐานะ talk_error:
                return line.sendMessage (ไปที่, 'เตะไม่ได้สมาชิกทุกคน, เหตุผลคือ `% s' '% talk_error.reason)
            time.sleep (0.8)
        line.sendMessage (ถึง, 'สำเร็จการเตะสมาชิกทั้งหมด, ยอดรวม% i สมาชิก'% len (group.members))
    elif cmd == 'cancelall':
        ถ้า msg.toType! = 2: return line.sendMessage (ไปที่ 'ล้มเหลวในการยกเลิกสมาชิกที่รออนุมัติทั้งหมดใช้คำสั่งนี้เฉพาะในการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ถ้าไม่ได้เป็นกลุ่ม invitee:
            return line.sendMessage (ถึง, 'ล้มเหลวในการยกเลิกสมาชิกที่รอดำเนินการทั้งหมด, ไม่มีสมาชิกรอดำเนินการในรายการ')
        สำหรับสมาชิกใน group.invitee:
            ถ้า member.mid == myMid:
                ต่อ
            ลอง:
                line.cancelGroupInvitation (ถึง, [member.mid])
            ยกเว้น TalkException ในฐานะ talk_error:
                return line.sendMessage (ไปที่ 'ล้มเหลวในการยกเลิกสมาชิกที่รอดำเนินการทั้งหมดเหตุผลคือ `% s' '% talk_error.reason)
            time.sleep (0.8)
        line.sendMessage (ถึง 'สำเร็จยกเลิกสมาชิกที่รออนุมัติทั้งหมดรวม% i สมาชิกที่รออนุมัติ'% len (pendings))
    elif cmd.startswith ('lurk'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        หาก msg.toType ใน [1, 2] และไม่อยู่ในที่ซุ่มซ่อน:
            ซุ่มซ่อน [เพื่อ] = {
                'สถานะ': เท็จ
                'เวลา': ไม่มี
                'สมาชิก': [],
                'ตอบกลับ': {
                    'สถานะ': เท็จ
                    'message': settings ['defaultReplyReader']
                }
            }
        res = '╭───「ที่ซุ่มซ่อน」'
        หาก msg.toType ใน [1, 2]: res + = '\ n├สถานะ:' + bool_dict [ที่ซุ่มซ่อน [ถึง] ['สถานะ']] [1]
        ถ้า msg.toType ใน [1, 2]: res + = '\ n├ผู้อ่านที่ตอบกลับ:' + bool_dict [ที่ซุ่มซ่อน [ถึง] ['ตอบ'] ['สถานะ']] [1]
        ถ้า msg.toType ใน [1, 2]: res + = '\ n├ข้อความตอบกลับของผู้อ่าน:' + ที่ซุ่มซ่อน [ถึง] ['ตอบ'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} Lurk'
        res + = '\ n│• {key} Lurk <เปิด / ปิด>'
        res + = '\ n│• {key} ผลลัพธ์แฝงตัว'
        res + = '\ n│• {key} Lurk รีเซ็ต'
        res + = '\ n│• {key} Lurk ReplyReader <เปิด / ปิด>'
        res + = '\ n│• {key} Lurk ReplyReader <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'lurk':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        ไม่ได้อยู่ใน [1, 2]:
            return line.sendMessage (ไปที่, 'ล้มเหลวในการรันคำสั่ง, ใช้คำสั่งนี้เฉพาะในห้องหรือแชทเป็นกลุ่ม')
        elif texttl == 'เปิด':
            ถ้าซุ่มซ่อน [ถึง] ['สถานะ']:
                line.sendMessage (ถึง, 'Lurking เปิดใช้งานแล้ว')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': จริง
                    'เวลา': datetime.now (tz = pytz.timezone ('เอเชีย / จาการ์ตา')) strftime ('% Y-% m-% d% H:% M:% S'),
                    'สมาชิก': []
                })
                line.sendMessage (ถึง, 'การเปิดใช้งานการดักสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendMessage (ถึง, 'Lurking deactive แล้ว')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': เท็จ
                    'เวลา': ไม่มี
                    'สมาชิก': []
                })
                line.sendMessage (ถึง 'ความสำเร็จปิดการใช้งานการซุ่มโจมตี')
        elif texttl == 'ผลลัพธ์':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendMessage (ถึง, 'การแสดงผลที่ไม่สามารถดักซุ่ม, การดักซุ่มยังไม่ได้เปิดใช้งาน')
            อื่น:
                ถ้าไม่ซุ่มซ่อน [กับ] ['members']:
                    line.sendMessage (ไปที่ 'แสดงผลการดักไม่สำเร็จไม่มีสมาชิกที่อ่าน')
                อื่น:
                    members = ซุ่มซ่อน [to] ['members']
                    res = '╭───「ที่ซุ่มซ่อน」'
                    ถ้า msg.toType == 2: res + = '\ n├ชื่อกลุ่ม:' + line.getGroup (ถึง) .name
                    parsed_len = len (สมาชิก) // 200 + 1
                    ไม่ = 0
                    หาจุดอยู่ในช่วง (parsed_len):
                        สำหรับสมาชิกในสมาชิก [จุด * 200: (จุด + 1) * 200]:
                            ไม่มี + = 1
                            ลอง:
                                name = line.getContact (สมาชิก) .displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ชื่อ)
                            ถ้าสมาชิก == สมาชิก [-1]:
                                res + = '\ n│'
                                res + = '\ n├ตั้งเวลา:' + ที่ซุ่มซ่อน [ถึง] ['เวลา']
                                res + = '\ n╰───「สวัสดีชาวโลก」'
                        ถ้า res:
                            ถ้า res.startswith ('\ n'): res = res [1:]
                            line.sendMessage (ถึง, res)
                        res = ''
        elif texttl == 'รีเซ็ต':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendMessage (ถึง, 'การรีเซ็ตที่ซ่อนไม่สำเร็จ, การซุ่มซ่อนไม่ได้เปิดใช้งาน')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': จริง
                    'เวลา': datetime.now (tz = pytz.timezone ('เอเชีย / จาการ์ตา')) strftime ('% Y-% m-% d% H:% M:% S'),
                    'สมาชิก': []
                })
                line.sendMessage (ถึง, 'การตั้งค่าใหม่สำเร็จแล้ว')
        elif texttl.startswith ('replyreader'):
            ตำรา = textt [12:]
            หากตำรา == 'เปิด':
                ถ้าซุ่มซ่อน [ถึง] ['ตอบ'] ['สถานะ']:
                    line.sendMessage (ถึง, 'ผู้อ่านตอบใช้งานอยู่แล้ว')
                อื่น:
                    ที่ซุ่มซ่อน [ถึง] ['reply'] ['สถานะ'] = จริง
                    line.sendMessage (ถึง 'ผู้อ่านตอบกลับที่เปิดใช้งานสำเร็จ')
            elif ตำรา == 'ปิด':
                ถ้าไม่ซุ่มซ่อน [กับ] ['ตอบ'] ['สถานะ']:
                    line.sendMessage (ถึง, 'ผู้อ่านตอบกลับใช้งานไม่ได้แล้ว')
                อื่น:
                    ที่ซุ่มซ่อน [ถึง] ['reply'] ['สถานะ'] = False
                    line.sendMessage (ถึง 'ผู้อ่านที่ตอบกลับการปิดการใช้งานสำเร็จ')
            อื่น:
                ซุ่มซ่อน [ถึง] ['reply'] ['message'] = ข้อความ
                line.sendMessage (เป็น, 'สำเร็จตั้งค่าข้อความตอบกลับของผู้อ่านเป็นข้อความ% `` s' '%)
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('ทักทาย'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「ทักทายข้อความ」'
        res + = '\ n├คำทักทายเข้าร่วมสถานะ:' + bool_dict [การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']] [1]
        res + = '\ n├ข้อความทักทายเข้าร่วม:' + การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['ข้อความ']
        res + = '\ n├ทักทายสถานะการลา:' + bool_dict [การตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']] [0]
        res + = '\ n├ทักทายเข้าร่วมข้อความ:' + การตั้งค่า ['ทักทาย'] ['ออก'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} Greet'
        res + = '\ n│• {key} ทักทายเข้าร่วม <เปิด / ปิด>'
        res + = '\ n│• {key} ทักทายเข้าร่วม <message>'
        res + = '\ n│• {key} สวัสดีปล่อยให้ <เปิด / ปิด>'
        res + = '\ n│• {key} ขอลา <message>'
        res + = '\ n╰───「สวัสดีชาวโลก」'
        ถ้า cmd == 'ทักทาย':
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('เข้าร่วม'):
            ตำรา = textt [5:]
            ตำราl = ตำรา.lower ()
            หากตำรา l == 'เปิด':
                หากการตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']:
                    line.sendMessage (ถึง 'ทักทายเข้าร่วมใช้งานอยู่แล้ว')
                อื่น:
                    การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ'] = จริง
                    line.sendMessage (ถึง "เข้าร่วมทักทายเปิดใช้งานสำเร็จแล้ว")
            elif ตำราl == 'ปิด':
                หากไม่มีการตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']:
                    line.sendMessage (ถึง, 'ทักทายเข้าร่วมแล้วปิดการใช้งาน')
                อื่น:
                    การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ'] = เท็จ
                    line.sendMessage (ถึง 'เข้าร่วมการปิดการทักทายที่ประสบความสำเร็จ')
            อื่น:
                การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['ข้อความ'] = ข้อความ
                line.sendMessage (เป็น, 'ทักทายเปลี่ยนความสำเร็จเข้าร่วมข้อความเป็นข้อความ'% s` '%)
        elif texttl.startswith ('ออก'):
            ตำรา = textt [6:]
            ตำราl = ตำรา.lower ()
            หากตำรา l == 'เปิด':
                หากการตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']:
                    line.sendMessage (ถึง 'ทักทายออกจากการใช้งานแล้ว')
                อื่น:
                    การตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ'] = จริง
                    line.sendMessage (ถึง 'เปิดใช้งานการทักทายสำเร็จแล้วปล่อยให้')
            elif ตำราl == 'ปิด':
                หากไม่มีการตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']:
                    line.sendMessage (ถึง, 'สวัสดีแล้วปล่อยให้ deactive แล้ว')
                อื่น:
                    การตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ'] = เท็จ
                    line.sendMessage (ไปยัง 'ออกจากความสำเร็จปิดการทักทาย')
            อื่น:
                settings ['greet'] ['ออก'] ['message'] = ข้อความ
                line.sendMessage (เป็น 'การทักทายเปลี่ยนความสำเร็จฝากข้อความถึงข้อความ'% s` '%%)
        อื่น:
            line.sendMessage (ถึง, parsingRes (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('kick'):
        ถ้า msg.toType! = 2: return line.sendMessage (ถึง, 'สมาชิกเตะไม่สำเร็จให้ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        ถ้า 'MENTION' ใน msg.contentMetadata.keys ():
            mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
            สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                mid = พูดถึง ['M']
                ถ้า mid == myMid:
                    ต่อ
                ลอง:
                    line.kickoutFromGroup (ถึง, [กลาง])
                ยกเว้น TalkException ในฐานะ talk_error:
                    return line.sendMessage (ถึง, 'สมาชิกเตะไม่สำเร็จเหตุผลคือ `% s' '% talk_error.reason)
                time.sleep (0.8)
            line.sendMessage (ถึง, 'สมาชิกที่ประสบความสำเร็จเตะทั้งหมด% i สมาชิก'% len (กล่าวถึง ['MENTIONEES'])
        อื่น:
line.sendMessage (ถึง, 'สมาชิก vultra kicked ไม่สำเร็จ, โปรดระบุผู้ใช้ที่คุณต้องการเตะ')

def executeOp (op):
    ลอง:
        พิมพ์ ('++ การทำงาน: (% i)% s'% (op.type, OpType._VALUES_TO_NAMES [op.type] .replace ('_', '')))
        ถ้า op.type == 5:
            หากการตั้งค่า ['autoAdd'] ['สถานะ']:
                line.findAndAddContactsByMid (op.param1)
            หากการตั้งค่า ['autoAdd'] ['ตอบกลับ']:
                ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoAdd'] ['ข้อความ']:
                    line.sendMessage (op.param1, การตั้งค่า ['autoAdd'] ['ข้อความ'])
                อื่น:
                    line.sendMentionV2 (op.param1, การตั้งค่า ['autoAdd'] ['ข้อความ'], [op.param1])
        ถ้า op.type == 13:
            หากการตั้งค่า ['autoJoin'] ['สถานะ'] และ myMid ใน op.param3:
                line.acceptGroupInvitation (op.param1)
                หากการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                    ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoJoin'] ['ข้อความ']:
                        line.sendMessage (op.param1, การตั้งค่า ['autoJoin'] ['ข้อความ'])
                    อื่น:
                        line.sendMentionV2 (op.param1, การตั้งค่า ['autoJoin'] ['ข้อความ'], [op.param2])
        ถ้า op.type == 15:
            หากการตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']:
                ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['ทักทาย'] ['ออก'] ['ข้อความ']:
                    line.sendMessage (op.param1, การตั้งค่า ['ทักทาย'] ['ออก'] ['ข้อความ']. รูปแบบ (ชื่อ = line.getCompactGroup (op.param1) .name))
                อื่น:
                    line.sendMentionV2 (op.param1, การตั้งค่า ['ทักทาย'] ['ออก'] ['ข้อความ']. รูปแบบ (ชื่อ = line.getCompactGroup (op.param1) .name), [op.param2]
        ถ้า op.type == 17:
            หากการตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']:
                ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['ข้อความ']:
                    line.sendMessage (op.param1, การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['ข้อความ']. รูปแบบ (ชื่อ = line.getCompactGroup (op.param1) .name))
                อื่น:
                    line.sendMentionV2 (op.param1, การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['ข้อความ']. รูปแบบ (ชื่อ = line.getCompactGroup (op.param1) .name), [op.param2]
        ถ้า op.type == 25:
            msg = op.message
            text = str (msg.text)
            msg_id = msg.id
            รับ = msg.to
            ผู้ส่ง = msg._ จาก
            เพื่อ = ผู้ส่งหากไม่ใช่ msg.toType และผู้ส่ง! = myMid ผู้รับอื่น ๆ
            txt = text.lower ()
            cmd = command (ข้อความ)
            setKey = settings ['setKey'] ['key'] หากการตั้งค่า ['setKey'] ['สถานะ'] else ''
            ถ้าข้อความใน tmp_text:
                return tmp_text.remove (ข้อความ)
            ถ้า msg.contentType == 0: # ประเภทเนื้อหาคือข้อความ
                หาก '/ ti / g /' เป็นข้อความและการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    regex = re.compile ('(?: line \: \ / | line \ .me \ / R) \ / ti \ / g \ / ([a-zA-Z0-9 _-] +)')
                    ลิงก์ = regex.findall (ข้อความ)
                    ตั๋ว = []
                    gids = line.getGroupIdsJoined ()
                    สำหรับลิงค์ในลิงค์:
                        หากลิงก์ไม่ได้อยู่ในตั๋ว:
                            tickets.append (ลิงค์)
                    สำหรับตั๋วในตั๋ว:
                        ลอง:
                            group = line.findGroupByTicket (ตั๋ว)
                        ยกเว้น:
                            ต่อ
                        ถ้า group.id เป็น gids:
                            line.sendMessage (ถึง, 'ฉัน \' อยู่ในกลุ่ม '+ group.name)
                            ต่อ
                        line.acceptGroupInvitationByTicket (group.id ตั๋ว)
                        หากการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                            ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoJoin'] ['ข้อความ']:
                                line.sendMessage (ไปยังการตั้งค่า ['autoJoin'] ['ข้อความ'])
                            อื่น:
                                line.sendMentionV2 (ไปยังการตั้งค่า ['autoJoin'] ['ข้อความ'], [ผู้ส่ง])
                        line.sendMessage (ถึง 'ประสบความสำเร็จในการเข้าร่วมกลุ่ม' + group.name)
                ลอง:
                    executeCmd (msg, ข้อความ, txt, cmd, msg_id, ผู้รับ, ผู้ส่ง, ถึง, setKey)
                ยกเว้น TalkException ในฐานะ talk_error:
                    : ฟังก์ชัน LogError (talk_error)
                    ถ้า talk_error.code ใน [7, 8, 20]:
                        sys.exit (1)
                    line.sendMessage (ถึง, 'เรียกใช้งานคำสั่งผิดพลาด' + str (talk_error))
                    time.sleep (3)
                ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
                    : ฟังก์ชัน LogError (ผิด)
                    line.sendMessage (ถึง, 'เรียกใช้งานคำสั่งผิดพลาด' + str (ข้อผิดพลาด))
                    time.sleep (3)
            elif msg.contentType == 1: # ประเภทเนื้อหาคือรูปภาพ
                หากการตั้งค่า ['changePictureProfile']:
                    path = line.downloadObjectMsg (msg_id, saveAs = 'tmp / picture.jpg')
                    line.updateProfilePicture (เส้นทาง)
                    line.sendMessage (เป็น, 'เปลี่ยนโปรไฟล์ภาพให้สำเร็จ')
                    settings ['changePictureProfile'] = เท็จ
                การตั้งค่า elif ['changeCoverProfile']:
                    path = line.downloadObjectMsg (msg_id, saveAs = 'tmp / cover.jpg')
                    line.updateProfileCover (เส้นทาง)
                    line.sendMessage (เป็น 'โปรไฟล์การเปลี่ยนแปลงความสำเร็จที่ครอบคลุม')
                    settings ['changeCoverProfile'] = เท็จ
                elif to in settings ['changeGroupPicture'] และ msg.toType == 2:
                    path = line.downloadObjectMsg (msg_id, saveAs = 'tmp / grouppicture.jpg')
                    line.updateGroupPicture (ไปยังเส้นทาง)
                    line.sendMessage (เป็น 'รูปภาพเปลี่ยนกลุ่มสำเร็จ')
                    การตั้งค่า [ 'changeGroupPicture']. ลบ (เพื่อ)
            elif msg.contentType == 7: # ประเภทเนื้อหาคือสติ๊กเกอร์
                หากการตั้งค่า ['checkSticker']:
                    res = '╭───「ข้อมูลสติ๊กเกอร์」'
                    res + = '\ n├รหัสสติกเกอร์:' + msg.contentMetadata ['STKID']
                    res + = '\ n├รหัสแพคเกจสติกเกอร์:' + msg.contentMetadata ['STKPKGID']
                    res + = '\ n├เวอร์ชั่นสติกเกอร์:' + msg.contentMetadata ['STKVER']
                    res + = '\ n├ลิงค์ของสติ๊กเกอร์: บรรทัด: // shop / detail /' + msg.contentMetadata ['STKPKGID']
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    line.sendMessage (ถึง, parsingRes (res))
            elif msg.contentType == 13: # ประเภทเนื้อหาคือที่ติดต่อ
                หากการตั้งค่า ['checkContact']:
                    mid = msg.contentMetadata ['mid']
                    ลอง:
                        contact = line.getContact (กลาง)
                    ยกเว้น:
                        return line.sendMessage (ถึง "ไม่สามารถรับรายละเอียดการติดต่อกับ mid" + mid)
                    res = '╭───「รายละเอียดผู้ติดต่อ」'
                    res + = '\ n├ MID:' + กลาง
                    res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                    res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                    res + = '\ n╰───「สวัสดีชาวโลก」'
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL (กลาง)
                    line.sendImageWithURL (ถึง, str (ปก))
                    line.sendMessage (ถึง, parsingRes (res))
            elif msg.contentType == 16: # ประเภทเนื้อหาคืออัลบั้ม / โน้ต
                หากการตั้งค่า ['checkPost']:
                    หาก msg.contentMetadata ['serviceType'] ใน ['GB', 'NT', 'MH']:
                        หาก msg.contentMetadata ['serviceType'] ใน ['GB', 'NT']:
                            contact = line.getContact (ผู้ส่ง)
                            ผู้เขียน = contact.displayName
                        อื่น:
                            ผู้เขียน = msg.contentMetadata ['serviceName']
                        posturl = msg.contentMetadata ['postEndUrl']
                        res = '╭───「รายละเอียดโพสต์」'
                        res + = '\ n├ผู้สร้าง:' + ผู้แต่ง
                        res + = '\ n├ลิงก์โพสต์:' + posturl
                        res + = '\ n╰───「สวัสดีชาวโลก」'
        elif op.type == 26:
            msg = op.message
            text = str (msg.text)
            msg_id = msg.id
            รับ = msg.to
            ผู้ส่ง = msg._ จาก
            เพื่อ = ผู้ส่งหากไม่ใช่ msg.toType และผู้ส่ง! = myMid ผู้รับอื่น ๆ
            txt = text.lower ()
            หากการตั้งค่า ['autoRead']:
                line.sendChatChecked (ถึง, msg_id)
            ถ้า msg.contentType == 0: # ประเภทเนื้อหาคือข้อความ
                หาก '/ ti / g /' เป็นข้อความและการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    regex = re.compile ('(?: line \: \ / | line \ .me \ / R) \ / ti \ / g \ / ([a-zA-Z0-9 _-] +)')
                    ลิงก์ = regex.findall (ข้อความ)
                    ตั๋ว = []
                    gids = line.getGroupIdsJoined ()
                    สำหรับลิงค์ในลิงค์:
                        หากลิงก์ไม่ได้อยู่ในตั๋ว:
                            tickets.append (ลิงค์)
                    สำหรับตั๋วในตั๋ว:
                        ลอง:
                            group = line.findGroupByTicket (ตั๋ว)
                        ยกเว้น:
                            ต่อ
                        ถ้า group.id เป็น gids:
                            line.sendMessage (ถึง, 'ฉัน \' อยู่ในกลุ่ม '+ group.name)
                            ต่อ
                        line.acceptGroupInvitationByTicket (group.id ตั๋ว)
                        หากการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                            ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoJoin'] ['ข้อความ']:
                                line.sendMessage (ไปยังการตั้งค่า ['autoJoin'] ['ข้อความ'])
                            อื่น:
                                line.sendMentionV2 (ไปยังการตั้งค่า ['autoJoin'] ['ข้อความ'], [ผู้ส่ง])
                        line.sendMessage (ถึง 'ประสบความสำเร็จในการเข้าร่วมกลุ่ม' + group.name)
                หากการตั้งค่า ['เลียนแบบ'] ['สถานะ']:
                    หากผู้ส่งในการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย'] และการตั้งค่า ['เลียนแบบ'] [[เป้าหมาย]] [ผู้ส่ง]:
                        ลอง:
                            line.sendMessage (ถึง, ข้อความ, msg.contentMetadata)
                            tmp_text.append (ข้อความ)
                        ยกเว้น:
                            ผ่านไป
                หากการตั้งค่า ['autoRespondMention'] ['สถานะ']:
                    ถ้า msg.toType ใน [1, 2] และ 'MENTION' ใน msg.contentMetadata.keys () และ sender! = myMid และ msg.contentType ไม่ใช่ใน [6, 7, 9]:
                        mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                        พูดถึง = [พูดถึง ['M'] เพื่อพูดถึงในการกล่าวถึง ['MENTIONEES']]
                        หาก myMid ในผู้ที่กล่าวถึง:
                            if line.getProfile (). displayName ในข้อความ:
                                ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoRespondMention'] ['ข้อความ']:
                                    line.sendMessage (ไปยังการตั้งค่า ['autoRespondMention'] ['ข้อความ'])
                                อื่น:
                                    line.sendMentionV2 (ไปยังการตั้งค่า ['autoRespondMention'] ['ข้อความ'], [ผู้ส่ง])
                หากการตั้งค่า ['autoRespond'] ['สถานะ']:
                    ถ้า msg.toType == 0:
                        contact = line.getContact (ผู้ส่ง)
                        ถ้า contact.attributes! = 32 และ 'MENTION' ไม่อยู่ใน msg.contentMetadata.keys ():
                            ถ้า '@!' ไม่ได้อยู่ในการตั้งค่า ['autoRespond'] ['message']:
                                line.sendMessage (ไปยังการตั้งค่า ['autoRespond'] ['ข้อความ'])
                            อื่น:
                                line.sendMentionV2 (ไปยังการตั้งค่า ['autoRespond'] ['ข้อความ'], [ผู้ส่ง])
        ถ้า op.type == 55:
            ถ้า op.param1 เป็นที่ซุ่มซ่อน:
                หากที่ซุ่มซ่อน [op.param1] ['สถานะ'] และ op.param2 ไม่อยู่ในที่ซุ่มซ่อน [op.param1] ['members']:
                    ซุ่มซ่อน [op.param1] [ 'สมาชิก']. ผนวก (op.param2)
                    ถ้าซุ่มซ่อน [op.param1] ['ตอบกลับ'] ['สถานะ']:
                        ถ้า '@!' ไม่ได้อยู่ในที่ซุ่มซ่อน [op.param1] ['reply'] ['ข้อความ']:
                            line.sendMessage (op.param1, ซุ่มซ่อน [op.param1] ['ตอบกลับ'] ['ข้อความ'])
                        อื่น:
                            line.sendMentionV2 (op.param1, ซุ่มซ่อน [op.param1] ['ตอบกลับ'] ['ข้อความ'], [op.param2])
    ยกเว้น TalkException ในฐานะ talk_error:
        : ฟังก์ชัน LogError (talk_error)
        ถ้า talk_error.code ใน [7, 8, 20]:
            sys.exit (1)
    ยกเว้น KeyboardInterrupt:
        sys.exit ('## ---- KEYBOARD INTERRUPT ----- ##')
    ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
        : ฟังก์ชัน LogError (ผิด)

def runningProgram ():
    หากการตั้งค่า ['restartPoint'] ไม่ใช่ไม่ใช่:
        ลอง:
            line.sendMessage (การตั้งค่า ['restartPoint'], 'Bot สามารถทำงานได้อีกครั้ง♪')
        ยกเว้น TalkException:
            ผ่านไป
        settings ['restartPoint'] = ไม่มี
    ในขณะที่ True:
        ลอง:
            ops = oepoll.singleTrace (count = 50)
        ยกเว้น TalkException ในฐานะ talk_error:
            : ฟังก์ชัน LogError (talk_error)
            ถ้า talk_error.code ใน [7, 8, 20]:
                sys.exit (1)
            ต่อ
        ยกเว้น KeyboardInterrupt:
            sys.exit ('## ---- KEYBOARD INTERRUPT ----- ##')
        ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
            : ฟังก์ชัน LogError (ผิด)
            ต่อ
        ถ้า ops:
            สำหรับ op ใน ops:
                executeOp (สหกรณ์)
                oepoll.setRevision (op.revision)

ถ้า __name__ == '__main__':
    พิมพ์ ('## ---- โปรแกรมการทำงาน ----- ##')
    runningProgram ()
