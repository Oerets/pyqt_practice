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
        main_layout = QFormLayout()

        name_widget = QLineEdit()
        birthday_layout = QHBoxLayout()
        year_widget = QComboBox()
        month_widget = QComboBox()
        day_widget = QComboBox()

        birthday_layout.addWidget(year_widget)
        birthday_layout.addWidget(month_widget)
        birthday_layout.addWidget(day_widget)

        for year in range(1900, 2021):
            year_widget.addItem(str(year))
                
        for month in range(1, 13):
            month_widget.addItem(str(month))

        for day in range(1, 32):
            day_widget.addItem(str(day))

        address_layout = QVBoxLayout()
        address_1 = QComboBox()
        address_1.addItems(["Seoul", "Daegu", "Daejeon", "Busan"])
        address_2 = QLineEdit()
        address_layout.addWidget(address_1)
        address_layout.addWidget(address_2)

        email_layout = QHBoxLayout()
        email_id = QLineEdit()
        email_company = QLineEdit()
        email_company_cb = QComboBox()
        email_company_cb.addItems(["google.com","naver.com","yahoo.com"])

        email_at = QLabel("@")
        email_layout.addWidget(email_id)
        email_layout.addWidget(email_at)
        email_layout.addWidget(email_company)
        email_layout.addWidget(email_company_cb)

        number_layout = QHBoxLayout()
        number_1 = QLineEdit()
        slash_1 = QLabel("-")
        number_2 = QLineEdit()
        slash_2 = QLabel("-")
        number_3 = QLineEdit()

        number_layout.addWidget(number_1)
        number_layout.addWidget(slash_1)
        number_layout.addWidget(number_2)
        number_layout.addWidget(slash_2)
        number_layout.addWidget(number_3)

        height_widget = QSpinBox()
        height_widget.setMaximum(250)

        personal_info_share = QCheckBox('Agree?')

        #self_intro = QLineEdit()
        self_intro = QPlainTextEdit()

        save_cancel_layout = QHBoxLayout()
        save_button = QPushButton('Save')
        cancel_button = QPushButton('Cancel')
        save_cancel_layout.addWidget(save_button)
        save_cancel_layout.addWidget(cancel_button)

        main_layout.addRow('Name : ',name_widget)
        main_layout.addRow('Birth date : ', birthday_layout)
        main_layout.addRow('Address : ', address_layout)
        main_layout.addRow('Email : ', email_layout)
        main_layout.addRow('Contact number : ', number_layout)
        main_layout.addRow('Height : ', height_widget)
        main_layout.addRow('Personal Information share : ', personal_info_share)
        main_layout.addRow('Introducion : ', self_intro)
        main_layout.addRow('', save_cancel_layout)

        self.setLayout(main_layout)
        self.resize(500,500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())