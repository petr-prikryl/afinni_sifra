from unidecode import unidecode
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_generated import Ui_MainWindow


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def filter_input(text):
    # odstraneni hacku a carek
    text = unidecode(text)

    # Odstranění random znaku
    special_chars = ['!', '>', '.', '-', ',']
    for char in special_chars:
        text = text.replace(char, '')

    # Nahrazení mezery za "XMEZERAX"
    text = text.replace(' ', 'XMEZERAX')

    return text


def encrypt(text, a, b):
    result = ''
    count = 0
    for char in text:
        if char.isalpha():
            char = char.upper()
            char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            result += char
            count += 1
            if count % 5 == 0:
                result += ' '  # mezery
        elif char.isdigit():
            char = chr(((int(char) + b) % 10) + ord('0'))  # cezarovasifra
            result += char
            count += 1
            if count % 5 == 0:
                result += ' '  # mezery
        else:
            pass

    return result


def decrypt(text, a, b):
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "a není nesoudělné s 26, nelze provést dešifrování."

    result = ''
    word = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                char = chr(((a_inverse * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            else:
                char = chr(((a_inverse * (ord(char) - ord('a') - b)) % 26) + ord('A'))
            word += char
        elif char.isdigit():
            char = chr(((int(char) - b) % 10) + ord('0'))  # cesarova sifra
            word += char
        else:
            pass

        if len(word) == 5:
            result += word
            word = ''

    result += word

    result = result.replace('XMEZERAX', ' ')  # vracecka mezer

    return result


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
