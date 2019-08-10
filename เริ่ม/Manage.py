# ! / usr / bin / env python
นำเข้าระบบปฏิบัติการ
sys นำเข้า

ถ้า __name__  ==  " __main__ " :
    os.environ.setdefault ( " DJANGO_SETTINGS_MODULE " , " gettingstarted.settings " )

    จาก django.core.management นำเข้า execute_from_command_line

    execute_from_command_line (sys.argv)
