# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Dec  8 12:45:50 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1416, 973)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 12, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.useTemplateTab = QtWidgets.QWidget()
        self.useTemplateTab.setObjectName("useTemplateTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.useTemplateTab)
        self.gridLayout_3.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.useTemplateTab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.dataFileListWidget = QtWidgets.QWidget(self.splitter_2)
        self.dataFileListWidget.setObjectName("dataFileListWidget")
        self.metadataControlsWidget = QtWidgets.QWidget(self.splitter_2)
        self.metadataControlsWidget.setObjectName("metadataControlsWidget")
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.useTemplateTab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.folderDestCB = QtWidgets.QComboBox(self.useTemplateTab)
        self.folderDestCB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.folderDestCB.setObjectName("folderDestCB")
        self.folderDestCB.addItem("")
        self.folderDestCB.addItem("")
        self.horizontalLayout_5.addWidget(self.folderDestCB)
        self.folderDestLineEdit = QtWidgets.QLineEdit(self.useTemplateTab)
        self.folderDestLineEdit.setObjectName("folderDestLineEdit")
        self.horizontalLayout_5.addWidget(self.folderDestLineEdit)
        self.folderDestSelectBtn = QtWidgets.QPushButton(self.useTemplateTab)
        self.folderDestSelectBtn.setObjectName("folderDestSelectBtn")
        self.horizontalLayout_5.addWidget(self.folderDestSelectBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.startBtn = QtWidgets.QPushButton(self.useTemplateTab)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_6.addWidget(self.startBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.tabWidget.addTab(self.useTemplateTab, "")
        self.createTemplateTab = QtWidgets.QWidget()
        self.createTemplateTab.setObjectName("createTemplateTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.createTemplateTab)
        self.gridLayout_2.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.createTemplateTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.dataTypeLabel = QtWidgets.QLabel(self.createTemplateTab)
        self.dataTypeLabel.setObjectName("dataTypeLabel")
        self.horizontalLayout_4.addWidget(self.dataTypeLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.createTemplateTab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.fileParserCB = QtWidgets.QComboBox(self.createTemplateTab)
        self.fileParserCB.setObjectName("fileParserCB")
        self.horizontalLayout_4.addWidget(self.fileParserCB)
        self.fileParserPathLabel = QtWidgets.QLabel(self.createTemplateTab)
        font = QtGui.QFont()
        font.setItalic(True)
        self.fileParserPathLabel.setFont(font)
        self.fileParserPathLabel.setText("")
        self.fileParserPathLabel.setObjectName("fileParserPathLabel")
        self.horizontalLayout_4.addWidget(self.fileParserPathLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.createTemplateTab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.fileDestCB = QtWidgets.QComboBox(self.createTemplateTab)
        self.fileDestCB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.fileDestCB.setObjectName("fileDestCB")
        self.fileDestCB.addItem("")
        self.fileDestCB.addItem("")
        self.horizontalLayout.addWidget(self.fileDestCB)
        self.fileDestLineEdit = QtWidgets.QLineEdit(self.createTemplateTab)
        self.fileDestLineEdit.setObjectName("fileDestLineEdit")
        self.horizontalLayout.addWidget(self.fileDestLineEdit)
        self.fileDestSelectBtn = QtWidgets.QPushButton(self.createTemplateTab)
        self.fileDestSelectBtn.setObjectName("fileDestSelectBtn")
        self.horizontalLayout.addWidget(self.fileDestSelectBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.createTemplateTab)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.dataFileLineEdit = QtWidgets.QLineEdit(self.createTemplateTab)
        self.dataFileLineEdit.setObjectName("dataFileLineEdit")
        self.horizontalLayout_3.addWidget(self.dataFileLineEdit)
        self.dataFileSelectBtn = QtWidgets.QPushButton(self.createTemplateTab)
        self.dataFileSelectBtn.setObjectName("dataFileSelectBtn")
        self.horizontalLayout_3.addWidget(self.dataFileSelectBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.createTemplateTab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.availableMetadataWidget = QtWidgets.QWidget(self.splitter)
        self.availableMetadataWidget.setObjectName("availableMetadataWidget")
        self.extractedMetadataWidget = QtWidgets.QWidget(self.splitter)
        self.extractedMetadataWidget.setObjectName("extractedMetadataWidget")
        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.generateBtn = QtWidgets.QPushButton(self.createTemplateTab)
        self.generateBtn.setObjectName("generateBtn")
        self.horizontalLayout_2.addWidget(self.generateBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.tabWidget.addTab(self.createTemplateTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1416, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUse_Template = QtWidgets.QAction(MainWindow)
        self.actionUse_Template.setCheckable(True)
        self.actionUse_Template.setChecked(False)
        self.actionUse_Template.setObjectName("actionUse_Template")
        self.actionCreate_Template = QtWidgets.QAction(MainWindow)
        self.actionCreate_Template.setCheckable(True)
        self.actionCreate_Template.setChecked(True)
        self.actionCreate_Template.setObjectName("actionCreate_Template")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Metadata Extractor", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Destination Folder:", None, -1))
        self.folderDestCB.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Local File System", None, -1))
        self.folderDestCB.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "HyperThought", None, -1))
        self.folderDestSelectBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.startBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.useTemplateTab), QtWidgets.QApplication.translate("MainWindow", "Use Template", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Data Type Detected:", None, -1))
        self.dataTypeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "N/A", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "File Parser:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Output File Destination:", None, -1))
        self.fileDestCB.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Local File System", None, -1))
        self.fileDestCB.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "HyperThought", None, -1))
        self.fileDestSelectBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Data File:", None, -1))
        self.dataFileSelectBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.generateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Generate Template", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createTemplateTab), QtWidgets.QApplication.translate("MainWindow", "Create Template", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionUse_Template.setText(QtWidgets.QApplication.translate("MainWindow", "Use Template", None, -1))
        self.actionUse_Template.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Switch to \"Use Template\" Mode", None, -1))
        self.actionCreate_Template.setText(QtWidgets.QApplication.translate("MainWindow", "Create Template", None, -1))
        self.actionCreate_Template.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Switch to \"Create Template\" Mode", None, -1))

