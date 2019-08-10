# Spoon-Knife
# Python: เริ่มต้น

แอพพลิเคชั่น Django ซึ่งสามารถนำไปใช้กับ Heroku ได้อย่างง่ายดาย

แอปพลิเคชันนี้สนับสนุนบทความ [เริ่มต้นใช้งาน Python ใน Heroku] (https://devcenter.heroku.com/articles/getting-started-with-python) บทความ - ลองดูสิ

## เรียกใช้ในเครื่อง

ตรวจสอบให้แน่ใจว่าคุณมี Python 3.7 [ติดตั้งภายในเครื่อง] (http://install.python-guide.org) ในการผลักดันไปยัง Heroku คุณจะต้องติดตั้ง [Heroku CLI] (https://devcenter.heroku.com/articles/heroku-cli) รวมถึง [Postgres] (https://devcenter.heroku.com / บทความ / Heroku-PostgreSQL # ท้องถิ่นติดตั้ง)

`` `ดวลจุดโทษ
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python เริ่มต้นใช้งาน

$ python3 -m venv เริ่มต้นใช้งาน
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python Manage.py โยกย้าย
$ python Manage.py สะสม

$ heroku ในประเทศ
`` `

แอปของคุณควรทำงานบน [localhost: 5000] (http: // localhost: 5000 /)

## ปรับใช้กับ Heroku

`` `ดวลจุดโทษ
$ heroku สร้าง
$ git ผลักดัน heroku master

$ heroku เรียกใช้ python Manage.py โยกย้าย
เปิด $ heroku
`` `
หรือ

[[ปรับใช้] (https://www.herokucdn.com/deploy/button.svg)] (https://heroku.com/deploy)

## เอกสารประกอบ

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ Python ใน Heroku ให้ดูบทความ Dev Center เหล่านี้:

- [Python บน Heroku] (https://devcenter.heroku.com/categories/python)
