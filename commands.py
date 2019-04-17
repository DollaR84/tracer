"""
Commands for graphical interface.

Created on 12.04.2019

@author: Ruslan Dolovanyuk

"""

from dialogs import About


class Commands:
    """Helper class, contains command for bind events, menu and buttons."""

    def __init__(self, drawer):
        """Initilizing commands class."""
        self.drawer = drawer

        self.masks = []
        self.rows = []
        self.hide_flags = []

    def log_browse(self, event):
        """Change file log."""
        self.drawer.path = self.drawer.log_ctrl.GetPath()

    def about(self, event):
        """Run about dialog."""
        About(self.drawer,
              'О программе...',
              'Tracer - просмотрщик логов',
              '1.0',
              'Руслан Долованюк').ShowModal()

    def close(self, event):
        """Close event for button close."""
        self.drawer.Close(True)

    def close_window(self, event):
        """Close window event."""
        self.drawer.Destroy()

    def edit_mask(self, event):
        """Edit mask in mask field."""
        if self.drawer.mask.GetValue() == '':
            self.drawer.but_add_exception.Disable()
        else:
            self.drawer.but_add_exception.Enable()

    def sel_mask(self, event):
        """Select mask in masks list."""
        self.drawer.but_del_exception.Enable()

    def add_exception(self, event):
        """Add exception to masks list."""
        pass

    def del_exception(self, event):
        """Remove mask from list masks."""
        pass