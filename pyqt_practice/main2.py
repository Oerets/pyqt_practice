import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #main_layout = QHBoxLayout() #수평 배치
        main_layout = QVBoxLayout() #수직 배치
        #main_layout = QGridLayout() #행렬 배치

        w_1 = QPushButton("Widget_1")
        w_2 = QPushButton("Widget_2")
        w_3 = QPushButton("Widget_3")
        w_4 = QPushButton("Widget_4")
        w_5 = QPushButton("Widget_5")
        w_6 = QPushButton("Widget_6")
        w_7 = QPushButton("Widget_7")
        w_8 = QPushButton("Widget_8")
        w_9 = QPushButton("Widget_9")
        w_10 = QPushButton("Widget_10")
        w_11 = QPushButton("Widget_11")

        layout_1 = QHBoxLayout()
        layout_1.addWidget(w_1)
        layout_1.addWidget(w_2)
        layout_1.addWidget(w_3)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(w_4)
        layout_2.addWidget(w_5)
        layout_2.addWidget(w_6)

        layout_3 = QHBoxLayout()
        layout_3.addWidget(w_7)
        layout_3.addWidget(w_8)
        layout_3.addWidget(w_9)
        layout_3.addWidget(w_10)

        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        main_layout.addLayout(layout_3)
        main_layout.addWidget(w_11)

        self.setLayout(main_layout)
        self.resize(500,500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())