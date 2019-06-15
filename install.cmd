pyinstaller -F --noconsole ^
--add-binary commands.pyd;. ^
--add-binary dialogs.pyd;. ^
--add-binary drawer.pyd;. ^
--add-binary extrows.pyd;. ^
--hidden-import wx ^
main.pyw
