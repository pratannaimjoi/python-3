จาก django.contrib.auth.models นำเข้า AnonymousUser ผู้ใช้
จาก django.test นำเข้า TestCase, RequestFactory

จาก . views ดัชนีการนำเข้า


คลาส SimpleTest ( TestCase ):
    def  setUp ( ตัวเอง ):
        #การทดสอบทุกครั้งจำเป็นต้องเข้าถึงโรงงานที่ร้องขอ
        โรงงาน. ตนเอง= RequestFactory ()

    def  test_details ( ตนเอง ):
        #สร้างตัวอย่างของคำขอ GET
        ขอ=  self .factory.get ( " / " )
        request.user = AnonymousUser ()

        #ทดสอบ my_view () ราวกับว่ามันถูกปรับใช้ที่ / ลูกค้า / รายละเอียด
        response = index (ร้องขอ)
        ตนเอง. assEqual (response.status_code, 200 )
