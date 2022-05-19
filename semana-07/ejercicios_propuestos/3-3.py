import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)
from PyQt5.QtGui import (QPixmap, QColor)
from PyQt5.QtCore import *


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.setGeometry(0, 0, 300, 300)
        self.setMaximumHeight(300)
        self.setMaximumWidth(300)

        self.noetiqueta = QLabel('Blanco', self)
        self.noetiqueta.move(100, 40)

        self.etiqueta = QLabel('Etiqueta', self)
        self.etiqueta.move(100, 70)
        # self.resize(self.etiqueta.sizeHint())

        self.label_blanco = QLabel('blanco', self)
        self.label_blanco.move(10, 50)
        self.label_blanco.setGeometry(QRect(100, 100, 100, 100))

        self.pixmap_blanco = QPixmap(100, 100)
        self.pixmap_blanco.fill(QColor("white"))
        self.label_blanco.setPixmap(self.pixmap_blanco)
        self.label_blanco.show()

        self.show()

    def keyPressEvent(self, event):

        # self.etiqueta.setText(f'Presionaron la tecla: \n{event.text()} de código: {type(event.key()),event.key()}')
        # self.etiqueta.resize(self.etiqueta.sizeHint())

        if event.key() == 86 : # v 86
            self.pixmap_blanco.fill(QColor("green"))
            
            self.label_blanco.setPixmap(self.pixmap_blanco)

            self.noetiqueta.setText("Verde")

        elif event.key() == 82 : # r 82
            self.pixmap_blanco.fill(QColor("red"))
            
            self.label_blanco.setPixmap(self.pixmap_blanco)

            self.noetiqueta.setText("Rojo")

        elif event.key() == 66 :
            self.pixmap_blanco.fill(QColor("white"))
            self.label_blanco.setPixmap(self.pixmap_blanco)
            self.noetiqueta.setText("Blanco")

        elif event.key() == 65 :
            self.pixmap_blanco.fill(QColor("blue"))
            self.label_blanco.setPixmap(self.pixmap_blanco)
            self.noetiqueta.setText("Azul")

        


if __name__ == '__main__':
    app = QApplication([])
    ex = MiVentana()
    sys.exit(app.exec_())