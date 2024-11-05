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
        layout = QVBoxLayout()

        label_widget = QLabel("Hello World!")
        button_widget = QPushButton("Click Me")
        combobox_widget = QComboBox()
        combobox_widget.addItem("Python1")
        combobox_widget.addItem("Python2")
        combobox_widget.addItem("Python3")
        combobox_widget.addItem("Python4")
        combobox_widget.addItem("Python5")

        check_box_widget_1 = QCheckBox("Summer")
        check_box_widget_2 = QCheckBox("Winter")

        radio_button_widget_male = QRadioButton("Male")
        radio_button_widget_female = QRadioButton("Female")

        spinbox_widget = QSpinBox()

        date_widget = QDateEdit()
        time_widget = QTimeEdit()

        list_widget = QListWidget()
        item_1 = QListWidgetItem("Dog")
        item_2 = QListWidgetItem("Cat")
        list_widget.addItem(item_1)
        list_widget.addItem(item_2)

        layout.addWidget(label_widget)
        layout.addWidget(button_widget)
        layout.addWidget(combobox_widget)
        layout.addWidget(check_box_widget_1)
        layout.addWidget(check_box_widget_2)
        layout.addWidget(radio_button_widget_male)
        layout.addWidget(radio_button_widget_female)
        layout.addWidget(spinbox_widget)
        layout.addWidget(date_widget)
        layout.addWidget(time_widget)
        layout.addWidget(list_widget)


        self.setLayout(layout)
        self.resize(500,500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())