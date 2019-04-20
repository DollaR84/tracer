"""
Graphical form for tracer.

Created on 12.04.2019

@author: Ruslan Dolovanyuk

"""

from commands import Commands

import wx


class Drawer:
    """Main class graphical form for tracer."""

    def __init__(self):
        """Initilizing drawer form."""
        self.app = wx.App()
        self.wnd = DrawerFrame()
        self.wnd.Show(True)
        self.app.SetTopWindow(self.wnd)

    def mainloop(self):
        """Graphical main loop running."""
        self.app.MainLoop()


class DrawerFrame(wx.Frame):
    """Create user interface."""

    def __init__(self):
        """Initialize interface."""
        super().__init__(None, wx.ID_ANY, 'Tracer - просмотрщик логов', size=wx.Size(600, 400))
        self.command = Commands(self)
        self.path = ''
        title_log = 'Выбор log файла:'
        wildcard_log = 'log file (*.log)|*.log|' \
                       'All files (*.*)|*.*'

        panel = wx.Panel(self, wx.ID_ANY)
        sizer_panel = wx.BoxSizer(wx.HORIZONTAL)
        sizer_panel.Add(panel, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer_panel)

        box_log_browse = wx.StaticBox(panel, wx.ID_ANY, 'Log файл')
        self.log_ctrl = wx.FilePickerCtrl(box_log_browse,
                                          wx.ID_ANY,
                                          self.path,
                                          title_log,
                                          wildcard_log,
                                          style=wx.FLP_OPEN |
                                          wx.FLP_USE_TEXTCTRL)
        self.log_ctrl.GetPickerCtrl().SetLabel('Обзор...')
        self.but_load = wx.Button(panel, wx.ID_ANY, 'Загрузить')
        but_about = wx.Button(panel, wx.ID_ANY, 'О программе...')
        but_exit = wx.Button(panel, wx.ID_ANY, 'Выход')
        box_exceptions = wx.StaticBox(panel, wx.ID_ANY, 'Исключения')
        self.mask = wx.TextCtrl(box_exceptions, wx.ID_ANY)
        self.but_add_exception = wx.Button(box_exceptions, wx.ID_ANY, 'Добавить')
        self.masks = wx.ListBox(box_exceptions, wx.ID_ANY, choices=self.command.masks,
                                style=wx.LB_SINGLE | wx.LB_HSCROLL)
        self.but_del_exception = wx.Button(box_exceptions, wx.ID_ANY, 'Удалить')
        box_rows = wx.StaticBox(panel, wx.ID_ANY, 'Трейсы')
        self.data = wx.TextCtrl(box_rows, wx.ID_ANY,
                                style=wx.TE_MULTILINE | wx.TE_READONLY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        log_sizer = wx.BoxSizer(wx.HORIZONTAL)
        log_browse_sizer = wx.StaticBoxSizer(box_log_browse, wx.VERTICAL)
        log_browse_sizer.Add(self.log_ctrl, 0, wx.EXPAND | wx.ALL, 5)
        log_sizer.Add(log_browse_sizer, 1, wx.EXPAND | wx.ALL, 5)
        log_sizer.Add(self.but_load, 0, wx.EXPAND | wx.ALL, 5)
        log_sizer.Add(but_about, 0, wx.EXPAND | wx.ALL, 5)
        log_sizer.Add(but_exit, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(log_sizer, 0, wx.EXPAND | wx.ALL)
        exceptions_sizer = wx.StaticBoxSizer(box_exceptions, wx.HORIZONTAL)
        exceptions_left_sizer = wx.BoxSizer(wx.VERTICAL)
        exceptions_left_sizer.Add(self.mask, 0, wx.EXPAND | wx.ALL, 5)
        exceptions_left_sizer.Add(self.but_add_exception, 0, wx.EXPAND | wx.ALL, 5)
        exceptions_left_sizer.Add(self.but_del_exception, 0, wx.EXPAND | wx.ALL, 5)
        exceptions_sizer.Add(exceptions_left_sizer, 0, wx.EXPAND | wx.ALL)
        exceptions_sizer.Add(self.masks, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(exceptions_sizer, 0, wx.EXPAND | wx.ALL)
        rows_sizer = wx.StaticBoxSizer(box_rows, wx.HORIZONTAL)
        rows_sizer.Add(self.data, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(rows_sizer, 1, wx.EXPAND | wx.ALL)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, getattr(self.command, 'close_window'))
        self.Bind(wx.EVT_FILEPICKER_CHANGED,
                  getattr(self.command, 'log_browse'), self.log_ctrl)
        self.Bind(wx.EVT_TEXT, getattr(self.command, 'edit_mask'), self.mask)
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'add_exception'), self.but_add_exception)
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'del_exception'), self.but_del_exception)
        self.Bind(wx.EVT_LISTBOX, getattr(self.command, 'sel_mask'), self.masks)
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'load_log'), self.but_load)
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'about'), but_about)
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'close'), but_exit)

        self.but_load.Disable()
        self.but_add_exception.Disable()
        self.but_del_exception.Disable()
        self.Layout()
