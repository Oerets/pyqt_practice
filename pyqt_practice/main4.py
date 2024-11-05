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
        main_layout = QVBoxLayout()

        pushbutton = QPushButton("button 1")
        pushbutton.clicked.connect(self.button_clicked)
        main_layout.addWidget(pushbutton)

        self.lineedit = QLineEdit()
        main_layout.addWidget(self.lineedit)

        combobox = QComboBox()
        combobox.addItems(["dog", "cat", "rabbit", "lion"])
        combobox.currentTextChanged.connect(self.combobox_changed)
        main_layout.addWidget(combobox)

        checkbox = QCheckBox("Check!")
        checkbox.stateChanged.connect(self.checkbox_changed)
        main_layout.addWidget(checkbox)
        
        radio_1, radio_2 = QRadioButton("A"), QRadioButton("B")
        radio_1.toggled.connect(self.radio_1_toggled)
        radio_2.toggled.connect(self.radio_2_toggled)
        main_layout.addWidget(radio_1)
        main_layout.addWidget(radio_2)



        self.setLayout(main_layout)
        self.resize(500,500)
        self.show()

    def button_clicked(self):
        print("button clicked.")
        self.lineedit.setText("button clicked.")

    def combobox_changed(self, item):
        self.lineedit.setText(f"combobox changed : {item}")

    def checkbox_changed(self, state):
        self.lineedit.setText(f"check box changed : {state}")

    def radio_1_toggled(self, state):
        self.lineedit.setText(f"radio_1 {state}")

    def radio_2_toggled(self, state):
        self.lineedit.setText(f"radio_2 {state}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())