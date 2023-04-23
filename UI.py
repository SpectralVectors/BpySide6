from PySide6.QtWidgets import (
    QDialog, QLabel, QPushButton, QDial, QWidget, QVBoxLayout, QGridLayout,
    QHBoxLayout, QSlider, QTableWidgetItem, QCheckBox, QFrame, QTextEdit)
from PySide6.QtCore import Qt, QSize
import qtawesome as qta
from . import resources_rc
from .core import Helper

bl_info = {
    'name': 'BpySide6',
    'author': 'Frieder Erdmann, Rajiv Sharma, Spectral Vectors',
    'description': 'Advanced PySide GUI for Blender Addons',
    'blender': (2, 80, 0),
    'version': (0, 0, 3),
    'location': 'N Panel > BpySide6',
    'warning': 'Under Development',
    'category': 'Generic'
}

'''
The Addon UI is divided into 3 primary sections:

1 - Title Bar - logo, title, window controls
2 - Nav Menu - home, settings and info buttons
3 - Main Area - Home, Settings, Docs, and Info Pages

The Main Area will display a different Page based on
the Nav buttons.
Each section is created, then added to the parent layout
at the bottom.

The Title Bar demonstrates a design pattern, and the same
pattern repeats for all other sections:
A Frame contains a layout which contains a series of Widgets,
Some of which are buttons, dials, sub-frames or sub-layouts.
'''


class Addon_UI(QDialog):
    def __init__(self, parent=None):
        super(Addon_UI, self).__init__(parent)

        # Shortcuts for alignment flags
        Top = Qt.AlignmentFlag.AlignTop
        Left = Qt.AlignmentFlag.AlignLeft
        Right = Qt.AlignmentFlag.AlignRight
        Center = Qt.AlignmentFlag.AlignCenter

        # The size of the Window
        self.setFixedSize(600, 400)

        # addon will be the parent container for all other widgets
        self.addon = QWidget()
        # addon layout will arrange all widgets according to its alignment flag
        self.addon_layout = QHBoxLayout(self.addon)
        self.addon_layout.setAlignment(Top | Left)

# Title Bar - starts
        # Create a Frame called title_bar that belongs to the parent: addon
        self.title_bar = QFrame(self.addon)
        # Set the Frame style
        self.title_bar.setFrameStyle(QFrame.NoFrame)
        # Set the max height to accomodate a 24x24 button with padding
        self.title_bar.setMaximumHeight(42)
        # Logo
        self.logo = QLabel()
        # Settings ObjectName allows us to refer to this button
        # individually in th stylesheet
        self.logo.setObjectName('logo')
        # Title
        self.title = QLabel(text=bl_info['name'])
        self.title.setObjectName('title')
        # Close Button
        # Using a QtAwesome Icon from the Phosphor icon set
        close_icon = qta.icon('ph.x')
        self.close_button = QPushButton(icon=close_icon)
        self.close_button.setObjectName('close_button')
        # Maximize Button
        maximize_icon = qta.icon('ph.arrows-out-simple')
        self.maximize_button = QPushButton(icon=maximize_icon)
        self.maximize_button.setObjectName('maximize_button')
        # Minimize Button
        minimize_icon = qta.icon('ph.minus')
        self.minimize_button = QPushButton(icon=minimize_icon)
        self.minimize_button.setObjectName('minimize_button')
        # Sublayout for window controls - maximize, minimize, close
        # Horizontal Box with Top Right Alignment
        window_controls = QHBoxLayout()
        window_controls.setAlignment(Top | Right)
        window_controls.addWidget(self.minimize_button)
        window_controls.addWidget(self.maximize_button)
        window_controls.addWidget(self.close_button)
        # Layout for all elements - logo, title and window controls
        title_bar_layout = QHBoxLayout(self.title_bar)
        title_bar_layout.setAlignment(Top)
        title_bar_layout.addWidget(self.logo)
        title_bar_layout.addWidget(self.title)
        title_bar_layout.addLayout(window_controls)
# Title Bar - ends

