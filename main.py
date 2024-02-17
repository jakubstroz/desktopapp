from PySide2 import QtCore, QtWidgets,QtGui
import sys
class AppWidget(QtWidgets.QWidget):
    def __init__(self, to_translate) -> None:
        super().__init__()
        self.to_translate = to_translate
        self.layout = self.initialize_layout()
        self.setLayout(self.layout)

    def initialize_layout(self):
        row = 0
        grid = QtWidgets.QGridLayout()

        for key in self.to_translate:


            label = QtWidgets.QLabel(key)
            enter = QtWidgets.QLineEdit()
            grid.addWidget(label, row, 0)
            grid.addWidget(enter, row, 1)
            row += 1

        return grid

if __name__ == '__main__':
    to_translate = {
        'dog': 'pies',
        'cat': 'kot',
        'snake': 'wąż',
        'cow': 'krowa'
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Learn english words with Jakub')
    app_widget = AppWidget(to_translate)
    app_widget.resize(800,600)
    app_widget.show()

    sys.exit(app.exec_())