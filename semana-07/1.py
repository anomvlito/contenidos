import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Mi Primera Ventanita')


if __name__ == '__main__':
    
    app = QApplication([])    ## Creamos ls base de la app: QApplication
    ventana = MiVentana()     ## Construirmos un QWidget que será nuestra ventana
    ventana.show()            ## Mostramos la ventna
    sys.exit(app.exec_())     ## La aplicación se inicia con app.exec_(). Esto habilita el loop de eventos
                              ## Su valor de retorno es un código de salida que luego lo tome sys.exit()






# necesito saber el precio de las siguientes enmarcaciones:

1) en vidrio simple 110x180, madera y con foam
2) en vidrio simple 110x180, aluminio y con foam
3) en vidrio opaco 110x200, madera y con foam
4) en vidrio opaco 110x200, aluminio y con foam
5) en vidrio de museo 110x150, madera y con foam
6) en vidrio de museo 110x150, aluminio y con foam
7) en vidrio de museo 110x170, madera y con foam
8) en vidrio de museo 110x170, aluminio y con foam