# from utilities.fileparser import FileParser
    
# parser = FileParser("ebsd.ang")
# header = parser.parseHeader('/Users/joeykleingers/Downloads/011.ang')
# for key, value in header.entries.items():
#     print(f'{key}, {value}')

import sys

from mainwindow import MainWindow
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())