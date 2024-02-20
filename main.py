
s_box2 = {"giris": ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
         "cikis": ['C','5','6','B','9','0','A','D','3','E','F','8','4','7','1','2']}

import random

rastgele_sayilar = [random.randint(0, 15) for _ in range(32)]

print(rastgele_sayilar)
print("=============================")
s_box = {"giris": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
         "cikis": [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]}


s_box_ciktilar = [s_box["cikis"][s_box["giris"].index(sayi)] for sayi in rastgele_sayilar] # s_box geir
s_box_ciktilar_binary = [bin(sayi)[2:].zfill(4) for sayi in s_box_ciktilar] # 4 bit çevir

# Sonuçları yazdır
print("Giriş:", rastgele_sayilar)
print("Çıkış:", s_box_ciktilar)
print("4 bit sonuçlar:", s_box_ciktilar_binary)


s_box_ciktilar_binary = [bin(sayi)[2:].zfill(4) for sayi in s_box_ciktilar]

str_128bit = ""


for i in s_box_ciktilar_binary:
    str_128bit += i

print("128 bit: ", str_128bit)
print("uzunluk: ", len(str_128bit))

str_ilk64 = ""
str_son64 = ""

str_ilk64 = str_128bit[:64]
str_son64 = str_128bit[64:]

print("İlk 64 bit:", str_ilk64)
print("son 64 bit:", str_son64)


def tabaka(veri):
    yeni_str = ""
    diffused_bit = 0

    for i in range(len(veri)):
        if i== 63:
            diffused_bit = veri[63]
        else:
            diffused_bit = veri[(16*i)%63]

        yeni_str += str(diffused_bit)

    return yeni_str

difizyon1 = tabaka(str_ilk64)
difizyon2 = tabaka(str_son64)

print("difizyon ilk 64 bit sonucu: ", difizyon1)
print("difizyon son 64 bit sonucu: ", difizyon2)

difizyondan_cikan_128 = difizyon1+difizyon2

print("difizyon sonucu: ", difizyondan_cikan_128)

liste = list(difizyondan_cikan_128)
degisken = liste.copy()

def xorlama(ilk, son):
    return ilk ^ son


for i in range(len(difizyondan_cikan_128)):
    if i == 0:
        continue

    if difizyondan_cikan_128[i - 1] == '0':
        ilk = 0
    else:
        ilk = 1
    if difizyondan_cikan_128[i] == '0':
        son = 0
    else:
        son = 1

    cikanbit = xorlama(ilk, son)
    degisken[i] = str(cikanbit)

xor_sonucu_128 = ""

for i in degisken:
    xor_sonucu_128 += i

print("XOR sonucu olusan 128 bit: ", xor_sonucu_128)


def hexcevir(veri):
    temp = hex(int(veri, 2))[2:]
    return temp.zfill(len(veri)//4)

en_son_hex = hexcevir(xor_sonucu_128)
print("en son hex:", en_son_hex)
