# Nav Menu - starts
        self.nav_menu = QFrame(self.addon)
        self.nav_menu.setFrameStyle(QFrame.NoFrame)
        self.nav_menu_layout = QVBoxLayout(self.nav_menu)
        self.nav_menu_layout.setAlignment(Top | Left)
        # Home Button
        self.home_button = QPushButton(icon=qta.icon('ph.house'))
        self.home_button.setToolTip('Home')
        self.home_button.setObjectName('home')
        self.home_button.setIconSize(QSize(48, 48))
        # Settings Button
        self.settings_button = QPushButton(icon=qta.icon('ph.faders'))
        self.settings_button.setToolTip('Settings')
        self.settings_button.setObjectName('settings')
        self.settings_button.setIconSize(QSize(48, 48))
        # Docs Button
        self.docs_button = QPushButton(icon=qta.icon('ph.file-text'))
        self.docs_button.setToolTip('Docs')
        self.docs_button.setObjectName('docs')
        self.docs_button.setIconSize(QSize(48, 48))
        # Info Button
        self.info_button = QPushButton(icon=qta.icon('ph.info'))
        self.info_button.setToolTip('Info')
        self.info_button.setObjectName('info')
        self.info_button.setIconSize(QSize(48, 48))
        # Add widgets to navigation menu
        self.nav_menu_layout.addWidget(self.home_button)
        self.nav_menu_layout.addWidget(self.settings_button)
        self.nav_menu_layout.addWidget(self.docs_button)
        self.nav_menu_layout.addWidget(self.info_button)
# Nav Menu - ends

