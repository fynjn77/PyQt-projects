import sys, time, random
from PyQt5 import QtCore,QtGui, QtWidgets
from des import *


class Handler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str) # указываю тип(ы) данных

    def __init__(self, parent=None):
        super(Handler, self).__init__(parent)

    def run(self):
        self.mysignal.emit('mysignal') #только одно значение т.к.
                                        #указан один тип данных



#основной класс ui
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.start_handler)

        self.mythread = Handler()
        self.mythread.mysignal.connect(self.add_item)


    def start_handler(self):
        self.mythread.start()# могу использовать метод start только потому,
                                #что внутри потока есть метод run()

    def add_item(self, value): # если бы в mysignal было указано больше
                                # типов данных, то здесь было бы больше
                                # параметров
        for item in value:
            self.ui.plainTextEdit.appendPlainText(str(item))

    def event(self, value):
        if value.type() == QtCore.QEvent.KeyPress:
            text = f'нажата клавиша: {value.text()}'
            self.ui.plainTextEdit.appendPlainText(text)
        elif value.type() == QtCore.QEvent.MouseButtonPress:
            text = f'координаты нажатия: {value.x()}, {value.y()}'
            self.ui.plainTextEdit.appendPlainText(text)
        return QtWidgets.QWidget.event(self, value)


    #
    # #Событие на закрытие
    def closeEvent(self, value):
        # value.ignore()
        result = QtWidgets.QMessageBox.question(self, 'Оповещение', 'Закрыть программу',
                                                QtWidgets.QMessageBox.Yes |
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.No:
            value.ignore()






# точка входа
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #передаю флаги, если есть
    mywin = GUI() #создаю экземпляр основного класса
    mywin.show()
    sys.exit(app.exec_())


