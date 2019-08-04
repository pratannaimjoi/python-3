# - * - การเข้ารหัส: utf-8 - * -
"""
LINE Python - API ส่วนตัวของ LINE Messaging
=========================================
    >>>จากการนำเข้า linepy *
การเชื่อมโยง
`` `` `
* `ที่เก็บ GitHub <https://github.com/fadhiilrachman/line-py>` _
"""
จาก __future__  นำเข้า with_statement
นำเข้าอีกตัวแปลงสัญญาณ

ลอง :
    จากการตั้งค่าการนำเข้า setuptools
ยกเว้น ImportError :
    จาก ez_setup นำเข้า use_setuptools
    use_setuptools ()
    จากการตั้งค่าการนำเข้า setuptools

ด้วย open ( ' linepy / __ init__.py ' ) เป็น f:
    รุ่น= re.search ( r ' __version__ \ s * = \ s * \' ( . +? ) \ ' ' , f.read ()) กลุ่ม ( 1 )
ยืนยันรุ่น

ด้วย open ( ' README.rst ' ) เป็น f:
    ติดตั้ง(
        ชื่อ= ' linepy ' ,
        packages = [ ' linepy ' ],
        รุ่น=รุ่น
        ใบอนุญาต= ' BSD 3 ข้อใบอนุญาต' ,
        ผู้เขียน= ' Fadhiil Rachman ' ,
        author_email = ' fadhiilrachman@gmail.com ' ,
        url = ' https://github.com/fadhiilrachman/line-py ' ,
        คำอธิบาย= 'สาย Messaging \' s API ส่วนตัว' ,
        long_description = f.read ()
        classifiers = [
            'สถานะการพัฒนา :: 4 - Beta ' ,
            'สิ่งแวดล้อม :: คอนโซล' ,
            'ผู้ชมที่ตั้งใจ :: นักพัฒนา' ,
            'ใบอนุญาต :: OSI อนุมัติ :: BSD ใบอนุญาต' ,
            'ระบบปฏิบัติการ :: ระบบปฏิบัติการอิสระ' ,
            'การเขียนโปรแกรมภาษา :: Python ' ,
            'ภาษาโปรแกรม :: Python :: 3 ' ,
            'ภาษาโปรแกรม :: Python :: 3.1 ' ,
            'การเขียนโปรแกรมภาษา Python :: :: 3.2 ' ,
            'ภาษาโปรแกรม :: Python :: 3.3 ' ,
            'ภาษาโปรแกรม :: Python :: 3.4 ' ,
            'การเขียนโปรแกรมภาษา Python :: :: 3.5 ' ,
            'การเขียนโปรแกรมภาษา Python :: :: 3.6 ' ,
            'ภาษาโปรแกรม :: Python :: 3.7 ' ,
            'การเขียนโปรแกรมภาษา Python :: :: การดำเนินงาน :: CPython ' ,
            'การเขียนโปรแกรมภาษา Python :: :: การดำเนินงาน :: PyPy ' ,
            'หัวข้อ :: การพัฒนาซอฟต์แวร์ :: ไลบรารี :: Python Modules ' ,
            'หัวข้อ :: อินเทอร์เน็ต :: WWW / HTTP :: เนื้อหาแบบไดนามิก' ,
            'หัวข้อ :: การสื่อสาร :: การแชท' ,
        ]
        install_requires = [
            ' Akad ' ,
            'ร้องขอ' ,
            'อาร์เอส' ,
            ' PyQRCode '
        ]
    )