# Main Area - starts
    # Home Screen
        self.home = QFrame(self.addon)
        self.home_layout = QVBoxLayout(self.home)

        # Location
        self.location_frame = QFrame(self.home)
        # self.location_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.location_layout = QHBoxLayout(self.location_frame)
        self.location_label = QLabel(text='Location: ')
        location_sliders = []
        self.location_x = QSlider()
        self.location_x.setObjectName('location_x')
        location_sliders.append(self.location_x)
        self.location_y = QSlider()
        self.location_y.setObjectName('location_y')
        location_sliders.append(self.location_y)
        self.location_z = QSlider()
        self.location_z.setObjectName('location_z')
        location_sliders.append(self.location_z)
        for slider in location_sliders:
            slider.setSingleStep(0.1)
            slider.setMinimum(-100)
            slider.setMaximum(100)
            slider.setOrientation(Qt.Horizontal)
        self.location_layout.addWidget(self.location_label)
        self.location_layout.addWidget(self.location_x)
        self.location_layout.addWidget(self.location_y)
        self.location_layout.addWidget(self.location_z)
        self.home_layout.addWidget(self.location_frame)

        # Rotation
        self.rotation_frame = QFrame(self.home)
        # self.rotation_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.rotation_layout = QHBoxLayout(self.rotation_frame)
        self.rotation_label = QLabel(text='Rotation: ')
        rotation_dials = []
        self.dial_x = QDial()
        self.dial_x.setObjectName('dial_x')
        rotation_dials.append(self.dial_x)
        self.dial_y = QDial()
        self.dial_y.setObjectName('dial_y')
        rotation_dials.append(self.dial_y)
        self.dial_z = QDial()
        self.dial_z.setObjectName('dial_z')
        rotation_dials.append(self.dial_z)
        for dial in rotation_dials:
            dial.setSingleStep(0.01745329)
            dial.setRange(0, 360)
            dial.setMinimumWidth(120)
        self.rotation_layout.addWidget(self.rotation_label)
        self.rotation_layout.addWidget(self.dial_x)
        self.rotation_layout.addWidget(self.dial_y)
        self.rotation_layout.addWidget(self.dial_z)
        self.home_layout.addWidget(self.rotation_frame)

        # Scale
        self.scale_frame = QFrame(self.home)
        # self.scale_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.scale_layout = QHBoxLayout(self.scale_frame)
        self.scale_label = QLabel(text='Scale: ')
        scale_sliders = []
        self.scale_x = QSlider()
        self.scale_x.setObjectName('scale_x')
        scale_sliders.append(self.scale_x)
        self.scale_y = QSlider()
        self.scale_y.setObjectName('scale_y')
        scale_sliders.append(self.scale_y)
        self.scale_z = QSlider()
        self.scale_z.setObjectName('scale_z')
        scale_sliders.append(self.scale_z)
        for slider in scale_sliders:
            slider.setSingleStep(0.1)
            slider.setMinimum(0.1)
            slider.setMaximum(10)
            slider.setMinimumWidth(150)
        self.scale_layout.addWidget(self.scale_label)
        self.scale_layout.addWidget(self.scale_x)
        self.scale_layout.addWidget(self.scale_y)
        self.scale_layout.addWidget(self.scale_z)
        self.home_layout.addWidget(self.scale_frame)

    # Settings Screen
        self.settings = QFrame(self.addon)
        self.settings_layout = QGridLayout(self.settings)
        self.settings_label = QLabel(text='Settings')
        self.checkbox_1 = QCheckBox('Option 1', self.settings)
        self.checkbox_2 = QCheckBox('Option 2', self.settings)
        self.checkbox_3 = QCheckBox('Option 3', self.settings)
        self.checkbox_4 = QCheckBox('Option 4', self.settings)
        self.settings_layout.addWidget(self.settings_label, 0, 0)
        self.settings_layout.addWidget(self.checkbox_1, 1, 1)
        self.settings_layout.addWidget(self.checkbox_2, 1, 2)
        self.settings_layout.addWidget(self.checkbox_3, 2, 1)
        self.settings_layout.addWidget(self.checkbox_4, 2, 2)
        self.settings.hide()

    # Docs Screen
        self.docs = QFrame(self.addon)
        self.docs_layout = QHBoxLayout(self.docs)
        self.readme = QTextEdit()
        path = Helper.absolute_path('README.md')
        with open(path, encoding="utf-8") as f:
            markdown = f.read()
        self.readme.setMarkdown(markdown)
        self.docs_layout.addWidget(self.readme)
        self.docs.hide()

    # Info Screen
        self.info = QFrame(self.addon)
        self.info_layout = QGridLayout(self.info)
        vertical_labels = [
            'Name',
            'Author',
            'Description',
            'Blender Version',
            'Addon Version',
            'Location',
            'Warning',
            'Category']
        v_labels = []
        user_labels = []
        count = 0
        for i in vertical_labels:
            self.i = QLabel(text=f"{vertical_labels[count]}:")
            self.i.setMinimumHeight(24)
            self.i.setStyleSheet('font: bold;')
            self.info_layout.addWidget(self.i, count, 0, Right)
            v_labels.append(self.i)
            count += 1
        count = 0
        for i in bl_info:
            self.i = QLabel(text=str(bl_info[i]))
            self.i.setMinimumHeight(24)
            user_labels.append(self.i)
            self.info_layout.addWidget(self.i, count, 1, Left)
            count += 1
        # count = 0
        # for i in v_labels:
        #     self.info_layout.addWidget(v_labels[count])
        #     self.info_layout.addWidget(user_labels[count])
        #     count += 1
        self.info.hide()

        # Create a frame to hold all the controls for the main area
        self.addon_controls = QFrame(self.addon)
        self.addon_controls_layout = QHBoxLayout(self.addon_controls)
        self.addon_controls_layout.setAlignment(Center)

        # Add each frame widget we created above
        self.addon_controls_layout.addWidget(self.home)
        self.addon_controls_layout.addWidget(self.settings)
        self.addon_controls_layout.addWidget(self.docs)
        self.addon_controls_layout.addWidget(self.info)

        # Add the navigation menu and the main area to the addon area
        self.addon_layout.addWidget(self.nav_menu)
        self.addon_layout.addWidget(self.addon_controls)
# Main Area - ends

# Parent Addon Layout - starts
        layout = QVBoxLayout()
        layout.setAlignment(Top)
        layout.addWidget(self.title_bar)
        layout.addWidget(self.addon)

        self.setLayout(layout)
# Parent Addon Layout - ends
