from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QTimer
from twilio.rest import TwilioRestClient
import sys, design


class SMSApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.send_btn.clicked.connect(self.send_sms)

    def send_sms(self):
        account_ssid = ''
        auth_token = ''
        client = TwilioRestClient(account_ssid, auth_token)
        twilio_number = ''
        cellphone_number = str(self.lineEdit.text())
        try:
            message = client.messages.create(body=str(self.textEdit.toPlainText()), from_=twilio_number, to=cellphone_number)
            self.label_3.setText("Message Sent!")
        except HTTPError:
            self.label_3.setText("Something went wrong!")

    def normal_status(self):
        self.label_3.setText("Status")

def main():
    app = QtGui.QApplication(sys.argv)
    form = SMSApp()
    form.show()
    timer = QTimer()
    timer.timeout.connect(form.normal_status)
    timer.start(10000)
    #timer.singleShot(0, form.normal_status)
    app.exec_()


if __name__ == '__main__':
    main()
