# SELF LEARNING and TRIALS for PySide6


# import sys
# from PySide6 import QtCore, QtWidgets, QtGui


# # app = QtWidgets.QApplication(sys.argv)
# # window = QtWidgets.QMainWindow()
# # window.setWindowTitle("Expense Tracker")
# # window.setGeometry(600, 500, 500, 500)

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = QtWidgets.Ui_MainWindow()
#         self.ui.setupUi(self)
        
        
# class section:
    
#     def __init__():
#         super.__init__()
#         button = QtWidgets.QPushButton()
        
        
        
# # button = QtWidgets.QPushButton()
# # button.setText("Credit")

# # window.setCentralWidget(button)
# # button.setGeometry(QtCore.QRect(50, 50, 100, 100))

# window.show()

# app.exec()






# # class MyWidget(QtWidgets.QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

# #         self.button = QtWidgets.QPushButton("Click me!")
# #         self.text = QtWidgets.QLabel("Hello World",
# #                                     alignment=QtCore.Qt.AlignCenter)
# #         self.layout = QtWidgets.QVBoxLayout(self)
# #         self.layout.addWidget(self.text)
# #         self.layout.addWidget(self.button)

# #         self.button.clicked.connect(self.magic)

# #     @QtCore.Slot()
# #     def magic(self):
# #         self.text.setText(random.choice(self.hello))
        
# # if __name__ == "__main__":
# #     app = QtWidgets.QApplication([])

# #     widget = MyWidget()
# #     widget.resize(800, 600)
# #     widget.show()

# #     sys.exit(app.exec())
    
from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt


class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 400, 400)

        # Current balance
        self.balance = 0

        # Layouts
        main_layout = QVBoxLayout()
        balance_layout = QHBoxLayout()
        input_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Widgets
        self.balance_label = QLabel(f"Current Balance: INR{self.balance:.2f}")
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.credit_input = QLineEdit()
        self.credit_input.setPlaceholderText("Credit Amount")
        self.debit_input = QLineEdit()
        self.debit_input.setPlaceholderText("Debit Amount")
        self.lent_input = QLineEdit()
        self.lent_input.setPlaceholderText("Lent Amount")
        self.borrowed_input = QLineEdit()
        self.borrowed_input.setPlaceholderText("Borrowed Amount")
        self.lent_person_input = QLineEdit()
        self.lent_person_input.setPlaceholderText("Lent To (Person's Name)")
        self.borrowed_person_input = QLineEdit()
        self.borrowed_person_input.setPlaceholderText("Borrowed From (Person's Name)")

        self.update_button = QPushButton("Update Balance")
        self.update_button.clicked.connect(self.update_balance)

        # Add widgets to layouts
        balance_layout.addWidget(self.balance_label)
        input_layout.addWidget(self.credit_input)
        input_layout.addWidget(self.debit_input)
        input_layout.addWidget(self.lent_input)
        input_layout.addWidget(self.lent_person_input)
        input_layout.addWidget(self.borrowed_input)
        input_layout.addWidget(self.borrowed_person_input)
        button_layout.addWidget(self.update_button)

        main_layout.addLayout(balance_layout)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_balance(self):
        try:
            credit = float(self.credit_input.text() or 0)
            debit = float(self.debit_input.text() or 0)
            lent = float(self.lent_input.text() or 0)
            borrowed = float(self.borrowed_input.text() or 0)
            lent_person = self.lent_person_input.text()
            borrowed_person = self.borrowed_person_input.text()

            self.balance += credit - debit - lent + borrowed
            self.balance_label.setText(f"Current Balance: INR{self.balance:.2f}")

            # if lent_person:
            #     # print(f"Lent ${lent:.2f} to {lent_person}")
            #     pass
            # if borrowed_person:
            #     pass
            #    # print(f"Borrowed ${borrowed:.2f} from {borrowed_person}")

            self.credit_input.clear()
            self.debit_input.clear()
            self.lent_input.clear()
            self.lent_person_input.clear()
            self.borrowed_input.clear()
            self.borrowed_person_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")


# if __name__ == "__main__":
app = QApplication([])
window = ExpenseTracker()
window.show()
app.exec()
