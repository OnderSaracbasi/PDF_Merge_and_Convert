from PyQt5.QtWidgets import QLineEdit, QListWidget, QPushButton, QWidget, \
                            QVBoxLayout, QHBoxLayout, \
                            QFileDialog, QMessageBox, QApplication, QAction, QMainWindow
from PyPDF2 import PdfFileMerger
import os, sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton, QWidget, QApplication, \
                            QVBoxLayout, QHBoxLayout, \
                            QFileDialog, QMessageBox
from PIL import Image

class PDF_Merge (QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):
        self.cikti_yolu = QLineEdit()
        self.browse = QPushButton("Çıktı Yolunu Seç")
        self.dosyalar = QListWidget()
        self.merge = QPushButton("Birleştir")
        self.cancel = QPushButton("İptal")
        self.temizle = QPushButton("Temizle")

        h_box = QHBoxLayout()
        h_box.addWidget(self.cikti_yolu)
        h_box.addWidget(self.browse)
        self.browse.clicked.connect(self.yol_sec)
        h_box.addWidget(self.merge)
        self.merge.clicked.connect(self.birlestir)
        h_box.addWidget(self.cancel)
        self.cancel.clicked.connect(self.iptal)
        h_box.addWidget(self.temizle)
        self.temizle.clicked.connect(self.cleaner)
        

        v_box = QVBoxLayout()
        v_box.addWidget(self.dosyalar)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        #self.setWindowTitle("PDF Merge")
        #self.show()

        
        self.merge.setEnabled(False)
        self.browse.setEnabled(False)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept ()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            self.links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.links.append(str(url.toLocalFile()))
                else:
                    self.links.append(str(url.toString()))
            self.dosyalar.addItems(self.links)
            self.browse.setEnabled(True)
        else:
            event.ignore()    

    def yol_sec(self):
        self.dosya_ismi = []
        self.dosya_ismi = QFileDialog.getSaveFileName(self, "PDF Dosya Kaydet", os.getcwd(), "PDF File (*.pdf)")
        self.cikti_yolu.setText(self.dosya_ismi[0])
        self.merge.setEnabled(True)

    def cleaner(self):
        self.dosyalar.clear()
        self.cikti_yolu.setText("")


        self.links.clear()
        self.merge.setEnabled(False)
        self.browse.setEnabled(False)

    def iptal(self):
        menu.close()

    def birlestir(self):
        try:
            sourch_dir = os.getcwd()
            merger = PdfFileMerger()
            check = True
            for item in self.links:
                if (item.endswith("pdf")):
                    merger.append(item)
                else:
                    check = False
                    QMessageBox.warning(self, "Tamamlanamadı", "Sürüklediğiniz odsyanın .pdf uzantılı olduğuna emin oldun.")
                    break

            if check:                     
                merger.write(self.dosya_ismi[0])
                merger.close()
                QMessageBox.information(self, "Tamamlandı", "PDF'ler başarıyla birleştirildi")
        except:
            QMessageBox.warning(self, "Tamamlanamadı", "Çıkartmak istediğiniz konumu seçin veya .pdf uzantılı dosyaları sürüklediğinizden emin olun.")

