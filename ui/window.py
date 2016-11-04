"""
    @Author Gustavo García

    Parent window of the application. This class use
    any exsitent translator. Default one is Yandex.
"""

from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget,
    QGridLayout, QHBoxLayout,
    QVBoxLayout, QPushButton,
    QTextEdit, QComboBox,
    QLabel, QFrame
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from core.translator import Translator
from ui.message import Message


class Window (QWidget):

    def __init__(self):
        super().__init__()
        self.init_translator()
        self.init_ui()
        self.init_layouts()
        self.add_widgets()
        self.configure_widgets()
        self.bind_events()
        self.apply_styles()
        self.configure_window()
        self.source_txt.setFocus() # set focus on focus area
        self._from = "" # init origin language variable
        self._to = "" # init target language variable

    def init_ui(self):
        # langugage  comboboxes
        self.origin_lang_cbo = QComboBox(self)
        self.target_lang_cbo = QComboBox(self)
        # text boxes
        self.source_txt = QTextEdit()
        self.output_txt = QTextEdit()
        # clear buttons
        self.clear_btn = QPushButton("Clear")
        self.translate_btn = QPushButton("Translate")
        # providers buttons
        self.yandex_btn = QPushButton()
        self.google_btn = QPushButton()
        self.microsoft_btn = QPushButton()
        # status panel widgets
        self.frame = QFrame()
        self.status_icon = QPushButton()
        self.status_lbl = QLabel("Using Yandex provider")

    def init_layouts(self):
        self.main_lyt = QVBoxLayout()
        self.content_lyt = QHBoxLayout()
        self.content_left_lyt = QVBoxLayout()
        self.content_right_lyt = QVBoxLayout()
        self.action_lyt = QHBoxLayout()
        self.providers_lyt = QHBoxLayout()
        self.buttons_lyt = QHBoxLayout()
        self.status_panel_lyt = QHBoxLayout()
        # layout order
        self.main_lyt.addLayout(self.content_lyt)
        self.main_lyt.addLayout(self.action_lyt)
        self.content_lyt.addLayout(self.content_left_lyt)
        self.content_lyt.addLayout(self.content_right_lyt)
        self.content_lyt.setContentsMargins(10, 10, 10, 0)
        self.action_lyt.addLayout(self.providers_lyt)
        self.action_lyt.addLayout(self.buttons_lyt)
        self.action_lyt.setContentsMargins(10, 0, 10, 0)
        self.providers_lyt.setAlignment(Qt.AlignLeft)
        self.main_lyt.addWidget(self.frame)
        # set main_lyt as defalt layout
        self.main_lyt.setSpacing(15)
        self.main_lyt.setContentsMargins(0, 0, 0, 0)
        self.status_panel_lyt.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.main_lyt)

    def add_widgets(self):
        self.content_left_lyt.addWidget(self.origin_lang_cbo)
        self.content_left_lyt.addWidget(self.source_txt)
        self.content_right_lyt.addWidget(self.target_lang_cbo)
        self.content_right_lyt.addWidget(self.output_txt)
        self.providers_lyt.addWidget(self.yandex_btn)
        self.providers_lyt.addWidget(self.google_btn)
        self.providers_lyt.addWidget(self.microsoft_btn)
        self.buttons_lyt.addWidget(self.clear_btn)
        self.buttons_lyt.addWidget(self.translate_btn)
        self.status_panel_lyt.addWidget(self.status_icon)
        self.status_panel_lyt.addWidget(self.status_lbl)

    def configure_widgets(self):
        # configure text boxes
        self.source_txt.setPlaceholderText("Write something...")
        self.source_txt.setObjectName("input")
        self.output_txt.setReadOnly(True)
        self.output_txt.setObjectName("output")
        # add size and object names to action buttons
        self.clear_btn.setObjectName("clear")
        self.clear_btn.setMaximumWidth(100)
        self.translate_btn.setObjectName("translate")
        self.translate_btn.setMaximumWidth(100)
        # fill comboboxes with languages
        self.origin_lang_cbo.addItem("- Origin lang -")
        self.origin_lang_cbo.setObjectName("origin-lang")
        self.origin_lang_cbo.setMaximumWidth(120)
        self.target_lang_cbo.addItem("- Target lang -")
        self.target_lang_cbo.setObjectName("target-lang")
        self.target_lang_cbo.setMaximumWidth(120)
        for (key, val) in self.langs.items():
            self.origin_lang_cbo.addItem(val, key)
            self.target_lang_cbo.addItem(val, key)
        # set size, object names and icons to providers buttons
        self.yandex_btn.setMaximumWidth(30)
        self.yandex_btn.setMaximumHeight(25)
        self.yandex_btn.setObjectName("yandex")
        self.yandex_btn.setIcon(QIcon("resources/img/yandex.png"))
        self.google_btn.setMaximumWidth(30)
        self.google_btn.setMaximumHeight(25)
        self.google_btn.setObjectName("google")
        self.google_btn.setIcon(QIcon("resources/img/google.png"))
        self.microsoft_btn.setMaximumWidth(30)
        self.microsoft_btn.setMaximumHeight(25)
        self.microsoft_btn.setObjectName("microsoft")
        self.microsoft_btn.setIcon(QIcon("resources/img/microsoft.png"))
        # configure size of status panel icon
        self.frame.setLayout(self.status_panel_lyt)
        self.frame.setObjectName("status-panel")
        self.status_icon.setMaximumWidth(30)
        self.status_icon.setMaximumHeight(30)
        self.status_icon.setObjectName("status-icon")
        self.status_icon.setIcon(QIcon("resources/img/smile.png"))
        self.status_lbl.setObjectName("status-lbl")
        # cause default provider is Yandex
        self.yandex_btn.setStyleSheet("border-color: #2980b9")

    def bind_events(self):
        # bind events
        self.origin_lang_cbo.activated.connect(self.origin_lang_changed)
        self.target_lang_cbo.activated.connect(self.target_lang_changed)
        self.clear_btn.clicked.connect(self.clear_boxes)
        self.translate_btn.clicked.connect(self.translate)
        self.yandex_btn.clicked.connect(self.provider_changed)
        self.google_btn.clicked.connect(self.provider_changed)
        self.microsoft_btn.clicked.connect(self.provider_changed)

    def configure_window(self):
        self.resize(550, 310)
        self.setWindowTitle("Pybabel ~ Translation Service")
        self.setWindowIcon(QIcon("resources/img/logo.png"))
        self.center_on_screen()
        self.show()

    # center window on screen
    def center_on_screen(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def apply_styles(self):
        with open("resources/css/window.css") as f:
            self.setStyleSheet(f.read())

    """
        Initialize the translator and fetch de langs. Default
        translator is Yandex.
    """
    def init_translator(self):
        try:
            self.translator = Translator()
            self.translator.set_provider("yandex")
            self.langs = self.translator.get_langs()
        except Exception as e:
            message = Message()
            message.level("error") \
                    .title("Error on start") \
                    .message(str(e)) \
                    .show()
            quit()

    """
        Listen for the combos events. Stores the _from variable that
        contains the shorthand lang to pass to the translator.
        If selected index is 0, that means that the user selected the
        "- Select -" option.
    """
    def origin_lang_changed(self, index):
        if index == 0:
            self._from = ""
        else:
            self._from = self.origin_lang_cbo.itemData(index)

    """
        Listen for the combos events. Stores the _to variable that
        contains the shorthand lang to pass to the translator.
        If selected index is 0, that means that the user selected the
        "- Select -" option.
    """
    def target_lang_changed(self, index):
        if index == 0:
            self._to = ""
        else:
            self._to = self.target_lang_cbo.itemData(index)

    """
        Listen for buttons events.
    """
    def clear_boxes(self):
        self.source_txt.clear()
        self.output_txt.clear()
        self.source_txt.setFocus()

    """
        Set a new provider
    """
    def provider_changed(self):
        self.yandex_btn.setStyleSheet("border-color: transparent")
        self.google_btn.setStyleSheet("border-color: transparent")
        self.microsoft_btn.setStyleSheet("border-color: transparent")
        self.sender().setStyleSheet("border-color: #2980b9")
        new_provider = self.sender().objectName().capitalize()
        # update the new provider on translator object
        if new_provider == "Yandex":
            self.translator.set_provider("yandex")
        elif new_provider == "Google":
            self.translator.set_provider("google")
        elif new_provider == "Microsoft":
            self.translator.set_provider("microsoft")
        # update the provider name on the status label
        self.status_lbl.setText("Using %s provider" % new_provider)

    """
        Request the translation. First check that is a
        valid request:

        [+] Origin lang must be selected
        [+] Target lang must be selected
        [+] Entry text area must be filled.

        If any of these requirements is missing, a message
        box will be displayed reporting the issue.
    """
    def translate(self):
        text = self.source_txt.toPlainText()
        message = Message()

        if text == "":
            message.level("warn") \
                    .title("Can't translate") \
                    .message("You need to write something!") \
                    .show()
            return
        if self._from == "":
            message.level("warn") \
                    .title("Can't translate") \
                    .message("Choose a source language") \
                    .show()
            return
        if self._to == "":
            message.level("warn") \
                    .title("Can't translate") \
                    .message("Choose a target language") \
                    .show()
            return

        try:
            translated = self.translator.translate(
                            text, self._from, self._to)
            self.output_txt.setPlainText(translated)
        except Exception as e:
            message.level("error") \
                    .title("Something wrong happen") \
                    .message(str(e)) \
                    .show()
