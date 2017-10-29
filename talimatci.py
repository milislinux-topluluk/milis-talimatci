from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout, QFormLayout, QLineEdit, QLabel, QComboBox, QCheckBox,
                             QVBoxLayout, QTextEdit, QPushButton,QFileDialog,QMessageBox,QListWidget, QDialog, QAction)
from PyQt5.QtCore import QDir,QUrl, Qt
import sys,os


class TalimciPencere(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(TalimciPencere,self).__init__(ebeveyn)
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
        self.gerec_url_dugme = QPushButton("Gerec Url")
        self.gerec_url_dugme.clicked.connect(self.url_ac_func)
        ac_kutu.addWidget(self.gerec_url_dugme)
        self.gerec_url = QLineEdit()
        self.gerec_url.setReadOnly(True)
        ac_kutu.addWidget(self.gerec_url)

        form_kutu = QHBoxLayout()
        merkez_kutu.addLayout(form_kutu)
        ilk_form = QFormLayout()
        form_kutu.addLayout(ilk_form)
        ikinci_form = QFormLayout()
        form_kutu.addLayout(ikinci_form)

        self.program_ad = QLineEdit()
        ilk_form.addRow(QLabel("Ad"),self.program_ad)
        self.program_surum = QLineEdit()
        ikinci_form.addRow(QLabel("Surum"),self.program_surum)
        self.program_devir = QLineEdit()
        ilk_form.addRow(QLabel("Devir"),self.program_devir)
        self.program_kaynak = QLineEdit()
        ikinci_form.addRow(QLabel("Source"),self.program_kaynak)
        self.program_tanim = QLineEdit()
        ilk_form.addRow(QLabel("Tanım"),self.program_tanim)
        self.program_url = QLineEdit()
        ikinci_form.addRow(QLabel("Url"),self.program_url)
        self.program_paketci = QLineEdit()
        ilk_form.addRow(QLabel("Paketci"),self.program_paketci)

        grub_kutu = QHBoxLayout()
        merkez_kutu.addLayout(grub_kutu)
        grub_label = QLabel("Grup")
        grub_label.setFixedWidth(40)
        grub_kutu.addWidget(grub_label)
        self.gruplar_combo = QComboBox()
        self.varolan_grup_list = ["uygulamalar","ofis ve verimlilik","güvenlik","geliştirme","sürücüler","oyunlar","kde","xfce4","gnome",
                                  "mate","ağ","bilim ve mühedislik","medya","grafik","sistem araçları","x11","sistem","kütüphane","tasarım",
                                  "kapalı kaynak"]
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


        merkez_kutu.addWidget(QLabel("Gerekler"))
        gerek_kutu = QHBoxLayout()
        merkez_kutu.addLayout(gerek_kutu)
        self.var_olan_gerekler = QListWidget()
        self.var_olan_gerekler.setContextMenuPolicy(Qt.ActionsContextMenu)
        gerek_talimat_ac_aksiyon = QAction("Talimatı Aç",self,triggered=self.talimat_ac)
        self.var_olan_gerekler.addAction(gerek_talimat_ac_aksiyon)
        gerek_kutu.addWidget(self.var_olan_gerekler)
        dugme_kutu = QVBoxLayout()
        gerek_kutu.addLayout(dugme_kutu)
        self.saga_dugme = QPushButton(">")
        self.saga_dugme.clicked.connect(self.saga_dugme_fonk)
        dugme_kutu.addWidget(self.saga_dugme)
        self.sola_dugme = QPushButton("<")
        self.sola_dugme.clicked.connect(self.sola_dugme_fonk)
        dugme_kutu.addWidget(self.sola_dugme)
        sag_dugme_kutu = QVBoxLayout()
        gerek_kutu.addLayout(sag_dugme_kutu)
        self.secilen_gerekler = QListWidget()
        sag_dugme_kutu.addWidget(self.secilen_gerekler)
        self.gerek_ekle_dugme = QPushButton("Ekle")
        self.gerek_ekle_dugme.clicked.connect(self.gerek_ekle)
        sag_dugme_kutu.addWidget(self.gerek_ekle_dugme)

        merkez_kutu.addWidget(QLabel("Build"))
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

    def talimat_ac(self):
        secilen = self.var_olan_gerekler.currentItem().text()
        url = self.gerec_url.text() + os.sep + secilen[0] + os.sep + secilen + os.sep + "talimat"
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

    def url_ac_func(self):
        dizin = QFileDialog.getExistingDirectory(self, self.tr("Gerek Dizini"), "/root/talimatname/genel", QFileDialog.ShowDirsOnly)
        if dizin:
            if dizin != ("",""):
                self.gerec_url.setText(dizin)
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
        yazilacak += "kaynak=(" + self.program_kaynak.text().replace(" ","\n        ") + ")\n\n"
        yazilacak += self.program_build.toPlainText()
        return yazilacak

    def temizle(self):
        self.secilen_gerekler.clear()
        self.program_grup.clear()


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
                        kaynak = i[8:-2].replace(" ", "")
                        self.program_kaynak.setText(kaynak)
                        self.acilan_sozluk["kaynak"] = kaynak
                    else:
                        kaynak_tum.append(i[8:-1])
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
                    kaynak = i.replace(" ", "")
                    if i[-2] == ")":
                        kaynak_tum.append(kaynak[:-2])
                        kaynak_durum = False
                        self.program_kaynak.setText(" ".join(kaynak_tum))
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


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    uygulama.setOrganizationName('Talimci')
    uygulama.setApplicationName('Talimci')
    merkezPencere = TalimciPencere()
    merkezPencere.show()
    sys.exit(uygulama.exec_())