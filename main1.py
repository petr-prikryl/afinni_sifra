



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_generated import Ui_MainWindow
from main import filter_input, encrypt, decrypt


class AffineCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect UI elements to functions
        self.ui.pushButton_encrypt.clicked.connect(self.encrypt_text)
        self.ui.pushButton_decrypt.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        a = int(self.ui.lineEdit_a.text())
        b = int(self.ui.lineEdit_b.text())
        text = self.ui.plainTextEdit_input.toPlainText()

        filtered_text = filter_input(text)
        encrypted_text = encrypt(filtered_text, a, b)

        self.ui.plainTextEdit_output.setPlainText(encrypted_text)

    def decrypt_text(self):
        a = int(self.ui.lineEdit_a.text())
        b = int(self.ui.lineEdit_b.text())
        text = self.ui.plainTextEdit_input.toPlainText()
        decrypted_text = decrypt(text, a, b)
        self.ui.plainTextEdit_output.setPlainText(decrypted_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AffineCipherApp()
    window.show()
    sys.exit(app.exec_())

