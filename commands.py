"""
Commands for graphical interface.

Created on 12.04.2019

@author: Ruslan Dolovanyuk

"""

from dialogs import About

from extrows import ExtRows


class Commands:
    """Helper class, contains command for bind events, menu and buttons."""

    def __init__(self, drawer):
        """Initilizing commands class."""
        self.drawer = drawer

        self.masks = []
        self.rows = None

    def log_browse(self, event):
        """Change file log."""
        self.drawer.path = self.drawer.log_ctrl.GetPath()
        if self.drawer.path != '':
            self.drawer.but_load.Enable()

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

    def load_log(self, event):
        """Load log data in traces control."""
        with open(self.drawer.path, 'r', encoding="utf-8") as log_file:
            for row in log_file:
                if self.rows is None:
                    self.rows = ExtRows(row)
                else:
                    self.rows.add(row)
            self.drawer.data.SetValue(self.rows.get_rows())
        self.drawer.but_load.Disable()

    def add_exception(self, event):
        """Add exception to masks list."""
        subrow = self.drawer.mask.GetValue()
        self.masks.append(subrow)
        self.drawer.masks.Set(self.masks)
        self.drawer.mask.SetValue('')
        self.rows.change(subrow, True)
        position = self.drawer.data.GetInsertionPoint()
        self.drawer.data.SetValue(self.rows.get_rows())
        self.drawer.data.SetInsertionPoint(position)

    def del_exception(self, event):
        """Remove mask from list masks."""
        index = self.drawer.masks.GetSelection()
        subrow = self.masks.pop(index)
        self.drawer.masks.Set(self.masks)
        self.drawer.but_del_exception.Disable()
        self.rows.change(subrow, False)
        position = self.drawer.data.GetInsertionPoint()
        self.drawer.data.SetValue(self.rows.get_rows())
        self.drawer.data.SetInsertionPoint(position)
