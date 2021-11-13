import sys
from wtf.des import *



#основной класс ui
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.modal)
        self.ui.pushButton.clicked.connect(self.qt_modal)

    def modal(self):
        window = modal_window(self)# привяжется к текущему окну
                                    # если указать self
        window.show()


    def qt_modal(self):
        window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        window.setWindowTitle('title')
        window.setWindowModality(2)
        window.resize(500, 500)
        window.show()








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


