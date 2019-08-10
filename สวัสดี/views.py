จาก django.shortcuts นำเข้าการแสดงผล
จาก django.http นำเข้า HttpResponse

จาก. model นำเข้าคำทักทาย

#สร้างมุมมองของคุณที่นี่
 ดัชนีdef ( ตามคำขอ ):
    # return HttpResponse ('สวัสดีจาก Python!')
    ส่งคืนการแสดงผล (คำขอ" index.html " )


def  db ( คำขอ ):

    อวยพร=อวยพร ()
    greeting.save ()

    greetings = Greeting.objects.all ()

    ส่งคืนการแสดงผล (คำขอ, " db.html " , { "ทักทาย" : greetings})
