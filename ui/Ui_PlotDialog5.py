# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotDialog(object):
    def setupUi(self, PlotDialog):
        PlotDialog.setObjectName("PlotDialog")
        PlotDialog.resize(334, 392)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PlotDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.description = QtWidgets.QLabel(PlotDialog)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.verticalLayout_2.addWidget(self.description)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PlotDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xCombo = QtWidgets.QComboBox(PlotDialog)
        self.xCombo.setObjectName("xCombo")
        self.horizontalLayout.addWidget(self.xCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(PlotDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.yCombo = QtWidgets.QComboBox(PlotDialog)
        self.yCombo.setObjectName("yCombo")
        self.horizontalLayout_2.addWidget(self.yCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(PlotDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.zCombo = QtWidgets.QComboBox(PlotDialog)
        self.zCombo.setObjectName("zCombo")
        self.horizontalLayout_3.addWidget(self.zCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(PlotDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.cCombo = QtWidgets.QComboBox(PlotDialog)
        self.cCombo.setObjectName("cCombo")
        self.horizontalLayout_4.addWidget(self.cCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.logCheckBox = QtWidgets.QCheckBox(PlotDialog)
        self.logCheckBox.setObjectName("logCheckBox")
        self.verticalLayout_2.addWidget(self.logCheckBox)
        self.frame = QtWidgets.QFrame(PlotDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minCheckBox = QtWidgets.QCheckBox(self.frame)
        self.minCheckBox.setObjectName("minCheckBox")
        self.horizontalLayout_5.addWidget(self.minCheckBox)
        self.minSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.minSpinBox.setEnabled(False)
        self.minSpinBox.setObjectName("minSpinBox")
        self.horizontalLayout_5.addWidget(self.minSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.maxCheckBox = QtWidgets.QCheckBox(self.frame)
        self.maxCheckBox.setObjectName("maxCheckBox")
        self.horizontalLayout_6.addWidget(self.maxCheckBox)
        self.maxSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.maxSpinBox.setEnabled(False)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.horizontalLayout_6.addWidget(self.maxSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.binCheckBox = QtWidgets.QCheckBox(self.frame)
        self.binCheckBox.setObjectName("binCheckBox")
        self.horizontalLayout_7.addWidget(self.binCheckBox)
        self.binSpinBox = QtWidgets.QSpinBox(self.frame)
        self.binSpinBox.setEnabled(False)
        self.binSpinBox.setMinimum(1)
        self.binSpinBox.setProperty("value", 10)
        self.binSpinBox.setObjectName("binSpinBox")
        self.horizontalLayout_7.addWidget(self.binSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.buttonBox = QtWidgets.QDialogButtonBox(PlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(PlotDialog)
        self.buttonBox.accepted.connect(PlotDialog.accept)
        self.buttonBox.rejected.connect(PlotDialog.reject)
        self.maxCheckBox.toggled['bool'].connect(self.maxSpinBox.setEnabled)
        self.minCheckBox.toggled['bool'].connect(self.minSpinBox.setEnabled)
        self.binCheckBox.toggled['bool'].connect(self.binSpinBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(PlotDialog)

    def retranslateUi(self, PlotDialog):
        _translate = QtCore.QCoreApplication.translate
        PlotDialog.setWindowTitle(_translate("PlotDialog", "Scatter Plot"))
        self.description.setText(_translate("PlotDialog", "TextLabel"))
        self.label.setText(_translate("PlotDialog", "X Axis:"))
        self.label_2.setText(_translate("PlotDialog", "Y Axis:"))
        self.label_3.setText(_translate("PlotDialog", "Z Axis:"))
        self.label_4.setText(_translate("PlotDialog", "Color By:"))
        self.logCheckBox.setText(_translate("PlotDialog", "Log Scale (Colors)"))
        self.minCheckBox.setText(_translate("PlotDialog", "Min:"))
        self.maxCheckBox.setText(_translate("PlotDialog", "Max:"))
        self.binCheckBox.setText(_translate("PlotDialog", "Bins:"))

