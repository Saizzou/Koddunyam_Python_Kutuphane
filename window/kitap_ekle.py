from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(342, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")

        # Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 81, 18))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 18))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 81, 18))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 81, 18))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 81, 18))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")

        # Line Edit
        self.line_Kitap_Adi = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kitap_Adi.setGeometry(QtCore.QRect(110, 60, 211, 32))
        self.line_Kitap_Adi.setObjectName("line_Kitap_Adi")
        self.line_Sayfa_Sayisi = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Sayfa_Sayisi.setGeometry(QtCore.QRect(110, 100, 211, 32))
        self.line_Sayfa_Sayisi.setObjectName("line_Sayfa_Sayisi")
        self.line_Yazar_Adi = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Yazar_Adi.setGeometry(QtCore.QRect(110, 140, 211, 32))
        self.line_Yazar_Adi.setObjectName("line_Yazar_Adi")
        self.line_Raf = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Raf.setGeometry(QtCore.QRect(110, 220, 211, 32))
        self.line_Raf.setObjectName("line_Raf")

        # Combo Box
        self.combo_Kategori = QtWidgets.QComboBox(self.centralwidget)
        self.combo_Kategori.setGeometry(QtCore.QRect(110, 180, 211, 32))
        self.combo_Kategori.setObjectName("combo_Kategori")
        self.combo_Kategori.addItem("")
        self.combo_Kategori.addItem("")
        self.combo_Kategori.addItem("")
        self.combo_Kategori.addItem("")
        self.combo_Kategori.addItem("")

        # Butonlar
        self.btn_Iptal_Ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Iptal_Ekle.setGeometry(QtCore.QRect(220, 260, 101, 34))
        self.btn_Iptal_Ekle.setObjectName("btn_Iptal_Ekle")
        self.btn_Kitap_Ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Kitap_Ekle.setGeometry(QtCore.QRect(110, 260, 101, 34))
        self.btn_Kitap_Ekle.setObjectName("btn_Kitap_Ekle")


        MainWindow1.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Kitap Ekle"))
        self.label.setText(_translate("MainWindow1", "Kitap Adi :"))
        self.label_2.setText(_translate("MainWindow1", "Kitap Ekle"))
        self.label_3.setText(_translate("MainWindow1", "Sayfa Sayisi :"))
        self.label_4.setText(_translate("MainWindow1", "Yazar Adi :"))
        self.label_5.setText(_translate("MainWindow1", "Kategori :"))
        self.label_6.setText(_translate("MainWindow1", "Raf :"))
        self.combo_Kategori.setItemText(0, _translate("MainWindow1", "Roman"))
        self.combo_Kategori.setItemText(1, _translate("MainWindow1", "Siir Kitabi"))
        self.combo_Kategori.setItemText(2, _translate("MainWindow1", "Ders Kitabi"))
        self.combo_Kategori.setItemText(3, _translate("MainWindow1", "Tarihi Kitap"))
        self.combo_Kategori.setItemText(4, _translate("MainWindow1", "Parsomen"))
        self.btn_Iptal_Ekle.setText(_translate("MainWindow1", "IPTAL"))
        self.btn_Kitap_Ekle.setText(_translate("MainWindow1", "EKLE"))

