# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterPanel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterPanel(object):
    def setupUi(self, FilterPanel):
        FilterPanel.setObjectName("FilterPanel")
        FilterPanel.resize(487, 564)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(FilterPanel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(FilterPanel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.partitionBox = QtWidgets.QGroupBox(self.widget)
        self.partitionBox.setCheckable(True)
        self.partitionBox.setChecked(False)
        self.partitionBox.setObjectName("partitionBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.partitionBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.partComboBox = QtWidgets.QComboBox(self.partitionBox)
        self.partComboBox.setObjectName("partComboBox")
        self.horizontalLayout_4.addWidget(self.partComboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.partitionBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.partBinSpinBox = QtWidgets.QSpinBox(self.partitionBox)
        self.partBinSpinBox.setMinimum(1)
        self.partBinSpinBox.setProperty("value", 10)
        self.partBinSpinBox.setObjectName("partBinSpinBox")
        self.horizontalLayout.addWidget(self.partBinSpinBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.partitionBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.partMinSpinBox = QtWidgets.QDoubleSpinBox(self.partitionBox)
        self.partMinSpinBox.setObjectName("partMinSpinBox")
        self.horizontalLayout_2.addWidget(self.partMinSpinBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.partitionBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.partMaxSpinBox = QtWidgets.QDoubleSpinBox(self.partitionBox)
        self.partMaxSpinBox.setObjectName("partMaxSpinBox")
        self.horizontalLayout_3.addWidget(self.partMaxSpinBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.partitionList = QtWidgets.QListView(self.partitionBox)
        self.partitionList.setObjectName("partitionList")
        self.verticalLayout.addWidget(self.partitionList)
        self.verticalLayout_4.addWidget(self.partitionBox)
        self.flaggedBox = QtWidgets.QGroupBox(self.widget)
        self.flaggedBox.setObjectName("flaggedBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.flaggedBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.flagIgnore = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagIgnore.setChecked(True)
        self.flagIgnore.setObjectName("flagIgnore")
        self.horizontalLayout_5.addWidget(self.flagIgnore)
        self.flagExclude = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagExclude.setObjectName("flagExclude")
        self.horizontalLayout_5.addWidget(self.flagExclude)
        self.flagKeep = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagKeep.setObjectName("flagKeep")
        self.horizontalLayout_5.addWidget(self.flagKeep)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_4 = QtWidgets.QLabel(self.flaggedBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.flaggedList = QtWidgets.QListView(self.flaggedBox)
        self.flaggedList.setObjectName("flaggedList")
        self.verticalLayout_2.addWidget(self.flaggedList)
        self.verticalLayout_4.addWidget(self.flaggedBox)
        self.filtersBox = QtWidgets.QGroupBox(self.splitter)
        self.filtersBox.setObjectName("filtersBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.filtersBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.saveFiltersButton = QtWidgets.QPushButton(self.filtersBox)
        self.saveFiltersButton.setObjectName("saveFiltersButton")
        self.horizontalLayout_6.addWidget(self.saveFiltersButton)
        self.loadFiltersButton = QtWidgets.QPushButton(self.filtersBox)
        self.loadFiltersButton.setObjectName("loadFiltersButton")
        self.horizontalLayout_6.addWidget(self.loadFiltersButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.filterTreeView = QtWidgets.QTreeView(self.filtersBox)
        self.filterTreeView.setObjectName("filterTreeView")
        self.filterTreeView.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.filterTreeView)
        self.verticalLayout_5.addWidget(self.splitter)

        self.retranslateUi(FilterPanel)
        QtCore.QMetaObject.connectSlotsByName(FilterPanel)

    def retranslateUi(self, FilterPanel):
        _translate = QtCore.QCoreApplication.translate
        FilterPanel.setWindowTitle(_translate("FilterPanel", "Filter Panel"))
        self.partitionBox.setTitle(_translate("FilterPanel", "Partition"))
        self.label.setText(_translate("FilterPanel", "Bins:"))
        self.label_2.setText(_translate("FilterPanel", "Min:"))
        self.label_3.setText(_translate("FilterPanel", "Max:"))
        self.flaggedBox.setTitle(_translate("FilterPanel", "Flagged Items"))
        self.flagIgnore.setText(_translate("FilterPanel", "Ignore"))
        self.flagExclude.setText(_translate("FilterPanel", "Exclude From Selection"))
        self.flagKeep.setText(_translate("FilterPanel", "Keep Only Flagged Items"))
        self.label_4.setText(_translate("FilterPanel", "Currently Flagged:"))
        self.filtersBox.setTitle(_translate("FilterPanel", "Filters"))
        self.saveFiltersButton.setText(_translate("FilterPanel", "Save"))
        self.loadFiltersButton.setText(_translate("FilterPanel", "Load"))
