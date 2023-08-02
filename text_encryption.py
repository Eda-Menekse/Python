print("METİN ŞİFRELEME PROGRAMINA HOŞGELDİNİZ...")

def metin_sifreleme(metin, n):
    sifrelenmis_metin = ''

    latin_alfabesi = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in metin:

        if i not in latin_alfabesi:
            sifrelenmis_metin += i
        else:
            sifrelenmis_metin += latin_alfabesi[(latin_alfabesi.index(i) + n) % len(latin_alfabesi)]

    print("Şifrelenmiş metin:", sifrelenmis_metin)


n = int(input("Şifreleme için kaç harf yana kaydırsın? Lütfen tamsayı giriniz."))
metin = input("Şifrelemek istediğiniz metni giriniz. Lütfen küçük harf kullanınız.")

metin_sifreleme(metin, n)


def sifre_coz(sifre_cozulecek_metin, n):
    sifre_cozuldu = ''
    latin_alfabesi = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in sifre_cozulecek_metin:

        if i not in latin_alfabesi:
            sifre_cozuldu += i
        else:
            sifre_cozuldu += latin_alfabesi[(latin_alfabesi.index(i) - n) % len(latin_alfabesi)]
    print("Şifreniz çözüldü:", sifre_cozuldu)


sifre_cozulecek_metin = input("Kontrol için şifrelenmiş metni giriniz:")

sifre_coz(sifre_cozulecek_metin, n)
x = input("Program Bitti...")