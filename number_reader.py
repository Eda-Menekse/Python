print("Sayı Okuma programına hoşgeldiniz... Programı bitirmek için çıkış yazın.")

def sayi_okuyucu(sayi):
    while True:
        sayi = input("Sayı giriniz: ")
        basamak = len(sayi) - 1

        sayilar = [["Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", ""],
                   ["On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan", ""],
                   ["Yüz", "İki Yüz", "Üç Yüz", "Dört Yüz", "Beş Yüz", "Altı Yüz", "Yedi Yüz", "Sekiz Yüz", "Dokuz Yüz",
                    ""],
                   ["Bin", "İki Bin", "Üç Bin", "Dört Bin", "Beş Bin", "Altı Bin", "Yedi Bin", "Sekiz Bin", "Dokuz Bin",
                    ""]]

        okunus = ""

        if sayi == "çıkış":
            print("Program Bitti...")
            break

        for i in sayi:
            okunus += sayilar[basamak][int(i) - 1] + " "
            basamak -= 1

        print("Girdiğiniz sayının okunuşu:", okunus)

sayi = input("Programı başlatmak için enter tuşuna basınız")
sayi_okuyucu(sayi)

x = input("----------------")