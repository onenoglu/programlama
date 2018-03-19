def musteriCalismaSuresi2016():
    calSur=int(170)
    topMusSa=int(50)
    print('Çalışma süresi:',calSur)
    print('Toplam müşteri sayısı:',topMusSa)
    global musCalSur2016
    musCalSur2016=calSur/topMusSa
    print('2016 Yılı müşteri çalışma süresi:')
    return musCalSur2016
def musteriCalismaSuresi2017():
    calSur=int(220)
    topMusSa=int(70)
    print('Çalışma süresi:',calSur)
    print('Toplam müşteri sayısı:',topMusSa)
    global musCalSur2017
    musCalSur2017=calSur/topMusSa
    print('2017 yılı müşteri çalışma süresi:')
    return musCalSur2017
def yillarArasiFark(musCalSur2016,musCalSur2017):
    yillarArasiFark=musCalSur2017-musCalSur2016
    print('Yıllar arasındaki müşteri çalışma süresi farkı:',yillarArasiFark)
calismaSure2016=musteriCalismaSuresi2016()
calismaSure2017=musteriCalismaSuresi2017()
yıllarArasiFark(calismaSure2016,calismaSure2017)
