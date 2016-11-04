'''
    @Author Gustavo García

    Build a QMessageBox component. You can 
    use method chaining for set properties
    on it.

    There is three states of levels:

    [+] info: traduces to QMessageBox.Information
    [+] warn: traduces to QMessageBox.Warning
    [+] error: traduces to QMessageBox.Critical
'''

from PyQt5.QtWidgets import QMessageBox


class Message:

    def __init__(self):
        self.init_ui()

    def init_ui(self):
        self.box = QMessageBox()
        self.box.setStandardButtons(QMessageBox.Close)
        self.box.setEscapeButton(QMessageBox.Close)

    def level(self, name):
        if name == "info":
            icon = QMessageBox.Information
        if name == "warn":
            icon = QMessageBox.Warning
        if name == "error":
            icon = QMessageBox.Critical
        
        self.box.setIcon(icon)
        return self

    def title(self, text):
        self.box.setWindowTitle(text)
        return self

    def message(self, text):
        self.box.setText(text)
        return self

    def show(self):
        self.box.exec_()