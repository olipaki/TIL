import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o-mini"

##############대화 내역을 저장할 리스트
messages = [
    {"role": "system", "content": "당신은 AI관련해서 40년경력의 이해하기쉽게 예시를 잘 만드는 강사."}
]

print("=== 챗봇 대화 시작 (종료하려면 'exit' 입력) ===")

while True:
    # 3. 사용자 입력 받기
    user_input = input("나: ")
    
    if user_input.lower() == "exit":
        print("챗봇을 종료합니다.")
        break

    # 4. 사용자 질문을 대화 내역에 추가
    messages.append({"role": "user", "content": user_input})

    # 5. 선생님 방식의 API 요청 설정
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
        "model": model,
        "messages": messages  # 전체 대화 내역을 보냄
    }

    # 6. API 호출 및 결과 처리
    response = requests.post(URL, headers=headers, json=payload)
    res_json = response.json()

    # 에러 발생 시 처리
    if 'choices' not in res_json:
        print("❌ 에러 발생!")
        pprint(res_json)
        break

    # 7. 답변 추출 및 출력
    content = res_json['choices'][0]['message']['content']
    print(f"AI: {content}")

    # 8. AI의 답변도 대화 내역에 추가 (다음 대화의 맥락을 위해)
    messages.append({"role": "assistant", "content": content})













    

######################

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {OPENAI_API_KEY}"
# }
# d
# payload = {
#     "model": model,
#     "messages": [
#         {"role": "system", "content": "당신은 AI관련해서 40년경력의 이해하기쉽게 예시를 잘 만드는 강사."},
#         {"role": "user", "content": "Chat Completions API가 뭐야? 2~3문장으로 답변해줘"}
#     ]
# }

# response = requests.post(URL, headers=headers, json=payload)
# pprint(response.json())
# print(response.json()['choices'][0]['message']['content'])

# ##################세번쨰
# from openai import OpenAI

# client = OpenAI(api_key=OPENAI_API_KEY)

# completion = client.chat.completions.create(
#     model=model,
#     messages=[
#         {"role": "user", "content": "Openai SDK를 사용하면 어떤 점이 좋아?"}
#     ]
# )

# print(completion.choices[0].message.content)