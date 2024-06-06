import sys
from objectbox import *
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
import trial as back

Store.remove_db_files("TransactionsDB")
store = Store(directory="TransactionsDB")
box = store.box(back.Transaction)

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 400, 300)
        
        self.total_balance = 10000
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()   # lines up widgets vertically
        
        self.balance_label = QLabel(f"Current Balance: {self.total_balance}")
        layout.addWidget(self.balance_label)
        
        # Amount input
        amount_layout = QHBoxLayout()   # lines up widgets horizontally
        amount_layout.addWidget(QLabel("Amount:"))
        self.amount_input = QLineEdit()
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)
        
        # Name input
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Name:"))
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)
        
        # Action buttons
        buttons_layout = QHBoxLayout()
        
        self.credit_button = QPushButton("Credit")
        self.credit_button.clicked.connect(self.credit)
        buttons_layout.addWidget(self.credit_button)
        
        self.debit_button = QPushButton("Debit")
        self.debit_button.clicked.connect(self.debit)
        buttons_layout.addWidget(self.debit_button)
        
        self.lend_button = QPushButton("Lend")
        self.lend_button.clicked.connect(self.lend)
        buttons_layout.addWidget(self.lend_button)
        
        self.borrow_button = QPushButton("Borrow")
        self.borrow_button.clicked.connect(self.borrow)
        buttons_layout.addWidget(self.borrow_button)
        
        self.display_button = QPushButton("Display Transactions")
        self.display_button.clicked.connect(self.display_transactions)
        buttons_layout.addWidget(self.display_button)
        
        layout.addLayout(buttons_layout)
        
        central_widget.setLayout(layout)
    
    def update_balance(self):
        self.balance_label.setText(f"Current Balance: {self.total_balance}")
    
    def credit(self):
        try:
            amount = int(self.amount_input.text())
            transaction = back.Transaction(action="credit", amount=amount)
            self.total_balance = transaction.credit(amount, self.total_balance)
            self.update_balance()
            box.put(transaction)
            self.amount_input.clear()
            self.name_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
    
    def debit(self):
        try:
            amount = int(self.amount_input.text())
            transaction = back.Transaction(action="debit", amount=amount)
            self.total_balance = transaction.debit(amount, self.total_balance)
            self.update_balance()
            box.put(transaction)
            self.amount_input.clear()
            self.name_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
    
    def lend(self):
        try:
            amount = int(self.amount_input.text())
            name = self.name_input.text()
            transaction = back.Transaction(action="lent", amount=amount, name=name)
            self.total_balance = transaction.lent(amount, name, self.total_balance)
            self.update_balance()
            box.put(transaction)
            self.amount_input.clear()
            self.name_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
    
    def borrow(self):
        try:
            amount = int(self.amount_input.text())
            name = self.name_input.text()
            transaction = back.Transaction(action="borrowed", amount=amount, name=name)
            self.total_balance = transaction.borrowed(amount, name, self.total_balance)
            self.update_balance()
            box.put(transaction)
            self.amount_input.clear()
            self.name_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
    
    
    def display_transactions(self):
        items = ["Credit", "Debit", "Lent", "Borrowed"]
        item, ok = QInputDialog.getItem(self, "Select Transaction Type", "Display Transactions:", items, 0, False)
        # print("item", item)
        # print("ok", ok)
        if ok and item:
            transaction_type = item.lower()   
            q = box.query(back.Transaction.action.equals(transaction_type)).build()   #find all transactions with given type
            transactions = q.find()  #returns a list
            
            if transactions:
                display_text = "\n".join(  # change to a string and traverse using a loop
                    [f"Id: {t.id}, Amount: {t.amount}, Name: {t.name}, Action: {t.action} " for t in transactions])
            else:
                display_text = f"No {item} transactions found."
            
            QMessageBox.information(self, "Transactions", display_text)



app = QApplication(sys.argv)
window = ExpenseTracker()
window.show()
sys.exit(app.exec())
