# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_projekt2DialogBase(object):
    def setupUi(self, projekt2DialogBase):
        projekt2DialogBase.setObjectName("projekt2DialogBase")
        projekt2DialogBase.resize(477, 391)
        self.button_box = QtWidgets.QDialogButtonBox(projekt2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(120, 350, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.pushButton_dH = QtWidgets.QPushButton(projekt2DialogBase)
        self.pushButton_dH.setGeometry(QtCore.QRect(30, 60, 101, 23))
        self.pushButton_dH.setObjectName("pushButton_dH")
        self.pushButton_liczelementy = QtWidgets.QPushButton(projekt2DialogBase)
        self.pushButton_liczelementy.setGeometry(QtCore.QRect(30, 20, 101, 23))
        self.pushButton_liczelementy.setObjectName("pushButton_liczelementy")
        self.pushButton_pole = QtWidgets.QPushButton(projekt2DialogBase)
        self.pushButton_pole.setGeometry(QtCore.QRect(30, 100, 101, 23))
        self.pushButton_pole.setObjectName("pushButton_pole")
        self.label_liczbaelementow = QtWidgets.QLabel(projekt2DialogBase)
        self.label_liczbaelementow.setGeometry(QtCore.QRect(160, 20, 41, 21))
        self.label_liczbaelementow.setText("")
        self.label_liczbaelementow.setObjectName("label_liczbaelementow")
        self.label_dH = QtWidgets.QLabel(projekt2DialogBase)
        self.label_dH.setGeometry(QtCore.QRect(160, 60, 41, 21))
        self.label_dH.setText("")
        self.label_dH.setObjectName("label_dH")
        self.label_pole = QtWidgets.QLabel(projekt2DialogBase)
        self.label_pole.setGeometry(QtCore.QRect(160, 100, 241, 21))
        self.label_pole.setText("")
        self.label_pole.setObjectName("label_pole")
        self.line = QtWidgets.QFrame(projekt2DialogBase)
        self.line.setGeometry(QtCore.QRect(140, 20, 20, 101))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mMapLayerComboBox_layers = QgsMapLayerComboBox(projekt2DialogBase)
        self.mMapLayerComboBox_layers.setGeometry(QtCore.QRect(20, 300, 131, 21))
        self.mMapLayerComboBox_layers.setObjectName("mMapLayerComboBox_layers")
        self.textEdit_pole = QtWidgets.QTextEdit(projekt2DialogBase)
        self.textEdit_pole.setGeometry(QtCore.QRect(100, 230, 181, 21))
        self.textEdit_pole.setObjectName("textEdit_pole")
        self.label = QtWidgets.QLabel(projekt2DialogBase)
        self.label.setGeometry(QtCore.QRect(20, 280, 131, 16))
        self.label.setObjectName("label")
        self.label_error = QtWidgets.QLabel(projekt2DialogBase)
        self.label_error.setGeometry(QtCore.QRect(30, 140, 191, 41))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")

        self.retranslateUi(projekt2DialogBase)
        self.button_box.accepted.connect(projekt2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(projekt2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(projekt2DialogBase)

    def retranslateUi(self, projekt2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        projekt2DialogBase.setWindowTitle(_translate("projekt2DialogBase", "projekt2"))
        self.pushButton_dH.setText(_translate("projekt2DialogBase", "RoznicaWysokosci"))
        self.pushButton_liczelementy.setText(_translate("projekt2DialogBase", "LiczElementy"))
        self.pushButton_pole.setText(_translate("projekt2DialogBase", "PolePowierzchni"))
        self.label.setText(_translate("projekt2DialogBase", "Aktualna warstwa:"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projekt2DialogBase = QtWidgets.QDialog()
    ui = Ui_projekt2DialogBase()
    ui.setupUi(projekt2DialogBase)
    projekt2DialogBase.show()
    sys.exit(app.exec_())
