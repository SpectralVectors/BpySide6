# BpySide6
Advanced Addon Interface for Blender, powered by PySide6 and QtAwesome

![BpySide6](/BpySide6.png)

__This Addon is under development. It relies on PySide6 and QtAwesome, but does not yet install those dependencies for you!__
## What Is It?
Rajiv Sharma (VFX Pipeline) and Frieder Erdmann created and streamlined the process of using PySide2 inside of Blender to create more advanced user interfaces for addons.

This addon updates their work to PySide6, and offers a template that is compatible with Blender 3 and up!

## What Does It Do?
This allows you to use images for your addon background, buttons etc. 

As well as custom solid colors or gradients per button, title etc.

Pyside6 also supports customizable dials for rotary control, as well as sliders, in addition to the standard push buttons, radio buttons, checkboxes and more!

There is a Stylesheet to allow global styling, or customizing individual elements.

Images are packed into a resources_rc.py data file to ensure compatibility and portability.

QtAwesome provides icon sets from FontAwesome, Elusive, Material Design, Phosphor, Remix and Microsoft Codicons.

## File structure
```
+ BpySide6/
| 
+ images/
|           The background and logo images are here in png format
+-- __init__.py
|           register() and unregister() are in here (Blender addon initialization)
+-- core.py
|           QtEventLoop() (this is the most important part)
+-- UI.py
|           The visual layout of the Addon window
+-- Functions.py
|           Linking the UI controls to functions and Operators in Blender
+-- Style.qss
|           Stylesheet for the Addon
+-- resources.qrc
|           List of resources used in the addon (images in this case)
+-- resources_rc.py
|           Our resources compiled into a .py data file
```     

## Remarks on structure
* The entire setup is a self contained addon.
  * In actual production, it would make sense to put the core.py contents into a module, rather than one specific addon, so other operators can also inherit from it.

## Inner workings
The main content here is the QtWindowEventLoop in core.py, which inherits the Blender operator and sets up modal execution with a QEventLoop that is triggered at 120Hz by Blender's window manager.

The actual tool is the Addon_UI, (originally inheriting the Ui_Form class, created by Qt designer, simplified here) and QDialog.

The only Blender UI element is AddonQtPanel (a regular bpy panel), containing the CustomWindowOperator as a UI button. The CustomWindowOperator is a QtWindowEventLoop Operator. It launches the eventloop and the (Qt) AddonWindow.

## Special Thanks
__Rajiv Sharma__ did all the difficult work on this, and graciously shared his knowledge in his VFX Pipeline video (see link at the top of this document). 

Frieder Erdmann contributed to layout, structure and documentation.
