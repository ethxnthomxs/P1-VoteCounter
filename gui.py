from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.setObjectName("verticalLayout")

        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("font-size: 24px; color: white;")
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)

        self.userIdInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userIdInput.setPlaceholderText("Enter Voting ID")
        self.userIdInput.setFixedHeight(30)
        self.userIdInput.setStyleSheet("font-size: 16px; padding: 4px;")
        self.userIdInput.setObjectName("userIdInput")
        self.verticalLayout.addWidget(self.userIdInput)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.johnRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.johnRadio.setStyleSheet("font-size: 18px; color: white;")
        self.johnRadio.setObjectName("johnRadio")
        self.horizontalLayout.addWidget(self.johnRadio)

        self.janeRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.janeRadio.setStyleSheet("font-size: 18px; color: white;")
        self.janeRadio.setObjectName("janeRadio")
        self.horizontalLayout.addWidget(self.janeRadio)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.voteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.voteButton.setMinimumSize(QtCore.QSize(160, 40))
        self.voteButton.setObjectName("voteButton")
        self.verticalLayout.addWidget(self.voteButton)

        self.resultButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resultButton.setMinimumSize(QtCore.QSize(160, 40))
        self.resultButton.setObjectName("resultButton")
        self.verticalLayout.addWidget(self.resultButton)

        self.statusLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.statusLabel.setStyleSheet("font-size: 14px; color: #eeeeee;")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)

        self.resultLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultLabel.setText("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultLabel.setStyleSheet("font-size: 14px; color: #eeeeee;")
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vote Now"))
        self.titleLabel.setText(_translate("MainWindow", "Choose Your Candidate"))
        self.johnRadio.setText(_translate("MainWindow", "John"))
        self.janeRadio.setText(_translate("MainWindow", "Jane"))
        self.voteButton.setText(_translate("MainWindow", "Vote"))
        self.resultButton.setText(_translate("MainWindow", "Show Results"))
