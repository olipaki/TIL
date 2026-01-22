import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 1. 환경변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"

# 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="AI 강사 챗봇", page_icon="🎓")

st.write("연결 테스트 중입니다!") # <-- 이 줄을 추가하고 저장해 보세요.
st.title("👨‍🏫 친절한 AI 강사님")
st.caption("OpenAI API와 Streamlit을 이용한 실시간 챗봇입니다.")

# 2. 대화 기록 초기화 (세션 상태 관리)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "당신은 친절한 AI 강사입니다."}
    ]

# 3. 화면에 기존 대화 내용 표시 (말풍선 UI)
for msg in st.session_state.messages:
    if msg["role"] != "system": # 시스템 메시지는 화면에 표시 안 함
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 4. 사용자 입력창 (화면 하단에 고정됨)
if prompt := st.chat_input("질문을 입력하면 AI 강사가 답변해 드립니다."):
    
    # 사용자 메시지 저장 및 화면 표시
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 5. API 호출 (선생님 방식)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": st.session_state.messages
    }

    # 6. AI 답변 처리 (로딩 애니메이션 추가)
    with st.chat_message("assistant"):
        with st.spinner("생각 중..."): # 답변 생성 중 애니메이션
            response = requests.post(URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                answer = response.json()['choices'][0]['message']['content']
                st.write(answer)
                # AI 답변 저장
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("API 호출에 실패했습니다. 키나 잔액을 확인하세요.")
                st.write(response.json())