from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(344, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")

        # Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 81, 18))
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 81, 18))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 81, 18))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 81, 18))
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 18))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        # Line Edit
        self.line_Kitap_adi = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kitap_adi.setGeometry(QtCore.QRect(110, 60, 211, 32))
        self.line_Kitap_adi.setObjectName("line_Kitap_adi")
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
        self.btn_Iptal_Duzenle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Iptal_Duzenle.setGeometry(QtCore.QRect(220, 260, 101, 34))
        self.btn_Iptal_Duzenle.setObjectName("btn_Iptal_Duzenle")
        self.btn_Duzenle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Duzenle.setGeometry(QtCore.QRect(110, 260, 101, 34))
        self.btn_Duzenle.setObjectName("btn_Duzenle")



        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "Kitap Düzenle"))
        self.combo_Kategori.setItemText(0, _translate("MainWindow", "Roman"))
        self.combo_Kategori.setItemText(1, _translate("MainWindow", "Siir Kitabi"))
        self.combo_Kategori.setItemText(2, _translate("MainWindow", "Ders Kitabi"))
        self.combo_Kategori.setItemText(3, _translate("MainWindow", "Tarihi Kitap"))
        self.combo_Kategori.setItemText(4, _translate("MainWindow", "Parsomen"))
        self.label_2.setText(_translate("MainWindow", "Kitap Düzenle"))
        self.btn_Iptal_Duzenle.setText(_translate("MainWindow", "IPTAL"))
        self.label_6.setText(_translate("MainWindow", "Raf :"))
        self.label.setText(_translate("MainWindow", "Kitap Adi :"))
        self.btn_Duzenle.setText(_translate("MainWindow", "DUZENLE"))
        self.label_4.setText(_translate("MainWindow", "Yazar Adi :"))
        self.label_5.setText(_translate("MainWindow", "Kategori :"))
        self.label_3.setText(_translate("MainWindow", "Sayfa Sayisi :"))

