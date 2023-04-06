# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청(통신)
import urllib.request
#특정한 주제를 필터링(정규표현식)
import re 

#웹소에서 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가(난 웹브라우져가 아닌데 인척하는 조치)
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지면 유니코드를 다시 해석
        page = data.decode('utf-8', 'ignore') #깨지는 것 무시
        soup = BeautifulSoup(page, 'html.parser') #파싱
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        title = item.text 
                        print(title.strip())
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                except:
                        pass
        
