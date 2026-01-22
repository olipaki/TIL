import os
from dotenv import load_dotenv # os사용위한 추가
import sys
import urllib.request
import json

load_dotenv()

# 이 부분을 꼭 따옴표로 감싸주세요!
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")  # 이미지에 있던 값입니다. 앞뒤에 따옴표 필수!

print(f"ID 로드 확인: {client_id}") # 제대로 불러왔는지 테스트용

# 검색어 설정
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

try:
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode == 200):
        response_body = response.read()
        data = json.loads(response_body.decode('utf-8'))
        
        # 제목만 깔끔하게 출력
        for item in data['items']:
            # <b> 태그 제거 후 출력
            clean_title = item['title'].replace("<b>", "").replace("</b>", "")
            print(f"[주식] {clean_title}")
    else:
        print("Error Code:" + str(rescode))
        
except Exception as e:
    print(f"연결 오류가 발생했습니다: {e}")