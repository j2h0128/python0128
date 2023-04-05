#web1.py

#크롤링
from bs4 import BeautifulSoup

#웹페이지를 로딩
page=open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 스프객체 생성
soup=BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#문서 안에 있는 <P>를 전부 검색
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#검색조건: <P class='outer-text'>
print(soup.find_all("P", class_="outer-text"))

#<p> attrs=>attributes
print(soup.find_all("P", attrs={"class":"outer-text"}))

#id=first 검색
print(soup.find_all(id="first"))

#태그의 컨텐츠만 리턴(.text)
for tag in soup.find_all("p"):
    title=tag.text.strip()
    title=title.replace("\n", "")
    print(title)

