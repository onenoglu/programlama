def katmaDegerCiroHesapla():
    a=int(input('Toplam Satış Miktarını giriniz:'))
    b=int(input('Hammadde Maliyetini giriniz:'))
    c=int(input('Bakım Onarım Giderlerini giriniz:'))
    d=int(input('Sevkiyat giderlerini giriniz:'))
    e=int(input('Satın alınan hizmet gierlerini giriniz:'))
    katmaDegerCiro=a-(b+c+d+e)
    if (katmaDegerCiro>1000):
        print('Katma değer cironuz:',katmaDegerCiro,'İşletme katma değer cirosu yüksek.')
    elif (katmaDegerCiro>=500):
        print('Katma değer cironuz:',katmaDegerCiro,'İşletme katma değer cirosu normal.')
    else:
        print('Katma değer cironuz:',katmaDegerCiro,'işletme katma değer cirosu düşük.')
