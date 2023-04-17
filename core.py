import sys
import os
import logging
import bpy

from PySide6 import QtWidgets, QtCore

logger = logging.getLogger('qtutils')


class QtWindowEventLoop(bpy.types.Operator):
    """Allows PyQt or PySide to run inside Blender"""

    bl_idname = 'screen.qt_event_loop'
    bl_label = 'Qt Event Loop'

    def __init__(self, widget, *args, **kwargs):
        self._widget = widget
        self._args = args
        self._kwargs = kwargs

    # modal is the loop that runs while the window is open, allowing
    # commands to pass from the PySide window into Blender
    def modal(self, context, event):
        wm = context.window_manager

        # If the widget is closed, end the loop
        if not self.widget.isVisible():
            logger.debug('Finished modal operator')
            wm.event_timer_remove(self._timer)
            return {'FINISHED'}
        # Otherwise, pass events from PySide to Blender
        else:
            logger.debug('Process the events for Qt window')
            self.event_loop.processEvents()
            self.app.sendPostedEvents(None, 0)

        return {'PASS_THROUGH'}

    def execute(self, context):
        logger.debug('execute operator')

        # Using an instance allows you to have multiple windows open,
        # and close them individually
        self.app = QtWidgets.QApplication.instance()

        # If there is not already an instance, then create the first one
        if not self.app:
            self.app = QtWidgets.QApplication(sys.argv)

        self.app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

        if 'stylesheet' in self._kwargs:
            stylesheet = self._kwargs['stylesheet']
            self.set_stylesheet(self.app, stylesheet)

        self.event_loop = QtCore.QEventLoop()
        self.widget = self._widget(*self._args, **self._kwargs)

        logger.debug(self.app)
        logger.debug(self.widget)

        # Run the modal loop
        wm = context.window_manager
        self._timer = wm.event_timer_add(1 / 120, window=context.window)
        context.window_manager.modal_handler_add(self)

        return {'RUNNING_MODAL'}

    def set_stylesheet(self, app, filepath):
        file_qss = QtCore.QFile(filepath)
        if file_qss.exists():
            file_qss.open(QtCore.QFile.ReadOnly)
            stylesheet = QtCore.QTextStream(file_qss).readAll()
            app.setStyleSheet(stylesheet)
            file_qss.close()


class Helper:
    """Collection of helper functions for working with local files"""

    @staticmethod
    def read_file(file):
        scriptpath = os.path.dirname(__file__)
        file_path = os.path.join(scriptpath, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def absolute_path(file):
        scriptpath = os.path.dirname(__file__)
        file_path = os.path.join(scriptpath, file)
        return file_path
