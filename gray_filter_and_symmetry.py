import numpy
from PIL import Image

gecerliinput = False


def siyah_beyaz_yapma(npImage):
    yeni = numpy.zeros((resimboyutu))

    for i in range(0, resimboyutu[0]):
        for j in range(0, resimboyutu[1]):
            x = npImage[i][j][0] * 0.2989
            y = npImage[i][j][1] * 0.5870
            z = npImage[i][j][2] * 0.1140
            a = x + y + z
            yeni[i, j] = a
    sbimage = Image.fromarray(yeni)
    sbimage.show()


def ters_cevirme(npImage):
    yeni_liste = numpy.zeros((npImage.shape))
    for i in range(0, resimboyutu[0]):
        for j in range(0, resimboyutu[1]):
            yeni_liste[resimboyutu[0] - i - 1, resimboyutu[1] - j - 1, 0] = npImage[i, j, 0]
            yeni_liste[resimboyutu[0] - i - 1, resimboyutu[1] - j - 1, 1] = npImage[i, j, 1]
            yeni_liste[resimboyutu[0] - i - 1, resimboyutu[1] - j - 1, 2] = npImage[i, j, 2]
    yeni_liste = yeni_liste.astype(numpy.uint8)
    tersimage = Image.fromarray(yeni_liste)
    tersimage.show()


while True:
    secim = input("1- Resim yükleme\n2- Resmi siyah ve beyaz hale çevirme\n3- Resmi yatay olarak döndürme\nSeçimizi yapınız >>> ")

    if secim == "1":
        resiminputu = input("Fotoğrafınızın tam adını giriniz. >>> ")
        image = Image.open(resiminputu)
        npImage = numpy.array(image)
        resimboyutu = image.size[::-1]
        print("{} resminiz yüklendi".format(resiminputu))
        gecerliinput = True

    elif secim == "2" and gecerliinput:
        print("\nLütfen bekleyiniz, resminiz siyah beyaz hale getiriliyor...")
        siyah_beyaz_yapma(npImage)

    elif secim == "3" and gecerliinput:
        print("\nLütfen bekleyiniz, resminiz ters döndürülüyor...")
        ters_cevirme(npImage)

    else:
        print("\nLütfen bir resim yükleyiniz.")




bitti = input("<<< PROGRAM BİTTİ >>>")