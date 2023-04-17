import bpy
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QPoint, Qt
from .UI import Addon_UI, bl_info
from .core import QtWindowEventLoop, Helper


class Addon_Functions(Addon_UI, QDialog):
    def __init__(self):
        super(Addon_Functions, self).__init__()
        self.setWindowTitle(bl_info['name'])
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(Helper.read_file('Style.qss'))
        self.show()
        self.connect_functions()

# Allows our frameless window to be clicked and dragged
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

# Moves the frameless window to the mouse cursor location
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# Connects the UI controls to their functions
    def connect_functions(self):
        # Buttons
        self.close_button.clicked.connect(self.close_button_function)
        self.maximize_button.clicked.connect(self.maximize_button_function)
        self.minimize_button.clicked.connect(self.minimize_button_function)

        self.home_button.clicked.connect(self.home_button_function)
        self.settings_button.clicked.connect(self.settings_button_function)
        self.docs_button.clicked.connect(self.docs_button_function)
        self.info_button.clicked.connect(self.info_button_function)

        # Dials
        self.dial_x.valueChanged.connect(self.dial_x_function)
        self.dial_y.valueChanged.connect(self.dial_y_function)
        self.dial_z.valueChanged.connect(self.dial_z_function)

# The functions that run when the controls are used:
# Title Bar Functions
    def close_button_function(self):
        self.close()

    def maximize_button_function(self):
        self.showFullScreen()

    def minimize_button_function(self):
        self.showMinimized()

    def home_button_function(self):
        self.home.show()
        self.settings.hide()
        self.info.hide()
        self.docs.hide()

    def settings_button_function(self):
        self.settings.show()
        self.home.hide()
        self.info.hide()
        self.docs.hide()

    def docs_button_function(self):
        self.docs.show()
        self.settings.hide()
        self.home.hide()
        self.info.hide()

    def info_button_function(self):
        self.info.show()
        self.settings.hide()
        self.home.hide()
        self.docs.hide()

# Rotation Dial Functions
    def dial_x_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.rotation_euler[0] = (self.dial_x.value() * 0.01745329)

    def dial_y_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.rotation_euler[1] = (self.dial_y.value() * 0.01745329)

    def dial_z_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.rotation_euler[2] = (self.dial_z.value() * 0.01745329)


class CustomWindowOperator(QtWindowEventLoop):
    bl_idname = 'screen.custom_window'
    bl_label = bl_info['name']

    def __init__(self):
        super().__init__(Addon_Functions)


class AddonQtPanel(bpy.types.Panel):
    bl_label = bl_info['name']
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BpySide6'

    def draw(self, context):
        layout = self.layout
        layout.operator('screen.custom_window')
