# -VPN 필수로 사용하면 차단 위험성 저하(티켓팅)
# -크롤링 브라우저 코멧


import requests

response = requests.get("https://www.naver.com/")

print(response.text)
