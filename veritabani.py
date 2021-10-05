""" SQLite3 Veritabani Islemlerini hizlandirmak icin hazirlanmis kütüphane örnegidir. Hazir Fonksiyonlar sayesinde
Arayüzler icerisinde bulunan islemler daha kolay gerceklestirilebilir.
"""

import sqlite3

veritabani = "test.db" # DataBase
baglan = sqlite3.connect(veritabani)
imlec = baglan.cursor()


def tablo_Olustur():
    """ SQLite3 Veritabani olusturan fonksiyondur. """

    try:
        imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                      KITAPADI TEXT NOT NULL,\
                      SAYFASAYISI INTEGER NOT NULL, \
                      YAZARADI TEXT, \
                      KATEGORI TEXT, \
                      RAF TEXT NOT NULL)")
        baglan.commit()
        print("[!] TABLO OLUSTURULDU!")
    except:
        print("[-] HATA!!! TABLO OLUSTUR Fonksiyonu TABLO OLUSTURAMADI!")


def tablo_Kitap_Ekle(kitap_adi:str, sayfa_sayisi:int, yazar_adi:str, kategori:str, raf:str):
    """ SQLite3 Veritabani Tablosuna Bilgi ekleyen fonksiyon. """

    imlec.execute(f"INSERT INTO kitaplar (KITAPADI, SAYFASAYISI, YAZARADI, KATEGORI, RAF) VALUES (?, ?, ?, ?, ?)", (kitap_adi, sayfa_sayisi, yazar_adi, kategori, raf,))
    baglan.commit()


def tablo_Kitap_Guncelle(id:int, kitap_adi:str, sayfa_sayisi:int, yazar_adi:str, kategori:str, raf:str):
    """ SQLite3 Veritabani Tablosunda bulunan bilgiyi düzenleyen fonksiyon. """

    imlec.execute(f"UPDATE kitaplar SET KITAPADI = '{kitap_adi}', SAYFASAYISI = {sayfa_sayisi}, YAZARADI = '{yazar_adi}', KATEGORI = '{kategori}', RAF = '{raf}' WHERE ID = {id}")
    baglan.commit()


def tablo_Bilgileri_Oku():
    """ SQLite3 Veritabani icerisindeki bilgileri okur! """

    bilgiler = imlec.execute("SELECT KITAPADI, SAYFASAYISI, YAZARADI, KATEGORI, RAF from kitaplar")
    for satir in bilgiler:
        kitapadi = satir[0]
        SayfaSayisi = satir[1]
        YazarAdi = satir[2]
        Kategori = satir[3]
        Raf = satir[4]


def tablo_Bilgileri_Sil(id:int):
    """ SQLite3 Veritabani icerisindeki bilgileri siler!"""

    imlec.execute(f"DELETE FROM kitaplar where ID={id}")
    baglan.commit()

def tablo_Sil(tablo_adi):
    """ SQLite3 Veritabanindaki Tabloyu siler! """

    imlec.execute(f"DROP TABLE IF EXISTS {tablo_adi}")
    baglan.commit()

def tablo_icinde_Ara(kitap_Adi):
    """ SQLite3 Veritabani icerisinde belirli Kitap Adini arayan fonksiyon. """

    islem = imlec.execute(f"SELECT ID, KITAPADI, SAYFASAYISI, YAZARADI, KATEGORI, RAF from kitaplar where KITAPADI = '{kitap_Adi}'")
    return islem


def tablo_icerik_duzenle(id:int):
    """ SQLite3 Veritabani icerisinde belirli icerikleri düzenlemek icin kullanilan SQL Komutu. """

    icerik = imlec.execute(f"SELECT KITAPADI,SAYFASAYISI,YAZARADI,KATEGORI,RAF from kitaplar where ID= {id}")
    return icerik


def tablo_icerikleri_dondur():
    """ SQLite3 icerisindeki tüm iceriklerin ciktisini veren fonksiyon. """

    icerik = imlec.execute("SELECT ID,KITAPADI,SAYFASAYISI,YAZARADI,KATEGORI,RAF from kitaplar")
    return icerik


def secure_params(currenparam):
    return currenparam.replace("\"","").replace("'","")
