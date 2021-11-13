import sys, time, random
from PyQt5 import QtCore,QtGui, QtWidgets
from des import *

#основной класс ui
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_value)
        self.ui.pushButton_2.clicked.connect(self.remove_values)
        self.ui.pushButton_3.clicked.connect(self.set_style)


#глобальные переменные
        self.progress_flag = False




    def add_value(self):
        so_value = self.ui.lineEdit.text()
        progressbar_value = self.ui.progressBar.value()
        if so_value:
            AllItems = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
            # проверяю на уникальность (с учетом регистра)
            if so_value in AllItems:
                self.ui.plainTextEdit.appendPlainText('Объект уже существует')

            elif progressbar_value < 100:
                self.ui.comboBox.addItem(so_value)
                self.ui.plainTextEdit.appendPlainText('Объект успешно добавлен')
                self.ui.progressBar.setValue(progressbar_value + 25)

            elif progressbar_value == 100:
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText('Список заполнен!')





        #     for item in range(self.ui.comboBox.count()):
        #         list_items += range(self.ui.comboBox.itemText(item))
        #         print(list_items)
        #         # if so_value != self.ui.comboBox.itemText(item):
        #         # # print(self.ui.comboBox.itemText(item))
        #         #


    def remove_values(self):
        self.ui.comboBox.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText('Объекты удалены')
        self.ui.progressBar.setValue(0)


    def set_style(self):
        default_style = '''
        QProgressBar{
        }
        '''

        style = '''
            QProgressBar::chunk{
            background-color: red;
            width: 10px;
            margin: 1px;            
            }
        '''

        if not self.progress_flag:
            self.ui.progressBar.setStyleSheet(style)
            self.progress_flag = True
        else:
            self.ui.progressBar.setStyleSheet(default_style)
            self.progress_flag = False


# точка входа
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #передаю флаги, если есть
    mywin = GUI() #создаю экземпляр основного класса
    mywin.show()
    sys.exit(app.exec_())


