from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Line Edit
        self.line_Ara = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Ara.setGeometry(QtCore.QRect(120, 60, 113, 32))
        self.line_Ara.setObjectName("line_Ara")

        # Labeller
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 71, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Tablo
        self.table_Icerik = QtWidgets.QTableWidget(self.centralwidget)
        self.table_Icerik.setGeometry(QtCore.QRect(10, 110, 781, 481))
        self.table_Icerik.setObjectName("table_Icerik")
        self.table_Icerik.setColumnCount(6)
        self.table_Icerik.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Icerik.setHorizontalHeaderItem(5, item)

        # Butonlar
        self.btn_Form_Ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Form_Ekle.setGeometry(QtCore.QRect(350, 60, 101, 34))
        self.btn_Form_Ekle.setObjectName("btn_Form_Ekle")
        self.btn_Kitap_Sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Kitap_Sil.setGeometry(QtCore.QRect(570, 60, 101, 34))
        self.btn_Kitap_Sil.setObjectName("btn_Kitap_Sil")
        self.btn_Form_Duzenle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Form_Duzenle.setGeometry(QtCore.QRect(460, 60, 101, 34))
        self.btn_Form_Duzenle.setObjectName("btn_Form_Duzenle")
        self.btn_Cikis_Main = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cikis_Main.setGeometry(QtCore.QRect(680, 60, 101, 34))
        self.btn_Cikis_Main.setObjectName("btn_Cikis_Main")
        self.btn_Ara = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ara.setGeometry(QtCore.QRect(240, 60, 101, 34))
        self.btn_Ara.setObjectName("btn_Ara")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Koddunyam Kütüphanesi"))
        self.label.setText(_translate("MainWindow", "Kitap Ara:"))
        self.label_2.setText(_translate("MainWindow", "Koddunyam Kütüphanesi"))
        item = self.table_Icerik.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_Icerik.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "KitapAdi"))
        item = self.table_Icerik.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SayfaSayisi"))
        item = self.table_Icerik.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "YazarAdi"))
        item = self.table_Icerik.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kategori"))
        item = self.table_Icerik.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Raf"))
        self.btn_Form_Ekle.setText(_translate("MainWindow", "Kitap Ekle"))
        self.btn_Kitap_Sil.setText(_translate("MainWindow", "Kitap Sil"))
        self.btn_Form_Duzenle.setText(_translate("MainWindow", "Kitap Düzenle"))
        self.btn_Cikis_Main.setText(_translate("MainWindow", "Cikis"))
        self.btn_Ara.setText(_translate("MainWindow", "Kitap Ara"))

