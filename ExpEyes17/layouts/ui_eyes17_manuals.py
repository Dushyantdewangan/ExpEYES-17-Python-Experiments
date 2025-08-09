# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eyes17_manuals.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(212, 138)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioPDF = QtWidgets.QRadioButton(self.groupBox)
        self.radioPDF.setChecked(True)
        self.radioPDF.setObjectName("radioPDF")
        self.verticalLayout_2.addWidget(self.radioPDF)
        self.radioEPUB = QtWidgets.QRadioButton(self.groupBox)
        self.radioEPUB.setObjectName("radioEPUB")
        self.verticalLayout_2.addWidget(self.radioEPUB)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose the format"))
        self.groupBox.setTitle(_translate("Dialog", "Format for the User Manual"))
        self.radioPDF.setText(_translate("Dialog", "PDF"))
        self.radioEPUB.setText(_translate("Dialog", "EPUB"))
