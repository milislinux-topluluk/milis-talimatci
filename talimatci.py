#!/usr/bin/python3
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout, QFormLayout, QLineEdit, QLabel, QComboBox, QCheckBox,
                             QVBoxLayout, QTextEdit, QPushButton,QFileDialog,QMessageBox,QListWidget, QDialog, QAction, QTabWidget)
from PyQt5.QtCore import QDir,QUrl, Qt
import sys,os


class TalimatciPencere(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(TalimatciPencere,self).__init__(ebeveyn)
        merkez_widget = QWidget()
        self.setCentralWidget(merkez_widget)
        merkez_kutu = QVBoxLayout()
        merkez_widget.setLayout(merkez_kutu)

        #######################################
        #         Gerek değişkenleri          #
        #######################################
        self.secilen_gerekler_liste = []
        self.var_olan_gerekler_liste = []

        ac_kutu = QHBoxLayout()
        merkez_kutu.addLayout(ac_kutu)
        self.ac_dugme = QPushButton("Aç")
        self.ac_dugme.clicked.connect(self.ac_func)
        ac_kutu.addWidget(self.ac_dugme)
        self.acilan_url = QLineEdit()
        self.acilan_url.setReadOnly(True)
        ac_kutu.addWidget(self.acilan_url)

        ac_kutu = QHBoxLayout()
        merkez_kutu.addLayout(ac_kutu)
        self.talimatname_dugme = QPushButton("Talimatname")
        self.talimatname_dugme.clicked.connect(self.talimatname_ac_func)
        ac_kutu.addWidget(self.talimatname_dugme)
        self.talimatname = QLineEdit()
        self.talimatname.setReadOnly(True)
        ac_kutu.addWidget(self.talimatname)

        form_kutu = QHBoxLayout()
        merkez_kutu.addLayout(form_kutu)
        self.program_ad = QLineEdit()
        form_ad_label = QLabel("Ad")
        form_ad_label.setFixedWidth(45)
        form_kutu.addWidget(form_ad_label)
        form_kutu.addWidget(self.program_ad)
        self.program_surum = QLineEdit()
        form_surum = QLabel("Sürüm")
        form_surum.setFixedWidth(40)
        form_kutu.addWidget(form_surum)
        form_kutu.addWidget(self.program_surum)
        self.program_devir = QLineEdit()
        form_devir = QLabel("Devir")
        form_devir.setFixedWidth(40)
        form_kutu.addWidget(form_devir)
        form_kutu.addWidget(self.program_devir)

        form_kutu = QHBoxLayout()
        merkez_kutu.addLayout(form_kutu)
        self.program_url = QLineEdit()
        form_url = QLabel("Url")
        form_url.setFixedWidth(45)
        form_kutu.addWidget(form_url)
        form_kutu.addWidget(self.program_url)
        form_paketci = QLabel("Paketçi")
        form_paketci.setFixedWidth(45)
        form_kutu.addWidget(form_paketci)
        self.program_paketci = QLineEdit()
        form_kutu.addWidget(self.program_paketci)

        form_kutu = QHBoxLayout()
        merkez_kutu.addLayout(form_kutu)
        self.program_tanim = QLineEdit()
        form_tanim = QLabel("Tanım")
        form_tanim.setFixedWidth(45)
        form_kutu.addWidget(form_tanim)
        form_kutu.addWidget(self.program_tanim)

        form_kutu = QHBoxLayout()
        merkez_kutu.addLayout(form_kutu)
        self.program_kaynak = QTextEdit()
        form_source = QLabel("Kaynak")
        form_source.setFixedWidth(45)
        form_kutu.addWidget(form_source)
        form_kutu.addWidget(self.program_kaynak)

        grub_kutu = QHBoxLayout()
        merkez_kutu.addLayout(grub_kutu)
        grub_label = QLabel("Grup")
        grub_label.setFixedWidth(40)
        grub_kutu.addWidget(grub_label)
        self.gruplar_combo = QComboBox()
        self.varolan_grup_list = self.gruplar_al()
        self.secilen_grub_liste = []
        self.gruplar_combo.addItems(self.varolan_grup_list)
        grub_kutu.addWidget(self.gruplar_combo)
        self.saga_grup_dugme = QPushButton(">")
        self.saga_grup_dugme.setFixedWidth(40)
        self.saga_grup_dugme.clicked.connect(self.saga_grup_fonk)
        grub_kutu.addWidget(self.saga_grup_dugme)
        self.sola_grup_dugme = QPushButton("<")
        self.sola_grup_dugme.setFixedWidth(40)
        self.sola_grup_dugme.clicked.connect(self.sola_grup_fonk)
        grub_kutu.addWidget(self.sola_grup_dugme)
        self.program_grup = QComboBox()
        grub_kutu.addWidget(self.program_grup)
        self.grup_ekle = QPushButton("+")
        self.grup_ekle.setFixedWidth(40)
        self.grup_ekle.clicked.connect(self.grup_ekle_fonk)
        grub_kutu.addWidget(self.grup_ekle)


        merkez_kutu.addWidget(QLabel("Talimatlar"))
        gerek_kutu = QHBoxLayout()
        merkez_kutu.addLayout(gerek_kutu)
        self.var_olan_gerekler = QListWidget()
        self.var_olan_gerekler.setContextMenuPolicy(Qt.ActionsContextMenu)
        gerek_talimat_ac_aksiyon = QAction("Talimatı Aç",self,triggered=self.talimat_ac)
        self.var_olan_gerekler.addAction(gerek_talimat_ac_aksiyon)
        gerek_kutu.addWidget(self.var_olan_gerekler)
        dugme_kutu = QVBoxLayout()
        gerek_kutu.addLayout(dugme_kutu)
        self.saga_dugme = QPushButton("Gerek Ekle")
        self.saga_dugme.clicked.connect(self.saga_dugme_fonk)
        dugme_kutu.addWidget(self.saga_dugme)
        self.sola_dugme = QPushButton("Gerek sil")
        self.sola_dugme.clicked.connect(self.sola_dugme_fonk)
        dugme_kutu.addWidget(self.sola_dugme)
        sag_dugme_kutu = QVBoxLayout()
        gerek_kutu.addLayout(sag_dugme_kutu)
        self.secilen_gerekler = QListWidget()
        sag_dugme_kutu.addWidget(self.secilen_gerekler)
        self.gerek_ekle_dugme = QPushButton("Yeni Gerek Ekle")
        self.gerek_ekle_dugme.clicked.connect(self.gerek_ekle)
        sag_dugme_kutu.addWidget(self.gerek_ekle_dugme)

        merkez_kutu.addWidget(QLabel("Derle"))
        self.program_build = QTextEdit()
        merkez_kutu.addWidget(self.program_build)

        kayit_kutu = QHBoxLayout()
        merkez_kutu.addLayout(kayit_kutu)
        self.farkli_kaydet_dugme = QPushButton("Farklı Kaydet")
        self.farkli_kaydet_dugme.clicked.connect(self.farkli_yaz)
        kayit_kutu.addWidget(self.farkli_kaydet_dugme)
        self.kaydet_dugme = QPushButton("Kaydet")
        self.kaydet_dugme.clicked.connect(self.yaz)
        kayit_kutu.addWidget(self.kaydet_dugme)
        self.talimat_indir_dugme = QPushButton("Talimat İndir")
        self.talimat_indir_dugme.clicked.connect(self.talimat_indir_fonk)
        kayit_kutu.addWidget(self.talimat_indir_dugme)

        kayit_kutu = QHBoxLayout()
        merkez_kutu.addLayout(kayit_kutu)
        self.derle_dugme = QPushButton("Derle")
        self.derle_dugme.clicked.connect(self.derle_fonk)
        kayit_kutu.addWidget(self.derle_dugme)
        self.url_kontrol_dugme = QPushButton("Url Kontrol")
        self.url_kontrol_dugme.clicked.connect(self.url_kontrol_fonk)
        kayit_kutu.addWidget(self.url_kontrol_dugme)
        self.gerek_kontrol_dugme = QPushButton("Gerek Kontrol")
        self.gerek_kontrol_dugme.clicked.connect(self.gerek_kontrol_fonk)
        kayit_kutu.addWidget(self.gerek_kontrol_dugme)

    def gruplar_al(self):
        fname="gruplar"
        with open(fname) as f:
            icerik = f.readlines()
        icerik = [x.strip() for x in icerik] 
        return icerik
    
    def talimat_indir_fonk(self):
        self.talimat_indir_pencere = TalimatindirSinif(self)
        self.talimat_indir_pencere.show()

    def gerek_kontrol_fonk(self):
        pass

    def url_kontrol_fonk(self):
        pass

    def derle_fonk(self):
        pass


    def talimat_ac(self):
        secilen = self.var_olan_gerekler.currentItem().text()
        url = self.talimatname.text() + os.sep + secilen[0] + os.sep + secilen + os.sep + "talimat"
        self.acilan_url.setText(url)
        self.oku(url)

    def grup_ekle_fonk(self):
        grup_ekle_pencere = GrupEkle(self)
        grup_ekle_pencere.show()

    def sola_grup_fonk(self):
        secilen = self.program_grup.currentText()
        if secilen != "":
            self.secilen_grub_liste.remove(secilen)
            self.program_grup.clear()
            self.program_grup.addItems(self.secilen_grub_liste)

    def saga_grup_fonk(self):
        secilen = self.gruplar_combo.currentText()
        if secilen != "":
            if secilen not in self.secilen_grub_liste:
                self.secilen_grub_liste.append(secilen)
                self.program_grup.clear()
                self.program_grup.addItems(self.secilen_grub_liste[::-1])

    def saga_dugme_fonk(self):
        secilen = self.var_olan_gerekler.currentItem()
        if secilen != None:
            secilen = secilen.text()
            self.gerek_ekle_fonk(secilen)

    def sola_dugme_fonk(self):
        secilen = self.secilen_gerekler.currentItem()
        if secilen != None:
            secilen = secilen.text()
            self.secilen_gerekler_liste.remove(secilen)
            self.secilen_gerekler.clear()
            self.secilen_gerekler.addItems(self.secilen_gerekler_liste)

    def gerek_ekle(self):
        gerek_pencere = GerekEkle(self)
        gerek_pencere.show()

    def ac_func(self):
        dosya = QFileDialog.getOpenFileName(self, self.tr("Talimat Dosyası Aç"), "","")
        if dosya:
            if dosya != ("",""):
                if os.path.split(dosya[0])[1] == "talimat":
                    self.acilan_url.setText(dosya[0])
                    self.oku(dosya[0])
                else:
                    QMessageBox.warning(self,"Hata","Lütfen Bir Talimat Dosyası Seçiniz")

    def talimatname_ac_func(self):
        dizin = QFileDialog.getExistingDirectory(self, self.tr("Talimatname Dizini"), "/root/talimatname/genel", QFileDialog.ShowDirsOnly)
        if dizin:
            if dizin != ("",""):
                self.talimatname.setText(dizin)
                self.gerek_doldur_fonk(dizin)
            else:
                QMessageBox.warning(self,"Hata","Lütfen Bir Gerec Urlsi Seçiniz")

    def yaz(self):
        if os.path.exists(self.acilan_url.text()):
            f = open(self.acilan_url.text(),"w")
            f.write(self.yazilacak_hazirla())
            f.close()
            QMessageBox.information(self,"Kaydedildi","Kayıt işlemi başarıyla gerçekleştirildi")

    def farkli_yaz(self):
        kaydet = QFileDialog.getSaveFileUrl(self, self.tr("Talimat Dosyası Kaydet"), "","")
        if kaydet:
            if kaydet != (QUrl(''), ''):
                url = kaydet[0].toString()[7:]
                f = open(url,"w")
                f.write(self.yazilacak_hazirla())
                f.close()
                QMessageBox.information(self, "Kaydedildi", "Kayıt işlemi başarıyla gerçekleştirildi")

    def yazilacak_hazirla(self):
        yazilacak = ""
        yazilacak += "# Tanım: " + self.program_tanim.text() + "\n"
        yazilacak += "# URL: " + self.program_url.text() + "\n"
        yazilacak += "# Paketçi: " + self.program_paketci.text() + "\n"
        yazilacak += "# Gerekler: " + " ".join(self.secilen_gerekler_liste)+ "\n"
        yazilacak += "# Grup: " + " ".join(self.secilen_grub_liste) + "\n\n"
        yazilacak += "isim=" + self.program_ad.text() + "\n"
        yazilacak += "surum=" + self.program_surum.text() + "\n"
        yazilacak += "devir=" + self.program_devir.text() + "\n"
        yazilacak += "kaynak=(" + self.program_kaynak.toPlainText().replace("\n","\n        ") + ")\n\n"
        yazilacak += self.program_build.toPlainText()
        return yazilacak

    def temizle(self):
        self.secilen_gerekler.clear()
        self.program_grup.clear()
        self.secilen_gerekler_liste = []
        self.secilen_grub_liste = []


    def oku(self,url):
        if os.path.exists(url):
            self.temizle()
            f = open(url,"r")
            okunan = f.readlines()
            f.close()
            build = ""
            self.acilan_sozluk = {}
            kaynak_durum = False
            kaynak_tum = []
            for i in okunan:
                if i[:5] == "isim=":
                    isim = i[5:-1].replace(" ","")
                    self.program_ad.setText(isim)
                    self.acilan_sozluk["isim"] = isim
                elif i[:6] == "surum=":
                    surum = i[6:-1].replace(" ", "")
                    self.program_surum.setText(surum)
                    self.acilan_sozluk["surum"] = surum
                elif i[:6] == "devir=":
                    devir= i[6:-1].replace(" ", "")
                    self.program_devir.setText(devir)
                    self.acilan_sozluk["devir"] = devir
                elif i[:8] == "kaynak=(":
                    if i[-2] == ")":
                        kaynak = i[8:-2].replace(" ", "").replace("\t","").replace("\n","")
                        self.program_kaynak.setText(kaynak)
                        self.acilan_sozluk["kaynak"] = kaynak
                    else:
                        kaynak = i[8:].replace(" ", "").replace("\t","").replace("\n","")
                        kaynak_tum.append(kaynak)
                        kaynak_durum = True
                elif i[:8] == "# Tanım:":
                    if i[9] == " ":
                        tanim = i[9:-1]
                    else:
                        tanim = i[8:-1]
                    self.program_tanim.setText(tanim)
                    self.acilan_sozluk["tanım"] = tanim
                elif i[:6] == "# URL:":
                    url_ = i[6:-1].replace(" ", "")
                    self.program_url.setText(url_)
                    self.acilan_sozluk["url"] = url_
                elif i[:10] == "# Paketçi:":
                    paketci = i[10:-1].replace(" ", "")
                    self.program_paketci.setText(paketci)
                    self.acilan_sozluk["paketci"] = paketci
                elif i[:7] == "# Grup:":
                    if i[7:-1] != "\n" and i[7:-1] != " " and i[7:-1] != "":
                        for x in i[7:-1].split(" "):
                            if x != "" and x != " ":
                                self.secilen_grub_liste.append(x)
                    self.program_grup.addItems(self.secilen_grub_liste)
                    self.acilan_sozluk["grup"] = " ".join(self.secilen_grub_liste)
                elif i[:11] == "# Gerekler:":
                    if i[11:-1] != "\n" and i[11:-1] != " " and i[11:-1] != "":
                        for x in i[11:-1].split(" "):
                            if x != "" and x != " ":
                                self.gerek_ekle_fonk(x)
                elif kaynak_durum:
                    kaynak = i.replace(" ", "").replace("\t","")
                    if i[-2] == ")":
                        kaynak = kaynak.replace("\n","")[:-1]
                        kaynak_tum.append(kaynak)
                        kaynak_durum = False
                        self.program_kaynak.setText("\n".join(kaynak_tum))
                        self.acilan_sozluk["kaynak"] = " ".join(kaynak_tum)
                    else:
                        kaynak_tum.append(kaynak[:-1])
                else:
                    if i != "\n":
                        build += i
            self.acilan_sozluk["build"] = build
            self.program_build.setText(build)

    def gerek_ekle_fonk(self,gerek):
        if gerek not in self.secilen_gerekler_liste:
            self.secilen_gerekler.addItem(gerek)
            self.secilen_gerekler_liste.append(gerek)

    def gerek_doldur_fonk(self,dizin):
        if not os.path.exists(dizin):
            QMessageBox.warning(self,"Hata","Sisteminizdeki paketler okunamadı. Milis kullanmıyor olabilirsiniz.")
        elif dizin[-17:] != 'talimatname/genel' and dizin[-18:] != 'talimatname/genel/':
            QMessageBox.warning(self, "Hata", "talimatname/genel benzeri bir dizin beklenmekte.")
        else:
            dizindekiler = os.listdir(dizin)
            for i in dizindekiler:
                for x in os.listdir(dizin+os.sep+i):
                    self.var_olan_gerekler_liste.append(str(x))
            self.var_olan_gerekler_liste.sort()
            self.var_olan_gerekler.addItems(self.var_olan_gerekler_liste)

class GerekEkle(QDialog):
    def __init__(self,ebeveyn=None):
        super(GerekEkle,self).__init__(ebeveyn)
        self.ebeveyn = ebeveyn
        form_kutu = QFormLayout()
        self.setLayout(form_kutu)
        self.gerek_adi = QLineEdit()
        form_kutu.addRow(QLabel("Gerek Adı:"),self.gerek_adi)
        self.tamam_dugme = QPushButton("Ekle")
        self.tamam_dugme.clicked.connect(self.ekle)
        form_kutu.addWidget(self.tamam_dugme)

    def ekle(self):
        if self.gerek_adi.text() != "":
            self.ebeveyn.gerek_ekle_fonk(self.gerek_adi.text())
            QDialog.accept(self)

class GrupEkle(QDialog):
    def __init__(self,ebeveyn=None):
        super(GrupEkle,self).__init__(ebeveyn)
        self.ebeveyn = ebeveyn
        form_kutu = QFormLayout()
        self.setLayout(form_kutu)
        self.gerek_adi = QLineEdit()
        form_kutu.addRow(QLabel("Grup Adı:"),self.gerek_adi)
        self.tamam_dugme = QPushButton("Ekle")
        self.tamam_dugme.clicked.connect(self.ekle)
        form_kutu.addWidget(self.tamam_dugme)

    def ekle(self):
        if self.gerek_adi.text() != "":
            if self.gerek_adi.text() not in self.ebeveyn.secilen_grub_liste:
                self.ebeveyn.secilen_grub_liste.append(self.gerek_adi.text())
                self.ebeveyn.program_grup.addItems(self.ebeveyn.secilen_grub_liste)

            QDialog.accept(self)

class TalimatindirSinif(QDialog):
    def __init__(self,ebeveyn=None):
        super(TalimatindirSinif,self).__init__(ebeveyn)
        tab_widget = QTabWidget()
        tab_widget.addTab(self.indir_bir(),"Arch Link ile")
        tab_widget.addTab(self.indir_iki(), "Arch Paket ile")
        tab_widget.addTab(self.indir_uc(), "Milis,Crux Link ile")
        merkez_kutu = QVBoxLayout()
        self.resize(400,200)
        self.setLayout(merkez_kutu)
        merkez_kutu.addWidget(tab_widget)


    def indir_bir(self):
        indir_parca = QWidget()
        merkez_kutu = QFormLayout()
        indir_parca.setLayout(merkez_kutu)
        self.url_arc = QLineEdit()
        indir = QPushButton("İndir")
        indir.clicked.connect(self.arc_url_cek)
        merkez_kutu.addRow(QLabel("Url"),self.url_arc)
        merkez_kutu.addWidget(indir)
        return indir_parca

    def indir_iki(self):
        indir_parca = QWidget()
        merkez_kutu = QFormLayout()
        indir_parca.setLayout(merkez_kutu)
        self.url_paket = QLineEdit()
        indir = QPushButton("İndir")
        indir.clicked.connect(self.arc_paket_cek)
        merkez_kutu.addRow(QLabel("Paket"),self.url_paket)
        merkez_kutu.addWidget(indir)
        return indir_parca

    def indir_uc(self):
        indir_parca = QWidget()
        merkez_kutu = QFormLayout()
        indir_parca.setLayout(merkez_kutu)
        self.url_cl = QLineEdit()
        indir = QPushButton("İndir")
        indir.clicked.connect(self.arc_cl_cek)
        merkez_kutu.addRow(QLabel("Url"),self.url_cl)
        merkez_kutu.addWidget(indir)
        return indir_parca

    def arc_url_cek(self):
        url = self.url_arc.text()
        if url != "":
            QMessageBox.information(self,"Başarılı","Url başarılı şekilde alınmıştır")
            QDialog.accept(self)
        else:
            QMessageBox.warning(self,"Hata","Lütfen geçerli bir url girin")

    def arc_paket_cek(self):
        url = self.url_paket.text()
        if url != "":
            QMessageBox.information(self,"Başarılı","Url başarılı şekilde alınmıştır")
            QDialog.accept(self)
        else:
            QMessageBox.warning(self,"Hata","Lütfen geçerli bir url girin")

    def arc_cl_cek(self):
        url = self.url_cl.text()
        if url != "":
            QMessageBox.information(self,"Başarılı","Url başarılı şekilde alınmıştır")
            QDialog.accept(self)
        else:
            QMessageBox.warning(self,"Hata","Lütfen geçerli bir url girin")


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    uygulama.setOrganizationName('Talimatci')
    uygulama.setApplicationName('Talimatci')
    merkezPencere = TalimatciPencere()
    merkezPencere.show()
    sys.exit(uygulama.exec_())
