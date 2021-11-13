import sys, time, random
from PyQt5 import QtCore,QtGui, QtWidgets
from des import *
from mod import *


#основной класс ui
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.open_files)
        self.ui.pushButton_3.clicked.connect(self.save_file)
        self.ui.pushButton_4.clicked.connect(self.color)
        self.ui.pushButton_5.clicked.connect(self.open_folders)

    def open_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'headers', 'filename', 'Python *.py\nCSS *.css\nHTML *.html\n Qt *.ui')
        print(file_path)

    def save_file(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(self)
        print(file_path)

        with open(file_path[0], 'w') as file:
            file.write('!!!')


    def open_files(self):
        file_path = QtWidgets.QFileDialog.getOpenFileNames(self, 'headers', 'filename', 'Python *.py')
        print(file_path)

    def open_folders(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(directory)

    def color(self):
        color = QtWidgets.QColorDialog(self).getColor()
        print(color.red(), color.green(), color.blue(), color.yellow(), color.alpha())










class modal_window(QtWidgets.QWidget):
    def __init__(self, parent=GUI):
        # QtWidgets.QWidget.__init__(self,parent) #
        super().__init__(parent, QtCore.Qt.Window)  #super() позволяет писать
                                # не копируя параметры класса
                                # и не используя в (self)
                                # QtCore.Qt.Window создает отдельное окно.
                                # если ничего не указать после Parent
                                # то вызываемое отобразится в род.окне
        self.modal= Ui_Form()
        self.modal.setupUi(self)
        self.setWindowModality(1) # 0 - не использовать мод.окна(по умолч.)
                                # 1 - использовать только для предыдущего.
                                # 2 - использовать для всей программы






















# точка входа
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #передаю флаги, если есть
    mywin = GUI() #создаю экземпляр основного класса
    mywin.show()
    sys.exit(app.exec_())


