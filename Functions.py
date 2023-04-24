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
        self.setStyleSheet(Helper.read_file('StyleSheet.qss'))
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
        self.rotation_x.valueChanged.connect(self.rotation_x_function)
        self.rotation_y.valueChanged.connect(self.rotation_y_function)
        self.rotation_z.valueChanged.connect(self.rotation_z_function)

        # Sliders
        self.location_x.valueChanged.connect(self.location_x_function)
        self.location_y.valueChanged.connect(self.location_y_function)
        self.location_z.valueChanged.connect(self.location_z_function)

        self.scale_x.valueChanged.connect(self.scale_x_function)
        self.scale_y.valueChanged.connect(self.scale_y_function)
        self.scale_z.valueChanged.connect(self.scale_z_function)

        # Checkboxes
        self.checkbox_1.clicked.connect(self.checkbox_1_function)
        self.checkbox_2.clicked.connect(self.checkbox_2_function)
        self.checkbox_3.clicked.connect(self.checkbox_3_function)
        self.checkbox_4.clicked.connect(self.checkbox_4_function)

# The functions that run when the controls are used:
# Title Bar Functions
    def close_button_function(self):
        self.close()

    def maximize_button_function(self):
        self.showFullScreen()

    def minimize_button_function(self):
        self.showMinimized()

# Nav Bar Functions
    # Show the screen of the button that was clicked
    # Hide all other screens
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

# Location Slider Functions
    def location_x_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.location[0] = self.location_x.value()

    def location_y_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.location[1] = self.location_y.value()

    def location_z_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.location[2] = self.location_z.value()

# Rotation Dial Functions
    def rotation_x_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                value = self.rotation_x.value() * 0.01745329
                object.rotation_euler[0] = (value)

    def rotation_y_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                value = self.rotation_y.value() * 0.01745329
                object.rotation_euler[1] = (value)

    def rotation_z_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                value = self.rotation_z.value() * 0.01745329
                object.rotation_euler[2] = (value)

# Scale Slider Functions
    def scale_x_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.scale[0] = self.scale_x.value()

    def scale_y_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.scale[1] = self.scale_y.value()

    def scale_z_function(self):
        for object in bpy.context.scene.objects:
            if object.select_get():
                object.scale[2] = self.scale_z.value()

# Checkbox Functions
    def checkbox_1_function(self):
        for screen in bpy.data.screens:
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        box = self.checkbox_1
                        space.overlay.show_overlays = box.isChecked()

    def checkbox_2_function(self):
        for screen in bpy.data.screens:
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        space.show_gizmo = self.checkbox_2.isChecked()

    def checkbox_3_function(self):
        settings = bpy.context.scene.tool_settings
        settings.use_snap = self.checkbox_3.isChecked()

    def checkbox_4_function(self):
        settings = bpy.context.scene.tool_settings
        settings.use_proportional_edit_objects = self.checkbox_4.isChecked()


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
