from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_ConverPage(object):
    def setupUi(self, ConverPage):
        ConverPage.setObjectName("ConverPage")
        ConverPage.resize(961, 646)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        ConverPage.setPalette(palette)
        ConverPage.setDocumentMode(False)
        ConverPage.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(ConverPage)
        self.centralwidget.setObjectName("centralwidget")
        self.BaseButton1 = QtWidgets.QComboBox(self.centralwidget)
        self.BaseButton1.setGeometry(QtCore.QRect(210, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BaseButton1.setFont(font)
        self.BaseButton1.setEditable(False)
        self.BaseButton1.setCurrentText("2")
        self.BaseButton1.setObjectName("BaseButton1")
        self.BaseButton1.addItem("")
        self.BaseButton1.addItem("")
        self.BaseButton1.addItem("")
        self.BaseButton1.addItem("")
        self.nsclbl = QtWidgets.QLabel(self.centralwidget)
        self.nsclbl.setGeometry(QtCore.QRect(0, 40, 961, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.nsclbl.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nsclbl.setFont(font)
        self.nsclbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nsclbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nsclbl.setLineWidth(1)
        self.nsclbl.setMidLineWidth(0)
        self.nsclbl.setTextFormat(QtCore.Qt.AutoText)
        self.nsclbl.setAlignment(QtCore.Qt.AlignCenter)
        self.nsclbl.setObjectName("nsclbl")
        self.inputbaselbl1 = QtWidgets.QLabel(self.centralwidget)
        self.inputbaselbl1.setGeometry(QtCore.QRect(70, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inputbaselbl1.setFont(font)
        self.inputbaselbl1.setObjectName("inputbaselbl1")
        self.BaseButton2 = QtWidgets.QComboBox(self.centralwidget)
        self.BaseButton2.setGeometry(QtCore.QRect(210, 310, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BaseButton2.setFont(font)
        self.BaseButton2.setEditable(False)
        self.BaseButton2.setCurrentText("2")
        self.BaseButton2.setFrame(True)
        self.BaseButton2.setObjectName("BaseButton2")
        self.BaseButton2.addItem("")
        self.BaseButton2.addItem("")
        self.BaseButton2.addItem("")
        self.BaseButton2.addItem("")
        self.outputbaselbl1 = QtWidgets.QLabel(self.centralwidget)
        self.outputbaselbl1.setGeometry(QtCore.QRect(50, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.outputbaselbl1.setFont(font)
        self.outputbaselbl1.setObjectName("outputbaselbl1")
        self.inputtake1 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputtake1.setGeometry(QtCore.QRect(460, 210, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputtake1.setFont(font)
        self.inputtake1.setAlignment(QtCore.Qt.AlignCenter)
        self.inputtake1.setPlaceholderText("")
        self.inputtake1.setClearButtonEnabled(True)
        self.inputtake1.setObjectName("inputtake1")
        self.output1 = QtWidgets.QLineEdit(self.centralwidget)
        self.output1.setEnabled(True)   ########
        self.output1.setGeometry(QtCore.QRect(460, 310, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output1.setFont(font)
        self.output1.setInputMask("")
        self.output1.setAlignment(QtCore.Qt.AlignCenter)
        self.output1.setDragEnabled(False)
        self.output1.setPlaceholderText("")
        self.output1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.output1.setClearButtonEnabled(False)
        self.output1.setObjectName("output1")
        self.inputnumberlbl = QtWidgets.QLabel(self.centralwidget)
        self.inputnumberlbl.setGeometry(QtCore.QRect(720, 210, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inputnumberlbl.setFont(font)
        self.inputnumberlbl.setObjectName("inputnumberlbl")
        self.outputnumberlbl = QtWidgets.QLabel(self.centralwidget)
        self.outputnumberlbl.setGeometry(QtCore.QRect(720, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.outputnumberlbl.setFont(font)
        self.outputnumberlbl.setObjectName("outputnumberlbl")
        self.convertoutputbtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertoutputbtn.setGeometry(QtCore.QRect(270, 420, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convertoutputbtn.setFont(font)
        icon = QtGui.QIcon.fromTheme("Light")
        self.convertoutputbtn.setIcon(icon)
        self.convertoutputbtn.setCheckable(True)
        self.convertoutputbtn.setAutoDefault(False)
        self.convertoutputbtn.setDefault(True)
        self.convertoutputbtn.setFlat(False)
        self.convertoutputbtn.setObjectName("convertoutputbtn")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(440, 420, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clearbtn.setFont(font)
        self.clearbtn.setDefault(True)
        self.clearbtn.setObjectName("clearbtn")
        ConverPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConverPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 26))
        self.menubar.setObjectName("menubar")
        ConverPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConverPage)
        self.statusbar.setObjectName("statusbar")
        ConverPage.setStatusBar(self.statusbar)

        self.retranslateUi(ConverPage)
        self.BaseButton1.setCurrentIndex(0)
        self.BaseButton2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConverPage)
        
        self.convertoutputbtn.clicked.connect(self.convert)
        self.clearbtn.clicked.connect(self.clear)
        

    def retranslateUi(self, ConverPage):
        _translate = QtCore.QCoreApplication.translate
        ConverPage.setWindowTitle(_translate("ConverPage", "ConvertPage"))
        self.BaseButton1.setItemText(0, _translate("ConverPage", "2"))
        self.BaseButton1.setItemText(1, _translate("ConverPage", "8"))
        self.BaseButton1.setItemText(2, _translate("ConverPage", "10"))
        self.BaseButton1.setItemText(3, _translate("ConverPage", "16"))
        self.nsclbl.setText(_translate("ConverPage", "Number System Conversion"))
        self.inputbaselbl1.setText(_translate("ConverPage", "Input Base"))
        self.BaseButton2.setItemText(0, _translate("ConverPage", "2"))
        self.BaseButton2.setItemText(1, _translate("ConverPage", "8"))
        self.BaseButton2.setItemText(2, _translate("ConverPage", "10"))
        self.BaseButton2.setItemText(3, _translate("ConverPage", "16"))
        self.outputbaselbl1.setText(_translate("ConverPage", "Output Base"))
        self.output1.setText(_translate("ConverPage", "Output"))
        self.inputnumberlbl.setText(_translate("ConverPage", "Input Number"))
        self.outputnumberlbl.setText(_translate("ConverPage", "Output Number "))
        self.convertoutputbtn.setText(_translate("ConverPage", "CONVERT"))
        self.clearbtn.setText(_translate("ConverPage", "CLEAR"))
        
    def clear(self):
        self.inputtake1.setText("")
        self.output1.setText("")
    
    def convert(self):    
        
        dropDown1 = int(self.BaseButton1.currentText())
        dropDown2 = int(self.BaseButton2.currentText())
        
        if dropDown1 == 2 and dropDown2 == 2:
            inpbin = str(self.inputtake1.text())      
            flag=1
            for i in inpbin:
                if i=='0' or i=='1' or i=='.':
                    continue
                else:
                    msg=QMessageBox()
                    msg.setWindowTitle("Binary Number Error")
                    msg.setText("Number should contain only 1 and 0 and for fraction only(.) ")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    flag=0
                    break
            if flag==0:
                self.output1.setText("")
            else:
                self.output1.setText(inpbin)
            
            
        elif dropDown1 == 2 and dropDown2 == 8:
            inp = self.inputtake1.text()
            value = self.bintooct()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 2 and dropDown2 == 10:
            value = str(self.bintodec())
            self.output1.setText(str(value))
        elif dropDown1 == 2 and dropDown2 == 16:
            inp = self.inputtake1.text()
            value = self.bintohex()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 10 and dropDown2 == 2:
            value = self.dectobin()
            self.output1.setText(str(value))
        elif dropDown1 == 10 and dropDown2 == 8:
            value = self.dectooct()
            self.output1.setText(str(value))            
        elif dropDown1 == 10 and dropDown2 == 10:
            inpbin = str(self.inputtake1.text())      
            flag=1
            for i in inpbin:
                if (i>='0'and i<='9') or i=='.':
                    continue
                else:
                    msg=QMessageBox()
                    msg.setWindowTitle("Decimal Number Error")
                    msg.setText("Number should contain only 0 - 9 and for fraction only(.) ")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    flag=0
                    break
            if flag==0:
                self.output1.setText("")
            else:
                self.output1.setText(inpbin)
                
        elif dropDown1 == 10 and dropDown2 == 16:
            value = self.dectohex()
            self.output1.setText(str(value))
        elif dropDown1 == 8 and dropDown2 == 2:
            inp = self.inputtake1.text()
            value = self.octtobin()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 8 and dropDown2 == 8:
            inpbin = str(self.inputtake1.text())      
            flag=1
            for i in inpbin:
                if (i>='0'and i<='7') or i=='.':
                    continue
                else:
                    msg=QMessageBox()
                    msg.setWindowTitle("Octal Number Error")
                    msg.setText("Number should contain only 0 - 7 and for fraction only(.) ")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    flag=0
                    break
            if flag==0:
                self.output1.setText("")
            else:
                self.output1.setText(inpbin)
        elif dropDown1 == 8 and dropDown2 == 10:
            value = self.octtodec()
            self.output1.setText(str(value))
        elif dropDown1 == 8 and dropDown2 == 16:
            inp = self.inputtake1.text()
            value = self.octtohex()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 16 and dropDown2 == 2:
            inp = self.inputtake1.text()
            value = self.hextobin()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 16 and dropDown2 == 8:
            inp = self.inputtake1.text()
            value = self.hextooct()
            self.output1.setText(str(value))
            self.inputtake1.setText(str(inp))
        elif dropDown1 == 16 and dropDown2 == 10:
            value = self.hextodec()
            self.output1.setText(str(value))            
        elif dropDown1 == 16 and dropDown2 == 16:
            inpbin = str(self.inputtake1.text())      
            flag=1
            for i in inpbin:
                if (i>='0'and i<='9') or i=='.' or (i>='A' and i<='F') or (i>='a' and i<='f'):
                    continue
                else:
                    msg=QMessageBox()
                    msg.setWindowTitle("HexaDecimal Number Error")
                    msg.setText("Number should contain only 0 - 9 or [A-F][a-f] and for fraction only(.) ")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    flag=0
                    break
            if flag==0:
                self.output1.setText("")
            else:
                self.output1.setText(inpbin)

            
    # Binary to decimal Perfectly Working for both the conditions fractional and decimal Part #
    def bintodec(self):
        inpbin = str(self.inputtake1.text())      
        for i in inpbin:
            if i=='0' or i=='1' or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Binary Number Error")
                msg.setText("Number should contain only 1 and 0 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
    
        splitedData=inpbin.split(".")
        if len(splitedData) > 1:
            decimal_part = splitedData[0]
            list_bin_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_bin_data.append(decimal_part[i])
                    
            value = 0
            for i in range(len(list_bin_data)):
            	digit = list_bin_data.pop()
            	if digit == '1':
            		value = value + pow(2, i)
    
            
            fractional_part = splitedData[1]
            
            list_bin_data_fract=[]
            for i in range(len(fractional_part)):
                if fractional_part[i]!=' ':
                    list_bin_data_fract.append(fractional_part[i])
            
            value2 = 0
            p=-1
            list_bin_data_fract.reverse()
            for i in range(len(list_bin_data_fract)):
                digit2= list_bin_data_fract.pop()
                if digit2 == '1':
                    value2=value2 + pow(2,p)
                p-=1
            fin_value = value+value2
            return fin_value
            
            
        else:
            decimal_part = splitedData[0]
            list_bin_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_bin_data.append(decimal_part[i])
            value = 0
            for i in range(len(list_bin_data)):
            	digit = list_bin_data.pop()
            	if digit == '1':
            		value = value + pow(2, i)
            
            return value
    
        
    def dectobin(self):
        inpdec = str(self.inputtake1.text())
        for i in inpdec:
            if (i>='0' and i<='9') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Decimal Number Error")
                msg.setText("Number should contain only 0 - 9 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        splitedData=inpdec.split(".")
        
        if len(splitedData)>1:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%2
                list_dec_data.append(dig)
                decimal_part=decimal_part//2
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
                
            va="0"
            
            fractional_part = float((va + "." + splitedData[1]))
            list_frac_part=[]
            for i in range(6):
                val = float(fractional_part*2)
                spl = str(val)
                spll = spl.split(".")
                list_frac_part.append(spll[0])
                fractional_part = float(val - int(val))
                
            st1=""
            for i in list_frac_part:
                st1+=str(i)
            
            finst= st + "." + st1
            
            return  finst
            
        else:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%2
                list_dec_data.append(dig)
                decimal_part=decimal_part//2
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
            
            return st
        
    def dectooct(self):
        inpdec = str(self.inputtake1.text())
        for i in inpdec:
            if (i>='0' and i<='9') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Decimal Number Error")
                msg.setText("Number should contain only 0 - 9 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        splitedData=inpdec.split(".")
        
        if len(splitedData)>1:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%8
                list_dec_data.append(dig)
                decimal_part=decimal_part//8
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
                
            va="0"
            
            fractional_part = float((va + "." + splitedData[1]))
            list_frac_part=[]
            for i in range(6):
                val = float(fractional_part*8)
                spl = str(val)
                spll = spl.split(".")
                list_frac_part.append(spll[0])
                fractional_part = float(val - int(val))
                
            st1=""
            for i in list_frac_part:
                st1+=str(i)
            
            finst= st + "." + st1
            
            return  finst
                
        else:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%8
                list_dec_data.append(dig)
                decimal_part=decimal_part//8
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
            
            return st
        
    def dectohex(self):
        inpdec = str(self.inputtake1.text())
        for i in inpdec:
            if (i>='0' and i<='9') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Decimal Number Error")
                msg.setText("Number should contain only 0 - 9 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        splitedData=inpdec.split(".")
        
        if len(splitedData)>1:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%16
                if dig==10:
                    list_dec_data.append('A')
                elif dig==11:
                    list_dec_data.append('B')
                elif dig==12:
                    list_dec_data.append('C')
                elif dig==13:
                    list_dec_data.append('D')
                elif dig==14:
                    list_dec_data.append('E')
                elif dig==15:
                    list_dec_data.append('F')
                else:
                    list_dec_data.append(dig)
                decimal_part=decimal_part//16
                
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
                
            va="0"
            
            fractional_part = float((va + "." + splitedData[1]))
            list_frac_part=[]
            for i in range(6):
                val = float(fractional_part*16)
                spl = str(val)
                spll = spl.split(".")
                if spll[0]=='10':
                    list_frac_part.append('A')
                elif spll[0]=='11':
                    list_frac_part.append('B')
                elif spll[0]=='12':
                    list_frac_part.append('C')
                elif spll[0]=='13':
                    list_frac_part.append('D')
                elif spll[0]=='14':
                    list_frac_part.append('E')
                elif spll[0]=='15':
                    list_frac_part.append('F')
                else:
                    list_frac_part.append(spll[0])
                fractional_part = float(val - int(val))
                
            st1=""
            for i in list_frac_part:
                st1+=str(i)
            
            finst= st + "." + st1
            
            return  finst
                
        else:
            decimal_part = int(splitedData[0])
            list_dec_data=[]
            while decimal_part > 0:
                dig=decimal_part%16
                if dig==10:
                    list_dec_data.append('A')
                elif dig==11:
                    list_dec_data.append('B')
                elif dig==12:
                    list_dec_data.append('C')
                elif dig==13:
                    list_dec_data.append('D')
                elif dig==14:
                    list_dec_data.append('E')
                elif dig==15:
                    list_dec_data.append('F')
                else:
                    list_dec_data.append(dig)
                decimal_part=decimal_part//16
                
            list_dec_data.reverse()
            
            st = ""
            for i in list_dec_data:
                st+=str(i)
            
            return st
        
    def bintooct(self):
        inpbin = str(self.inputtake1.text())      
        for i in inpbin:
            if i=='0' or i=='1' or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Binary Number Error")
                msg.setText("Number should contain only 1 and 0 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
        
        value = self.bintodec()       
        self.inputtake1.setText(str(value))
        return self.dectooct()
    
    def bintohex(self):
        inpbin = str(self.inputtake1.text())      
        for i in inpbin:
            if i=='0' or i=='1' or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Binary Number Error")
                msg.setText("Number should contain only 1 and 0 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
        value = self.bintodec()       
        self.inputtake1.setText(str(value))
        return self.dectohex()
    
    def octtodec(self):
        inpoct = str(self.inputtake1.text())
        for i in inpoct:
            if (i>='0' and i<='7') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Octal Number Error")
                msg.setText("Number should contain only 0 - 7 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        splitedData=inpoct.split(".")
        if len(splitedData) > 1:
            decimal_part = splitedData[0]
            list_oct_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_oct_data.append(decimal_part[i])
                    
            value = 0
            list_oct_data.reverse()
            for i in range(len(list_oct_data)):
           		value = value + int(list_oct_data[i])*pow(8, i)
    
            
            fractional_part = splitedData[1]
            
            list_oct_data_fract=[]
            for i in range(len(fractional_part)):
                if fractional_part[i]!=' ':
                    list_oct_data_fract.append(fractional_part[i])
            
            value2 = 0
            p=-1
            
            for i in range(len(list_oct_data_fract)):
                value2=value2 + int(list_oct_data_fract[i])*pow(8,p)
                p-=1
                
            fin_value = value+value2
            return fin_value
            
            
        else:
            decimal_part = splitedData[0]
            list_oct_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_oct_data.append(decimal_part[i])
            value = 0
            list_oct_data.reverse()
            for i in range(len(list_oct_data)):
           		value = value + int(list_oct_data[i])*pow(8, i)
            
            return value
        
    def octtobin(self):
        inpoct = str(self.inputtake1.text())
        for i in inpoct:
            if (i>='0' and i<='7') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Octal Number Error")
                msg.setText("Number should contain only 0 - 7 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        value = self.octtodec()       
        self.inputtake1.setText(str(value))
        return self.dectobin()
    
    def octtohex(self):
        inpoct = str(self.inputtake1.text())
        for i in inpoct:
            if (i>='0' and i<='7') or i=='.':
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("Octal Number Error")
                msg.setText("Number should contain only 0 - 7 and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        value = self.octtodec()       
        self.inputtake1.setText(str(value))
        return self.dectohex()
    
    def hextodec(self):
        inphex = str(self.inputtake1.text())
        for i in inphex:
            if (i>='0'and i<='9') or i=='.' or (i>='A' and i<='F') or (i>='a' and i<='f'):
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("HexaDecimal Number Error")
                msg.setText("Number should contain only 0 - 9 or [A-F][a-f] and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
        splitedData=inphex.split(".")
        if len(splitedData) > 1:
            decimal_part = splitedData[0]
            list_hex_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_hex_data.append(decimal_part[i])
                    
            value = 0
            list_hex_data.reverse()
            for i in range(len(list_hex_data)):
                if list_hex_data[i]=='A' or list_hex_data[i]=='a':
                    value = value + 10*pow(16, i)
                elif list_hex_data[i]=='B' or list_hex_data[i]=='b':
                    value = value + 11*pow(16, i)
                elif list_hex_data[i]=='c' or list_hex_data[i]=='c':
                    value = value + 12*pow(16, i)
                elif list_hex_data[i]=='D' or list_hex_data[i]=='d':
                    value = value + 13*pow(16, i)
                elif list_hex_data[i]=='E' or list_hex_data[i]=='e':
                    value = value + 14*pow(16, i)
                elif list_hex_data[i]=='F' or list_hex_data[i]=='f':
                    value = value + 15*pow(16, i)
                else:
               		 value = value + (int(list_hex_data[i]))*pow(16, i)
            
            print(value)
            
            fractional_part = splitedData[1]
            
            list_hex_data_fract=[]
            for i in range(len(fractional_part)):
                if fractional_part[i]!=' ':
                    list_hex_data_fract.append(fractional_part[i])
            
            value2 = 0
            p=-1
            
            for i in range(len(list_hex_data_fract)):
                if list_hex_data_fract[i]=='A' or list_hex_data_fract[i]=='a':
                    value2 = value2 + 10*pow(16, p)
                elif list_hex_data_fract[i]=='B' or list_hex_data_fract[i]=='b':
                    value2 = value2 + 11*pow(16, p)
                elif list_hex_data_fract[i]=='c' or list_hex_data_fract[i]=='c':
                    value2 = value2 + 12*pow(16, p)
                elif list_hex_data_fract[i]=='D' or list_hex_data_fract[i]=='d':
                    value2 = value2 + 13*pow(16, p)
                elif list_hex_data_fract[i]=='E' or list_hex_data_fract[i]=='e':
                    value2 = value2 + 14*pow(16, p)
                elif list_hex_data_fract[i]=='F' or list_hex_data_fract[i]=='f':
                    value2 = value2 + 15*pow(16, p)
                else:
               		value2 = value2 + (int(list_hex_data_fract[i]))*pow(16, p)
                       
                p-=1
                
            print(value2)
                
            fin_value = value+value2
            return fin_value
            
            
        else:
            decimal_part = splitedData[0]
            list_hex_data=[]
            for i in range(len(decimal_part)):
                if decimal_part[i]!=" ":
                    list_hex_data.append(decimal_part[i])
                    
            value = 0
            list_hex_data.reverse()
            for i in range(len(list_hex_data)):
                if list_hex_data[i]=='A' or list_hex_data[i]=='a':
                    value = value + 10*pow(16, i)
                elif list_hex_data[i]=='B' or list_hex_data[i]=='b':
                    value = value + 11*pow(16, i)
                elif list_hex_data[i]=='c' or list_hex_data[i]=='c':
                    value = value + 12*pow(16, i)
                elif list_hex_data[i]=='D' or list_hex_data[i]=='d':
                    value = value + 13*pow(16, i)
                elif list_hex_data[i]=='E' or list_hex_data[i]=='e':
                    value = value + 14*pow(16, i)
                elif list_hex_data[i]=='F' or list_hex_data[i]=='f':
                    value = value + 15*pow(16, i)
                else:
               		 value = value + (int(list_hex_data[i]))*pow(16, i)
            
            return value
        
    def hextobin(self):
        inphex = str(self.inputtake1.text())
        for i in inphex:
            if (i>='0'and i<='9') or i=='.' or (i>='A' and i<='F') or (i>='a' and i<='f'):
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("HexaDecimal Number Error")
                msg.setText("Number should contain only 0 - 9 or [A-F][a-f] and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
            
        value = self.hextodec()       
        self.inputtake1.setText(str(value))
        return self.dectobin()
    
    def hextooct(self):
        inphex = str(self.inputtake1.text())
        for i in inphex:
            if (i>='0'and i<='9') or i=='.' or (i>='A' and i<='F') or (i>='a' and i<='f'):
                continue
            else:
                st=""
                msg=QMessageBox()
                msg.setWindowTitle("HexaDecimal Number Error")
                msg.setText("Number should contain only 0 - 9 or [A-F][a-f] and for fraction only(.) ")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return st
        value = self.hextodec()       
        self.inputtake1.setText(str(value))
        return self.dectooct()
            
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConverPage = QtWidgets.QMainWindow()
    ui = Ui_ConverPage()
    ui.setupUi(ConverPage)
    ConverPage.show()
    sys.exit(app.exec_())
