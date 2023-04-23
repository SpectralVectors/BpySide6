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
    'version': (0, 0, 4),
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
        HCenter = Qt.AlignmentFlag.AlignHCenter

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
        self.home.setMinimumSize(450, 280)
        self.home_layout = QGridLayout(self.home)

        # Location
        self.location_label = QLabel(text='Location: ')
        self.location_label.setObjectName('location_label')
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
            slider.setSingleStep(0.01)
            slider.setMinimum(-50)
            slider.setMaximum(50)
            slider.setOrientation(Qt.Horizontal)

        # Rotation
        self.rotation_label = QLabel(text='Rotation: ')
        self.rotation_label.setObjectName('rotation_label')
        rotation_dials = []
        self.rotation_x = QDial()
        self.rotation_x.setObjectName('rotation_x')
        rotation_dials.append(self.rotation_x)
        self.rotation_y = QDial()
        self.rotation_y.setObjectName('rotation_y')
        rotation_dials.append(self.rotation_y)
        self.rotation_z = QDial()
        self.rotation_z.setObjectName('rotation_z')
        rotation_dials.append(self.rotation_z)
        for dial in rotation_dials:
            dial.setSingleStep(0.01745329)
            dial.setRange(0, 360)

        # Scale
        self.scale_label = QLabel(text='Scale: ')
        self.scale_label.setObjectName('scale_label')
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

        self.home_layout.addWidget(self.location_label, 0, 0, Center)
        self.home_layout.addWidget(self.location_x, 0, 1, Center)
        self.home_layout.addWidget(self.location_y, 0, 2, Center)
        self.home_layout.addWidget(self.location_z, 0, 3, Center)

        self.home_layout.addWidget(self.rotation_label, 1, 0, Center)
        self.home_layout.addWidget(self.rotation_x, 1, 1, Center)
        self.home_layout.addWidget(self.rotation_y, 1, 2, Center)
        self.home_layout.addWidget(self.rotation_z, 1, 3, Center)

        self.home_layout.addWidget(self.scale_label, 2, 0, Center)
        self.home_layout.addWidget(self.scale_x, 2, 1, Center)
        self.home_layout.addWidget(self.scale_y, 2, 2, Center)
        self.home_layout.addWidget(self.scale_z, 2, 3, Center)

    # Settings Screen
        self.settings = QFrame(self.addon)
        self.settings.setMinimumSize(450, 120)
        self.settings_layout = QVBoxLayout(self.settings)
        self.settings_layout.setAlignment(Top | HCenter)
        self.settings_label = QLabel(text='Settings')
        self.settings_label.setObjectName('settings_label')
        self.checkbox_1 = QCheckBox('Show Overlays', self.settings)
        self.checkbox_1.setCheckState(Qt.Checked)
        self.checkbox_2 = QCheckBox('Show Nav Gizmos', self.settings)
        self.checkbox_2.setCheckState(Qt.Checked)
        self.checkbox_3 = QCheckBox('Enable Snapping', self.settings)
        self.checkbox_4 = QCheckBox('Enable Proportional Editing', self.settings)
        self.settings_layout.addWidget(self.settings_label)
        self.settings_layout.addWidget(self.checkbox_1)
        self.settings_layout.addWidget(self.checkbox_2)
        self.settings_layout.addWidget(self.checkbox_3)
        self.settings_layout.addWidget(self.checkbox_4)
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
