import json
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_rad_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.h_cmb_lay1 = QHBoxLayout()
        self.h_cmb_lay2 = QHBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("name...")
        self.second = QLineEdit()
        self.second.setPlaceholderText("second...")
        self.age = QLineEdit()
        self.age.setPlaceholderText("age...")

        self.lbl_t = QLabel("Registration")
        self.lbl_j = QLabel("Jins:")
        self.lbl_city = QLabel("Shahar:")
        self.lbl_dist = QLabel("Tuman:")

        self.r1_M = QRadioButton("M")
        self.r2_F = QRadioButton("F")

        f = open('reg.json')
        self.data = json.load(f)
        f.close()

        self.cmb_city = QComboBox()
        self.cmb_dist = QComboBox()

        self.cmb_city.addItems(self.data['cities'])
        self.cmb_city.activated[str].connect(self.dist)

        self.btn_sub = QPushButton("Submit")
        self.btn_sub.clicked.connect(self.submit)
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(exit)

        self.h_rad_lay.addWidget(self.lbl_j)
        self.h_rad_lay.addWidget(self.r1_M)
        self.h_rad_lay.addWidget(self.r2_F)

        self.h_cmb_lay1.addWidget(self.lbl_city)
        self.h_cmb_lay1.addWidget(self.cmb_city)

        self.h_cmb_lay2.addWidget(self.lbl_dist)
        self.h_cmb_lay2.addWidget(self.cmb_dist)

        self.h_btn_lay.addWidget(self.btn_sub)
        self.h_btn_lay.addWidget(self.btn_exit)

        self.v_main_lay.addWidget(self.lbl_t)
        self.v_main_lay.addWidget(self.name)
        self.v_main_lay.addWidget(self.second)
        self.v_main_lay.addWidget(self.age)
        self.v_main_lay.addLayout(self.h_rad_lay)
        self.v_main_lay.addLayout(self.h_cmb_lay1)
        self.v_main_lay.addLayout(self.h_cmb_lay2)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def submit(self):
        self.msg = QMessageBox()

        if (
            self.name.text()
            and self.second.text()
            and self.age.text().isdigit()
            and (self.r1_M.isChecked() or self.r2_F.isChecked())
            and self.cmb_city.currentText()
            and self.cmb_dist.currentText()
        ):
            f = open("reg.json", "r")
            data = json.load(f)
            f.close()

            g = "M" if self.r1_M.isChecked() else "F"

            user = {
                "name": self.name.text(),
                "second": self.second.text(),
                "age": int(self.age.text()),
                "gender": g,
                "city": self.cmb_city.currentText(),
                "district": self.cmb_dist.currentText()
            }

            data["users"].append(user)

            f = open("reg.json", "w")
            json.dump(data, f, indent=4)
            f.close()

            self.name.clear()
            self.second.clear()
            self.age.clear()
            self.r1_M.setChecked(False)
            self.r2_F.setChecked(False)
            self.cmb_city.setCurrentIndex(0)
            self.cmb_dist.clear()

            self.msg.setText("Hurmatli mijoz sizning barcha malumotlaringiz saqlandi!")
            self.msg.setIcon(QMessageBox.Information)
        else:
            self.msg.setText("Hamma maydonlarni to'ldiring!")
            self.msg.setIcon(QMessageBox.Warning)

        self.msg.exec_()
    
    def dist(self, city):
        self.cmb_dist.clear()
        if city == 'Andijon':
            self.cmb_dist.addItems(self.data['districts']['Andijon'])
        elif city == 'Buxoro':
            self.cmb_dist.addItems(self.data['districts']['Buxoro'])
        elif city == "Farg'ona":
            self.cmb_dist.addItems(self.data['districts']["Farg'ona"])
        elif city == 'Jizzax':
            self.cmb_dist.addItems(self.data['districts']['Jizzax'])
        elif city == 'Xorazm':
            self.cmb_dist.addItems(self.data['districts']['Xorazm'])
        elif city == 'Namangan':
            self.cmb_dist.addItems(self.data['districts']['Namangan'])
        elif city == 'Navoiy':
            self.cmb_dist.addItems(self.data['districts']['Navoiy'])
        elif city == 'Qashqadaryo':
            self.cmb_dist.addItems(self.data['districts']['Qashqadaryo'])
        elif city =='Samarqand':
            self.cmb_dist.addItems(self.data['districts']['Samarqand'])
        elif city =='Sirdaryo':
            self.cmb_dist.addItems(self.data['districts']['Sirdaryo'])
        elif city =='Surxondaryo':
            self.cmb_dist.addItems(self.data['districts']['Surhandaryo'])
        elif city =='Toshkent':
            self.cmb_dist.addItems(self.data['districts']['Toshkent'])
        else:
            self.cmb_dist.addItems(self.data['districts']['Toshkent shahri'])

        
app = QApplication([])
win = MyWindow()
win.show()
app.exec_()