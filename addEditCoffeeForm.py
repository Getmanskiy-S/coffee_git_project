# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CoffeeEditDialog(object):
    def setupUi(self, CoffeeEditDialog):
        CoffeeEditDialog.setObjectName("CoffeeEditDialog")
        CoffeeEditDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(CoffeeEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEditSort = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditSort.setObjectName("lineEditSort")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditSort)
        self.label_2 = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEditDegree = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditDegree.setObjectName("lineEditDegree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditDegree)
        self.label_3 = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.lineEditState = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditState.setObjectName("lineEditState")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditState)
        self.label_4 = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEditTaste = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditTaste.setObjectName("lineEditTaste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditTaste)
        self.label_5 = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEditPrice = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditPrice)
        self.label_6 = QtWidgets.QLabel(parent=CoffeeEditDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.lineEditVolume = QtWidgets.QLineEdit(parent=CoffeeEditDialog)
        self.lineEditVolume.setObjectName("lineEditVolume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditVolume)
        self.verticalLayout.addLayout(self.formLayout)
        self.saveButton = QtWidgets.QPushButton(parent=CoffeeEditDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.retranslateUi(CoffeeEditDialog)
        QtCore.QMetaObject.connectSlotsByName(CoffeeEditDialog)

    def retranslateUi(self, CoffeeEditDialog):
        _translate = QtCore.QCoreApplication.translate
        CoffeeEditDialog.setWindowTitle(_translate("CoffeeEditDialog", "Редактировать запись о кофе"))
        self.label.setText(_translate("CoffeeEditDialog", "название сорта:"))
        self.label_2.setText(_translate("CoffeeEditDialog", "Степень обжарки:"))
        self.label_3.setText(_translate("CoffeeEditDialog", "молотый/в зернах"))
        self.label_4.setText(_translate("CoffeeEditDialog", "описание вкуса:"))
        self.label_5.setText(_translate("CoffeeEditDialog", "Цена:"))
        self.label_6.setText(_translate("CoffeeEditDialog", "Объем упаковки:"))
        self.saveButton.setText(_translate("CoffeeEditDialog", "Сохранить"))
