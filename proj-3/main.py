import sys, time, random
from PyQt5 import QtCore,QtGui, QtWidgets
from des import *


#основной класс ui
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.notification)
        self.ui.pushButton_3.clicked.connect(self.confirm)
        self.ui.pushButton_2.clicked.connect(self.message)
        self.ui.pushButton_4.clicked.connect(self.error_message)



    def notification(self):
        # вызов оповещений
        #  QtWidgets.QMessageBox.about(self, 'title', 'message')
         QtWidgets.QMessageBox.warning(self, 'title', 'message')
        #  QtWidgets.QMessageBox.information(self, 'title', 'message')
        #  QtWidgets.QMessageBox.critical(self, 'title', 'message')


    def confirm(self):
        # вызов оповещения с подтверждением пользователя
        result = QtWidgets.QMessageBox.question(self, 'Headers',
                                                'Description..',
                                                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes: print('Yes')
        else: print('No')

        # QMessageBox.Ok
        # QMessageBox.Open
        # QMessageBox.Close
        # QMessageBox.Yes
        # QMessageBox.No
        # QMessageBox.Abort
        # QMessageBox.Retry
        # QMessageBox.Ignore



    def message(self):
        # вывод подробного оповещения с доп.информацией
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle('title')
        msg.setInformativeText('description')
        msg.setDetailedText('detailed.. ')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        item = msg.exec_()

        if item == QtWidgets.QMessageBox.Ok:
            print('OK')
        elif item == QtWidgets.QMessageBox.Cancel:
            print('CANCEL')
    #
    #
    def error_message(self):
        # ошибка которая дает возможность пользователю
        # не выводить её в следующний раз

        error = QtWidgets.QErrorMessage(self)
        error.setWindowTitle('Title')
        error.showMessage('error_message')





    # def notification(self):
    #     pass





# точка входа
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #передаю флаги, если есть
    mywin = GUI() #создаю экземпляр основного класса
    mywin.show()
    sys.exit(app.exec_())


