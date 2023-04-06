#DemoForm.py
#DemoForm.ui(화면단) +DemoForm.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#화면을 로딩
form_class=uic.loadUiType('DemoForm.ui')[0]
#위도우(폼)클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모")

#직접 이 모듈을 실행한 경우 체크
if __name__ == "__main__":
    app=QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()