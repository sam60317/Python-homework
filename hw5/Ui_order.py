# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\school\python\hw5\order.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrderWindow(object):
    def setupUi(self, OrderWindow):
        OrderWindow.setObjectName("OrderWindow")
        OrderWindow.resize(600, 820)
        self.centralwidget = QtWidgets.QWidget(OrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setObjectName("label_size")
        self.verticalLayout.addWidget(self.label_size)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_mid = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.btn_mid.setFont(font)
        self.btn_mid.setObjectName("btn_mid")
        self.verticalLayout_2.addWidget(self.btn_mid)
        self.btn_large = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.btn_large.setFont(font)
        self.btn_large.setObjectName("btn_large")
        self.verticalLayout_2.addWidget(self.btn_large)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setObjectName("label_temp")
        self.verticalLayout.addWidget(self.label_temp)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_temp = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.comboBox_temp.setFont(font)
        self.comboBox_temp.setObjectName("comboBox_temp")
        self.horizontalLayout.addWidget(self.comboBox_temp)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_sweet = QtWidgets.QLabel(self.centralwidget)
        self.label_sweet.setObjectName("label_sweet")
        self.verticalLayout.addWidget(self.label_sweet)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_sweet = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.comboBox_sweet.setFont(font)
        self.comboBox_sweet.setObjectName("comboBox_sweet")
        self.horizontalLayout_2.addWidget(self.comboBox_sweet)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.btn_sub.setFont(font)
        self.btn_sub.setObjectName("btn_sub")
        self.horizontalLayout_3.addWidget(self.btn_sub)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_3.addWidget(self.btn_add)
        self.btn_addTo = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.btn_addTo.setFont(font)
        self.btn_addTo.setObjectName("btn_addTo")
        self.horizontalLayout_3.addWidget(self.btn_addTo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        OrderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OrderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        OrderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OrderWindow)
        self.statusbar.setObjectName("statusbar")
        OrderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OrderWindow)
        QtCore.QMetaObject.connectSlotsByName(OrderWindow)

    def retranslateUi(self, OrderWindow):
        _translate = QtCore.QCoreApplication.translate
        OrderWindow.setWindowTitle(_translate("OrderWindow", "OrderWindow"))
        self.label_size.setText(_translate("OrderWindow", "TextLabel"))
        self.btn_mid.setText(_translate("OrderWindow", "中 Medium"))
        self.btn_large.setText(_translate("OrderWindow", "大 Large (+10元)"))
        self.label_temp.setText(_translate("OrderWindow", "TextLabel"))
        self.label_sweet.setText(_translate("OrderWindow", "TextLabel"))
        self.btn_sub.setText(_translate("OrderWindow", "-"))
        self.btn_add.setText(_translate("OrderWindow", "+"))
        self.btn_addTo.setText(_translate("OrderWindow", "新增至訂單"))
