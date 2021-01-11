# inflearn 웹스크래핑 무료 강의

* 강의, 제대로 된 수업없이 구글링을 통해서 하나하나 공부하다보니
* 더 좋은 방법이나 제대로 구현할 수 없는 부분이 많아서 강의 듣기 시작. ! 

* request, 셀레니움 강의

* 동적 웹 스크래핑
* headless Chrome
  + 창을 띄우지 않고 더 빠르게 웹 스크래핑 가능
  + 서버에서 웹 스크래핑 가능 AWS와 함께 사용가능 할 것 같다. 

* Requests vs 셀레니움
* 기억 나는 몇가지 문법

   + .(ca.e) -> cave cafe 등
   + ^ (^de) -> desk detination 
   + $ (se$) -> base 등
   + match() 처음부터 일치하는 것 search() 문자열중 일치하는 패턴 findall() 일치하는 것 모두 리스트로 반환
   + User-Agent 사용자의 유입경로에 따라 서버에서 보여주는 UI를 다르게 해줌
   + 셀리니움 find_element(s)_by_id.text
   + 웹페이지까지 로딩 기다려주기 elem = WebdriverWait(browser,10).until(EC.presence_of_element_located((B Y.XPATH,"//*[@id='content']")))
   + 자동 스크롤링
   + BeautifulSoup

     - find_next_sibling(s)

     - find_previous_sibling(s)

       -soup["href"]

     - soup.get_text()
