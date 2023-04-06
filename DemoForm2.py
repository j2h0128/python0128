# DemoForm2.py(로직 코딩) + DemoForm2.ui(화면을 XML문서 저장) 
import sys 
#Qt패키지를 임포트 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹사이트에 페이지 실행을 요청 
import requests
from bs4 import BeautifulSoup 


#디자인 문서를 로딩 
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0] 
#윈도우 클래스 정의(좀 더 기능이 많은 창 QMainWindow) 
class DemoForm(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
    def firstclick(self): 
        url="https://www.daangn.com/"
        response=requests.get(url)
        #검색이 용이한 객체 생성
        soup=BeautifulSoup(response.text, "html.parser")

        posts=soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title= post.find("h2", attrs={"class":"card-title"})
            price= post.find("h2", attrs={"class":"card-price"})
            addr= post.find("h2", attrs={"class":"card-region-name"})
            print("{0}, {1}, {2}".format(title, price, addr))
        self.label.setText("첫번째 버튼") 
    def secondclick(self): 
        self.label.setText("두번째 화면") 
    def thirdclick(self): 
        self.label.setText("세번째 화면~~") 

#모듈을 직접 실행했는지를 체크 
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    demoForm = DemoForm() 
    demoForm.show() 
    app.exec_()