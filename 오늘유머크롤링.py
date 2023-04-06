# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청(통신)
import urllib.request
#특정한 주제를 필터링(정규표현식)
import re 

#웹소에서 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}


# 크롤링결과를 파일로 저장(r: raw string notation)
# 기존 내용에 추가(a+: append + read +write)
f=open(r"c:\work\2dayhumor.txt", "a+", encoding="utf-8") 

#이 사이트 페이지는 1~10
for n in range(1,11):
        #오유 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가(난 웹브라우져가 아닌데 인척하는 조치)
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지면 유니코드를 다시 해석
        page = data.decode('utf-8', 'ignore') #깨지는 것 무시
        soup = BeautifulSoup(page, 'html.parser') #파싱
        list = soup.find_all('td', attrs={'class':'subject'})
        #태그 확인용 소스(주석처리)
        #<td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=466744&amp;s_no=466744&amp;page=1" target="_top">
        # 우리를 악에서 구하소서</a><span class="list_memo_count_span"> [26]</span>  <span style="margin-left:4px;">
        # <img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> 
        # </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_pencil.gif?2" alt="창작글" style="margin-right:3px;top:2px;position:
        # relative"> </td>

        for item in list:
                try:
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        title = item.find('a').text.strip()
                        # print(title)
                        if (re.search('한국', title)):
                                print(title.strip())
                                f.write(title.strip()+"\n")
                except:
                        pass
        
f.close()