class PDF_Convert (QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.init_ui()
    def init_ui(self):
        self.browse = QPushButton("Çıktı Yolunu Seç")
        self.dosyalar = QListWidget()
        self.convert = QPushButton("Dönüştür")
        self.cancel = QPushButton("İptal")
        self.temizle = QPushButton("Temizle")
        combobox_list = ["Resim", "Word", "Excel", ".odt (LibreOffice Word)", ".ods (LibreOffice Excel)"]
        self.sec = QComboBox()
        self.sec.addItems(combobox_list)

        h_box = QHBoxLayout()
        h_box.addWidget(self.browse)
        self.browse.clicked.connect(self.yol_sec)
        h_box.addWidget(self.convert)
        self.convert.clicked.connect(self.cevir)
        h_box.addWidget(self.cancel)
        self.cancel.clicked.connect(self.iptal)
        h_box.addWidget(self.temizle)
        self.temizle.clicked.connect(self.cleaner)
        h_box.addWidget(self.sec)
        

        v_box = QVBoxLayout()
        v_box.addWidget(self.dosyalar)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        #self.setWindowTitle("Deneme")
        #self.show()

        self.convert.setEnabled(False)
        self.browse.setEnabled(False)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept ()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            self.links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.links.append(str(url.toLocalFile()))
                else:
                    self.links.append(str(url.toString()))
            self.dosyalar.addItems(self.links)
            self.browse.setEnabled(True)
        else:
            event.ignore()

    def yol_sec(self):
        self.dosya_ismi = []
        self.dosya_ismi.append(QFileDialog.getExistingDirectory(self, "Select Dierctorty"))
        #print(self.dosya_ismi)
        self.convert.setEnabled(True)
    
    def cleaner(self):
        self.dosyalar.clear()
        #self.cikti_yolu.setText("")
        self.links.clear()
        self.convert.setEnabled(False)
        self.browse.setEnabled(False)

    def iptal(self):
        menu.close()
        

    def cevir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Lütfen seçmiş olduğunuz dosya yolunda 1.pdf, 2.pdf... adında başka dosyalarınız olmadığından emin " +
        "olun eğer var ise veya emin değilseniz 'Cancel' butonuna basıp başka bir dosya yolu seçiniz aksi taktikde aynı isimli dosyalar değiştirilecektir "+
        "Emin iseniz 'Ok' butonuna tıklayıp işleminizi devam ettirebilirsiniz.")
        msgBox.setWindowTitle("Uyarı")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            secilen = self.sec.currentText()
            try:
                if secilen == "Resim":
                    sayac = 1
                    for i in self.links:
                        resim = Image.open(i)
                        renklendir = resim.convert('RGB')
                        renklendir.save(str(self.dosya_ismi[0]) + "/" + str(sayac) + ".pdf")
                        sayac += 1
                    QMessageBox.information(self, "Tamamlandı", "Resimler başarıyla PDF'e dönüştürüldü.")                
                else: QMessageBox.about(self, "Yapım Aşamasında", "Bu özellik şuan kullanılamıyor, yapım aşamasında")
                """
                elif secilen == "Word":
                    QMessageBox.about(self, "Yapım Aşamasında", "Bu özellik şuan kullanılamıyor, yapım aşamasında")
                """
            except:
                QMessageBox.warning(self, "Tamamlanamadı", "Eklediğiniz dosyanın uzantısını doğru seçtiğinizden emin olun.\n" + 
                "Veya çıkartmak istediğiniz konumu seçin")
        else:
            msgBox.close()

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere_merge = PDF_Merge()
        self.setCentralWidget(self.pencere_merge)

        self.menuleri_olustur()

    def menuleri_olustur(self):
        menubar = self.menuBar()

        sec = menubar.addMenu("Seç")
        merge = QAction("PDF Birleştir", self)
        convert = QAction("PDF'e Dönüştür", self)
        sec.addAction(merge)
        sec.addAction(convert)

        sec.triggered.connect(self.response1)

        help = menubar.addMenu("Yardım")
        merge_help = QAction("PDF Birleştirme Yardım", self)
        convert_help = QAction("PDF'e Dönüştürme Yardım", self)
        help.addAction(merge_help)
        help.addAction(convert_help)

        help.triggered.connect(self.response2)

        self.setWindowTitle("PDF Birleştir")
        self.show()


    def response1(self, action):
        if action.text() == "PDF Birleştir":
            self.pencere_merge = PDF_Merge()
            self.setCentralWidget(self.pencere_merge)
            self.setWindowTitle("PDF Birleştir")
            self.pencere_merge.show()

        else:
            self.pencere_convert = PDF_Convert()
            self.setCentralWidget(self.pencere_convert)
            self.setWindowTitle("PDF'e Dönüştür")
            self.pencere_convert.show()

    def response2(self, action):
        if action.text() == "PDF Birleştirme Yardım":
            QMessageBox.information(self, "PDF Birleştirme İşlemi Nasıl Yapılır?",
            "1) Öncelikle birleştirme işleminde dosyaların sırası önem arz ediyorsa dosylarınızın adını alfabetik sıraya veya sıralı sayılar olarak kaydedin. (Ör: A, B, C, ... veya 1, 2, 3, ...) \n \n" +
            "2) Beyaz alana .pdf uzantılı dosyalarını sürükleyin. (NOT: Birden fazla PDF dosyanız var ise hepsini seçip birlikte sürükleyin. Birleştirme işleminde hangisi ilk sırada olmasını istiyosanız onu tutup sürükleyin\n \n" +
            "3) Dosyalarınızı sürükledikten sonra 'Çıktı Yolunu Seç' butonuna tıklayarak birleştirilecek dosyanın nereye kaydedileceğini belirleyiniz. (Çıktı yolunu seçerken 'Dosya ad:' alanını doldurunuz.) \n \n" +
            "4) Daha sonra 'Birleştir' butonuna tıklayarak birleştirme işlemini başlatabilirsiniz. (Birleştirme işlemi bittiğinde bilgilendirileceksin.)")

        else:
            QMessageBox.information(self, "PDF'e Dönüştürme İşlemi Nasıl Yapılır.", 
            "1) Öncelikle dönüştüme işleminde dosyaların sırası önem arz ediyorsa dosylarınızın adını alfabetik sıraya veya sıralı sayılar olarak kaydedin. (Ör: A, B, C, ... veya 1, 2, 3, ...) \n \n" +
            "2) Beyaz alana .jpg, .jpeg veya .png uzantılı dosyalarınızı sürükleyin. (NOT: Birden fazla dosyanız var ise hepsini seçip birlikte sürükleyin. Dönüştürme işleminde hangisi ilk sırada olmasını istiyosanız onu tutup sürükleyin\n \n" +
            "3) Dosyalarınızı sürükledikten sonra 'Çıktı Yolunu Seç' butonuna tıklayarak dönüştürülecek dosyaların nereye kaydedileceğini belirleyiniz. (Çok fazla dosya var ise masaüstü yerine yeni bir klasör oluşturup o klasörü seçmeniz tavsiye edilir.) \n \n" +
            "4) Daha sonra 'Dönüştür' butonuna tıklayarak dönüştürme işlemini başlatabilirsiniz. (Dönüştürme işlemi bittiğinde bilgilendirileceksin.) \n \n" +
            "** NOT **: Dönüştürme işleminde PDF'leri 1.pdf 2.pdf, 3.pdf ... gibi isimlendirilecek eğer seçtiğiniz dosya yolunda aynı dosya isminde başka dosyanız var ise o dosyanın bir yedeğini alın veya çıktı yolu olarak farklı bir klasör seçin.")


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())