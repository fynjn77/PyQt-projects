# import sys, time, random
# from PyQt5 import QtCore,QtGui, QtWidgets
# from des import *
#
# #основной класс ui
# class MyWin(QtWidgets.QMainWindow):
#     def __init__(self, parent=None, ):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.gettext)
#         self.ui.checkBox.clicked.connect(self.output )
#         # self.ui.pushButton.clicked.connect(self.handler)
#         # self.ui.pushButton.clicked - это сигнал
#         # .connect - соединяю сигнал и обработчик сигнала
#         # (self.handler) - обработчик сигнала
#
#     # def handler(self): #обработчик
#     #     self.ui.pushButton.set(False)
#     #     self.ui.plainTextEdit.appendPlainText('test text')
#     #     self.ui.label.setText('text')
#
#     def output(self):
#         # self.ui.plainTextEdit.appendPlainText('checkbox')
#         name = self.ui.checkBox.text()
#         number = str(random.randint(0, 100))
#         print(name)
#         self.ui.radioButton.setTextnumber)
#
#     def gettext(self):
#         if self.ui.checkBox.isChecked():
#             checkbox_1 = self.ui.checkBox.text()
#         else:
#             checkbox_1 = ''
#         if self.ui.checkBox_2.isChecked():
#             checkbox_2 = self.ui.checkBox_2.text()
#         else:
#             checkbox_2 = ''
#
#         if self.ui.radioButton.isChecked():
#             radio = self.ui.radioButton.text()
#         else:
#             radio = ''
#         if self.ui.radioButton_2.isChecked():
#             radio_2 = self.ui.radioButton_2.text()
#         else:
#             radio_2 = ''
#
#         result = f'{checkbox_1}{checkbox_2}{radio}{radio_2} HELLO WORLD'
#
#         self.ui.plainTextEdit.appendPlainText(result)
#
#
#
#
#
#
# # точка входа
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv) #передаю флаги, если есть
#     myapp = MyWin() #создаю экземпляр основного класса
#     myapp.show()
#     sys.exit(app.exec_())