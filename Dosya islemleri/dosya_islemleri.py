
#f = open('deneme.txt', 'r')
#icerik = f.read()
#print(icerik)
#f.close()

#with open('deneme.txt', 'r') as f:
#     icerik = f.read()
#     print(icerik)

#with open('deneme.txt', 'r') as f:
#     icerik = f.readlines()
#     print(icerik)
#
#     for satır in icerik:
#         print(satır, end='')

#with open('deneme.txt') as f:
#    for satir in f:
#        print(satir, end = '')

#with open('deneme.txt', 'r') as f:
#    satir = f.readline()
#    print(satir, end='')
#    satir = f.readline()
#    print(satir, end='')
#    satir = f.readline()
#    print(satir, end='')

#with open('deneme.txt') as f:
#    satir = f.readline()
#    print(satir, end='')
#    pozisyon = f.tell()
#    print(pozisyon)
#    satir = f.readline()
#    print(satir, end='')
#    pozisyon = f.tell()
#    print(pozisyon)
  
#with open('deneme2.txt') as f:
#    satir = f.readline()
#    print(satir, end='')
#    f.seek(34)
#    satir = f.readline()
#    print(satir, end='')

#with open('deneme2.txt') as f:
#    icerik= f.read(10)
#    print(icerik, end='')
#    icerik= f.read(10)
#    print(icerik, end='')
#    icerik= f.read(10)
#    print(icerik, end='')

#with open('deneme2.txt') as f:
#    okunacak_miktar = 1
#    icerik = f.read(okunacak_miktar)
#    while len(icerik) > 0:
#        print(icerik, end='')
#        icerik = f.read(okunacak_miktar)

#with open('deneme.txt', 'w') as f:
#     f.write('defol')
#
#with open('deneme2', 'a') as f:
#     f.write('bende iyi')

#with open('deneme3.txt', 'r') as okunacak:
#    with open('deneme3.txt', 'w') as yazilacak:
#        for satir in okunacak:
#            yazilacak.write(satir)

#with open('deneme4.txt', 'r') as okunacak:
#    with open('deneme4.txt', 'w') as yazilacak:
#        icerik = okunacak.readlines()
#        for satir in icerik:
#            yazilacak.write(satir)

                                                                # not : eğer metinsel verilerin haricinde birşey 
                                                                # okuyacak yada yazacaksak wb ve rb kullanılır..
                                                                # eğer metinsel verileri okuyacak yada yazacaksak
                                                                # o zaman r ve w kullanılır....




#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/05 - Curly Hair.mp3', 'rb') as okunacak:
#    with open('yeni müzik.mp3', 'wb') as yazilacak:
#        okunacak_miktar = 1024
#        icerik = okunacak.read(okunacak_miktar)
#        while len(icerik) > 0:
#            yazilacak.write(icerik)
#            icerik = okunacak.read(okunacak_miktar)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/05 - Curly Hair.mp3', 'rb') as okunacak:
#     with open('yeni müzik3.wavewr', 'wb') as yazilacak:
#          for i in okunacak:
#              yazilacak.write(i)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/NYC New York City June 2000.mp4', 'rb') as okunacak:
#     with open('yeni video.avi', 'wb') as yazilacak:
#          okunacak_miktar = 1024
#          icerik = okunacak.read(okunacak_miktar)
#          while len(icerik) > 0:
#               yazilacak.write(icerik)
#               icerik = okunacak.read(okunacak_miktar)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/NYC New York City June 2000.mp4', 'rb') as okunacak:
#     with open('yeni video2.xvid', 'wb') as yazilacak:
#          for i in okunacak:
#               yazilacak.write(i)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/kemalsunalfotograf.jpg', 'rb') as okunacak:
#     with open('yeni resim.png', 'wb') as yazilacak:
#          okunacak_miktar = 1024
#          icerik = okunacak.read(okunacak_miktar)
#          while len(icerik) > 0:
#               yazilacak.write(icerik)
#               icerik = okunacak.read(okunacak_miktar)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/kemalsunalfotograf.jpg', 'rb') as okunacak:
#     with open('yeni resim2.webp', 'wb') as yazilacak:
#          for i in okunacak:
#               yazilacak.write(i)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/ülkeler.txt', 'rb') as okunacak:
#     with open('yeni ülkeler.txt', 'wb') as yazilacak:
#          okunacak_miktar = 1
#          icerik = okunacak.read(okunacak_miktar)
#          while len(icerik) > 0:
#               yazilacak.write(icerik)
#               icerik = okunacak.read(okunacak_miktar)

#with open('C:/Users/5530/Desktop/nesne tabanlı programlama 6/takımlar.txt', 'rb') as okunacak:
#     with open('yeni takımlar.txt', 'wb') as yazilacak:
#          for i in okunacak:
#               yazilacak.write(i)
             
               



             









      










 
   
   
   
    
   




     
     


