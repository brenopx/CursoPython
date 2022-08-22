"""
PyQT é toolkit desenvolvido em C++ utilizando por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc....
pip install pyqt5
"""
import sys
from PyQT5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
