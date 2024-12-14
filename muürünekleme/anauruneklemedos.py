import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from Urun_Ekle import *

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


#veritabanı işlemleri
import sqlite3
baglanti= sqlite3.connect("urunler.db")
islem= baglanti.cursor()
baglanti.commit()
tablo = islem.execute("create table if not exists urun ( urunAdi text, birimFiyat int, stokMiktari int,urunKodu int, urunAciklaması text, marka text, kategori text)")
baglanti.commit

def kayıt_ekle():
    urunAdı = ui.leurunAdi.text()
    birimFiyat = int(ui.lebirimFiyat.text())
    stokMiktarı = int(ui.lestokMiktari.text())
    urunKodu = int(ui.leurunKodu.text())
    urunAciklaması = ui.leurunAciklamasi.text()
    marka = ui.cburunMarkasi.currentText()
    kategori = ui.cbKategori.currentText()
    try:
        ekle = "insert into urun (urunAdi,birimFiyat,stokMiktari ,urunKodu ,urunAciklaması,marka,kategori) values (?,?,?,?,?,?,?)"
        islem.execute(ekle,(urunAdı,birimFiyat, stokMiktarı ,urunKodu, urunAciklaması, marka, kategori))
        baglanti.commit()
        # kayit_listele()
        ui.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı",10000)
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Eklenemedi Hata Çıktı === "+str(error))

def kayıt_listele():
    ui.twListemiz.clear()
    ui.twListemiz.setHorizontalHeaderLabels(("Ürün Adı" , "Birim Fiyatı" , "Stok Miktarı" ,"Ürün Kodu" ,  "Ürün Açıklaması" , "Markası" , "Kategori"))
    sorgu = "select * from urun"
    islem.execute(sorgu)
    for indexSatir , KayıtNumarasi in enumerate(islem):
        for indexSütun , kayıtSütun in enumerate (KayıtNumarasi):
            ui.twListemiz.setItem(indexSatir , indexSütun , QTableWidgetItem (str(kayıtSütun)))

def kategoriye_gore_listele():
    listelenecekategori = ui.cbKategoriListele.currentText()
    sorgu = "select * from urun where kategori = ?" 
    islem.execute(sorgu ,(listelenecekategori,))
    ui.twListemiz.clear()
    for indexSatir , KayıtNumarasi in enumerate(islem):
        for indexSütun , kayıtSütun in enumerate (KayıtNumarasi):
            ui.twListemiz.setItem(indexSatir , indexSütun , QTableWidgetItem (str(kayıtSütun)))

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayı " , "Silmek İstediğinizden Emin Misiniz?" , QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.twListemiz.selectedItems()
        silinecek_kayit = secilen_kayit[0].text()
        sorgu = "delete from urun where urunKodu =  ? "
        try :
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt başarıyla silindi.")
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Eklenemedi Hata Çıktı === "+str(error))
    else :
        ui.statusbar.showMessage("Silme işlemi iptal edildi.")

#butonlar
ui.bEkle.clicked.connect(kayıt_ekle)
ui.bListele.clicked.connect(kayıt_listele)
ui.bKategoriyeGoreListele.clicked.connect(kategoriye_gore_listele)
ui.bSil.clicked.connect(kayit_sil)

sys.exit(uygulama.exec())