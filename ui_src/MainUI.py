# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Face_Recognition_window(object):
    def setupUi(self, Face_Recognition_window):
        Face_Recognition_window.setObjectName("Face_Recognition_window")
        Face_Recognition_window.resize(843, 694)
        Face_Recognition_window.setMinimumSize(QtCore.QSize(843, 694))
        Face_Recognition_window.setMaximumSize(QtCore.QSize(843, 694))
        Face_Recognition_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Face_Recognition_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 798, 603))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_frame = QtWidgets.QLabel(self.layoutWidget)
        self.lab_frame.setEnabled(True)
        self.lab_frame.setMinimumSize(QtCore.QSize(641, 481))
        self.lab_frame.setMaximumSize(QtCore.QSize(641, 481))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lab_frame.setFont(font)
        self.lab_frame.setToolTip("")
        self.lab_frame.setTextFormat(QtCore.Qt.RichText)
        self.lab_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_frame.setObjectName("lab_frame")
        self.verticalLayout.addWidget(self.lab_frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_selecCalss = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecCalss.setFont(font)
        self.lab_selecCalss.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecCalss.setObjectName("lab_selecCalss")
        self.verticalLayout_2.addWidget(self.lab_selecCalss)
        self.lab_selecLable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecLable.setFont(font)
        self.lab_selecLable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecLable.setObjectName("lab_selecLable")
        self.verticalLayout_2.addWidget(self.lab_selecLable)
        self.lab_selecLable_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecLable_2.setFont(font)
        self.lab_selecLable_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecLable_2.setObjectName("lab_selecLable_2")
        self.verticalLayout_2.addWidget(self.lab_selecLable_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_face = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_face.setObjectName("comboBox_face")
        self.verticalLayout_3.addWidget(self.comboBox_face)
        self.comboBox_id = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_id.setObjectName("comboBox_id")
        self.verticalLayout_3.addWidget(self.comboBox_id)
        self.comboBox_checkWork = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_checkWork.setObjectName("comboBox_checkWork")
        self.verticalLayout_3.addWidget(self.comboBox_checkWork)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_openCamera = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_openCamera.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_openCamera.setFont(font)
        self.btn_openCamera.setObjectName("btn_openCamera")
        self.verticalLayout_4.addWidget(self.btn_openCamera)
        self.btn_sqlite = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sqlite.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_sqlite.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sqlite.setFont(font)
        self.btn_sqlite.setAutoRepeatInterval(100)
        self.btn_sqlite.setObjectName("btn_sqlite")
        self.verticalLayout_4.addWidget(self.btn_sqlite)
        self.btn_takePhoto = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_takePhoto.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_takePhoto.setFont(font)
        self.btn_takePhoto.setObjectName("btn_takePhoto")
        self.verticalLayout_4.addWidget(self.btn_takePhoto)
        self.btn_train = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_train.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_train.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_train.setFont(font)
        self.btn_train.setObjectName("btn_train")
        self.verticalLayout_4.addWidget(self.btn_train)
        self.btn_recogniton = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_recogniton.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_recogniton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_recogniton.setFont(font)
        self.btn_recogniton.setObjectName("btn_recogniton")
        self.verticalLayout_4.addWidget(self.btn_recogniton)
        self.btn_refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_refresh.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_refresh.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout_4.addWidget(self.btn_refresh)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        Face_Recognition_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Face_Recognition_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName("menubar")
        Face_Recognition_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Face_Recognition_window)
        self.statusbar.setObjectName("statusbar")
        Face_Recognition_window.setStatusBar(self.statusbar)
        self.actionAdd_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionAdd_Person.setObjectName("actionAdd_Person")
        self.actionDelete_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelete_Person.setObjectName("actionDelete_Person")
        self.actionHelp = QtWidgets.QAction(Face_Recognition_window)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(Face_Recognition_window)
        self.actionExit.setObjectName("actionExit")
        self.actionauthor = QtWidgets.QAction(Face_Recognition_window)
        self.actionauthor.setObjectName("actionauthor")
        self.actionAddClass = QtWidgets.QAction(Face_Recognition_window)
        self.actionAddClass.setObjectName("actionAddClass")
        self.actionDelClass = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelClass.setObjectName("actionDelClass")
        self.actionAddCheck = QtWidgets.QAction(Face_Recognition_window)
        self.actionAddCheck.setObjectName("actionAddCheck")
        self.actionDelCheck = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelCheck.setObjectName("actionDelCheck")

        self.retranslateUi(Face_Recognition_window)
        QtCore.QMetaObject.connectSlotsByName(Face_Recognition_window)

    def retranslateUi(self, Face_Recognition_window):
        _translate = QtCore.QCoreApplication.translate
        Face_Recognition_window.setWindowTitle(_translate("Face_Recognition_window", "人脸识别1.0"))
        self.lab_frame.setText(_translate("Face_Recognition_window", "没有图像输入"))
        self.lab_selecCalss.setText(_translate("Face_Recognition_window", "选择人脸数据表(Face)"))
        self.lab_selecLable.setText(_translate("Face_Recognition_window", "选择学号(Face)"))
        self.lab_selecLable_2.setText(_translate("Face_Recognition_window", "选择考勤表(CheckWork)"))
        self.btn_openCamera.setText(_translate("Face_Recognition_window", "打开摄像头"))
        self.btn_sqlite.setText(_translate("Face_Recognition_window", "数据库管理"))
        self.btn_takePhoto.setText(_translate("Face_Recognition_window", "录入人脸"))
        self.btn_train.setText(_translate("Face_Recognition_window", "生成模型"))
        self.btn_recogniton.setText(_translate("Face_Recognition_window", "开始检测"))
        self.btn_refresh.setText(_translate("Face_Recognition_window", "刷新"))
        self.actionAdd_Person.setText(_translate("Face_Recognition_window", "添加人脸"))
        self.actionDelete_Person.setText(_translate("Face_Recognition_window", "删除人脸"))
        self.actionHelp.setText(_translate("Face_Recognition_window", "操作细节"))
        self.actionExit.setText(_translate("Face_Recognition_window", "退出"))
        self.actionauthor.setText(_translate("Face_Recognition_window", "关于作者"))
        self.actionAddClass.setText(_translate("Face_Recognition_window", "添加人脸数据表"))
        self.actionDelClass.setText(_translate("Face_Recognition_window", "删除人脸数据表"))
        self.actionAddCheck.setText(_translate("Face_Recognition_window", "添加考勤表"))
        self.actionDelCheck.setText(_translate("Face_Recognition_window", "删除考勤表"))

