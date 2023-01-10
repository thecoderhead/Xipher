import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import struct
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

# create a password-based key using PBKDF2
def create_key(password):
    salt = b'salt_'  # include a salt to make the key more secure
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key

# encrypt a file using AES
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

# decrypt a file using AES
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)

# create a PyQt5 GUI to encrypt or decrypt a file
class FileCryptoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        # create widgets
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.file_label = QLabel('File:')
        self.file_input = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.encrypt_button = QPushButton('Encrypt')
        self.decrypt_button = QPushButton('Decrypt')
        # create layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.password_label)
        v_layout.addWidget(self.password_input)
        v_layout.addWidget(self.file_label)
        v_layout.addWidget(self.file_input)
        v_layout.addWidget(self.browse_button)
        v_layout.addWidget(self.encrypt_button)
        v_layout.addWidget(self.decrypt_button)
        self.setLayout(v_layout)
        # set window properties
        self.setWindowTitle('Xipher')
        self.setGeometry(300, 300, 300, 150)
        # connect signals to slots
        self.browse_button.clicked.connect(self.browse_file)
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

    def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            self.file_input.setText(file_name)

    def encrypt(self):
        password = self.password_input.text()
        if password and self.file_input.text():
            key = create_key(password.encode())
            encrypt_file(key, self.file_input.text())
            self.file_input.setText(self.file_input.text() + '.enc')

    def decrypt(self):
        password = self.password_input.text()
        if password and self.file_input.text():
            key = create_key(password.encode())
            decrypt_file(key, self.file_input.text())
            self.file_input.setText(self.file_input.text().replace('.enc',''))

# create pyqt5 app and show the gui
app = QApplication([])
gui = FileCryptoGUI()
gui.show()
app.exec_()