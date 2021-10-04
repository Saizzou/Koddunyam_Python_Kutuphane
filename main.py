# Import
from window.arayuz import *
from window.kitap_ekle import *
from window.kitap_duzenle import *
import veritabani
import sys


# Giris Ekrani
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Kitap Ekle
MainWindow1 = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow1()
ui1.setupUi(MainWindow1)

# Kitap Düzenle
MainWindow2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow2()
ui2.setupUi(MainWindow2)

def tablo_guncelle():
    """ Veritabani icerisindeki bilgileri PyQT Tablosuna aktaran fonksiyon. """

    ui.table_Icerik.clear()
    ui.table_Icerik.setHorizontalHeaderLabels(('ID','KitapAdi','SayfaSayisi','YazarAdi','Kategori','Raf'))
    icerik = veritabani.tablo_icerikleri_dondur()

    for satir, satir_veri in enumerate(icerik):
        for sutun, sutun_veri in enumerate(satir_veri):
            ui.table_Icerik.setItem(satir, sutun, QtWidgets.QTableWidgetItem(str(sutun_veri)))
    print("[+] Veriler güncellendi ve Tablo icerisine yazdirildi.")


def kitap_Ara():
    """ Veritabani icerisinde olan kitabi arar. """

    kitap_Adi = ui.line_Ara.text()
    if kitap_Adi == "":
        tablo_guncelle()
    else:
        ui.table_Icerik.clear()
        ui.table_Icerik.setHorizontalHeaderLabels(('ID', 'KitapAdi', 'SayfaSayisi', 'YazarAdi', 'Kategori', 'Raf'))
        arama = veritabani.tablo_icinde_Ara(kitap_Adi)

        for satir, satir_veri in enumerate(arama):
            for sutun, sutun_veri in enumerate(satir_veri):
                ui.table_Icerik.setItem(satir, sutun, QtWidgets.QTableWidgetItem(str(sutun_veri)))

def kitap_Ekle_Arayuz():
    """ Kitap Ekle Arayüzünün acilmasini saglayan fonksiyon. """

    MainWindow1.show()


def kitap_Ekle():
    """ Veritabani icerisine yeni Kitap bilgisi ekleyen fonksiyon. """

    kitap_adi = ui1.line_Kitap_Adi.text()
    sayfa_sayisi = ui1.line_Sayfa_Sayisi.text()
    yazar_adi = ui1.line_Yazar_Adi.text()
    kategori = ui1.combo_Kategori.currentText()
    raf = ui1.line_Raf.text()
    veritabani.tablo_Kitap_Ekle(kitap_adi, sayfa_sayisi, yazar_adi, kategori, raf)
    print("Kitap Ekleme Basarili!")
    tablo_guncelle()


def kitap_Duzenle_Arayuz():
    """ Kitap Düzenle Arayüzüne tablo icerisinden bilgileri gönderen fonksiyon. """

    try:
        MainWindow2.show()
        index = ui.table_Icerik.currentIndex()
        veri = ui.table_Icerik.model().index(index.row(), 0)
        id = ui.table_Icerik.model().data(veri)
        imlec = veritabani.tablo_icerik_duzenle(id)
        for icerik in imlec:
            kitap_Adi = icerik[0]
            sayfa_Sayisi = icerik[1]
            yazar_Adi = icerik[2]
            kategori = icerik[3]
            raf = icerik[4]
        ui2.line_Kitap_adi.setText(kitap_Adi)
        ui2.line_Sayfa_Sayisi.setText(str(sayfa_Sayisi))
        ui2.line_Yazar_Adi.setText(yazar_Adi)
        ui2.line_Raf.setText(raf)
        ui2.combo_Kategori.findText(kategori)
    except:
        soru = QtWidgets.QMessageBox.question(MainWindow, "HATA!",
                                              "Lütfen Tablo icerisinden bir kitap seciniz!", \
                                              QtWidgets.QMessageBox.Ok)
        if soru == QtWidgets.QMessageBox.Ok:
            MainWindow.show()
            MainWindow2.close()


def kitap_Duzenle():
    """ Veritabani icerisinden Tabloda secili olan Kitap Bilgisini düzenleyen fonksiyon. """

    index = ui.table_Icerik.currentIndex()
    veri = ui.table_Icerik.model().index(index.row(), 0)
    id = ui.table_Icerik.model().data(veri)
    kitap_Adi = ui2.line_Kitap_adi.text()
    sayfa_Sayisi = int(ui2.line_Sayfa_Sayisi.text())
    yazar_Adi = ui2.line_Yazar_Adi.text()
    raf = ui2.line_Raf.text()
    kategori = ui2.combo_Kategori.currentText()
    veritabani.tablo_Kitap_Guncelle(id, kitap_Adi, sayfa_Sayisi, yazar_Adi, kategori, raf)
    tablo_guncelle()
    MainWindow2.close()



def kitap_Sil():
    """ Veritabani icerisinden Tabloda secili olan Kitap Bilgisini silen fonksiyon. """

    index = ui.table_Icerik.currentIndex()
    veri = ui.table_Icerik.model().index(index.row(), 0)
    id = ui.table_Icerik.model().data(veri)
    veritabani.tablo_Bilgileri_Sil(id)
    tablo_guncelle()



def cikis():
    """ Cikis yapilsin mi sorgusunu yapan fonksiyon. """

    soru = QtWidgets.QMessageBox.question(MainWindow, "Emin misiniz?", "Programdan cikmak istediginize emin misiniz?", \
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if soru == QtWidgets.QMessageBox.Yes:
        sys.exit(app.exec_())
    else:
        MainWindow.show()


def iptal_Duzenle():
    """ Kitap Düzenle Arayüzünü kapatan fonksiyon. """

    MainWindow2.close()


def iptal_Ekle():
    """ Kitap Ekle Arayüzünü kapatan fonksiyon. """

    MainWindow1.close()

# Arayuz Objeleri Baglama
# Temel Arayuz
ui.btn_Form_Duzenle.clicked.connect(kitap_Duzenle_Arayuz)
ui.btn_Ara.clicked.connect(kitap_Ara)
ui.line_Ara.returnPressed.connect(kitap_Ara)
ui.btn_Form_Ekle.clicked.connect(kitap_Ekle_Arayuz)
ui.btn_Cikis_Main.clicked.connect(cikis)
ui.btn_Kitap_Sil.clicked.connect(kitap_Sil)

# Kitap Düzenle
ui2.btn_Iptal_Duzenle.clicked.connect(iptal_Duzenle)
ui2.btn_Duzenle.clicked.connect(kitap_Duzenle)

# Kitap Ekle
ui1.btn_Kitap_Ekle.clicked.connect(kitap_Ekle)
ui1.btn_Iptal_Ekle.clicked.connect(iptal_Ekle)

# Start
veritabani.tablo_Olustur()
MainWindow.show()
tablo_guncelle()
sys.exit(app.exec_())
