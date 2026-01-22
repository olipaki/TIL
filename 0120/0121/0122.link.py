import os
from dotenv import load_dotenv
import urllib.request
import json
import streamlit as st

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

# 페이지 설정
st.set_page_config(
    page_title="네이버 뉴스 검색기",
    page_icon="📰",
    layout="wide"
)

# 커스텀 CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .news-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .news-title {
        font-size: 20px;
        font-weight: bold;
        color: #222;
        margin-bottom: 10px;
    }
    .news-desc {
        color: #555;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    .news-date {
        color: #999;
        font-size: 13px;
    }
    h1 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.title("📰 네이버 뉴스 검색기")

# 검색 입력
col1, col2 = st.columns([3, 1])
with col1:
    search_keyword = st.text_input("검색어를 입력하세요", placeholder="예: 파이썬, AI, 주식...")
with col2:
    st.write("")
    st.write("")
    search_button = st.button("🔍 검색", use_container_width=True)

# 검색 실행
if search_button and search_keyword:
    with st.spinner(f"'{search_keyword}' 검색 중..."):
        try:
            encText = urllib.parse.quote(search_keyword)
            url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
            
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            
            if rescode == 200:
                response_body = response.read()
                data = json.loads(response_body.decode('utf-8'))
                
                # 결과 표시
                st.success(f"✅ 총 {len(data['items'])}개의 기사를 찾았습니다!")
                
                if len(data['items']) == 0:
                    st.warning("😢 검색 결과가 없습니다. 다른 검색어로 시도해보세요.")
                else:
                    # 뉴스 카드 표시
                    for idx, item in enumerate(data['items'], 1):
                        clean_title = item['title'].replace("<b>", "").replace("</b>", "").replace("&quot;", '"').replace("&apos;", "'")
                        clean_desc = item['description'].replace("<b>", "").replace("</b>", "").replace("&quot;", '"').replace("&apos;", "'")
                        link = item['link']
                        pub_date = item['pubDate']
                        
                        with st.container():
                            st.markdown(f"""
                            <div class="news-card">
                                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                    <span style="background: linear-gradient(135deg, #667eea, #764ba2); 
                                                 color: white; padding: 5px 12px; border-radius: 15px; 
                                                 font-size: 13px; font-weight: bold; margin-right: 10px;">
                                        #{idx}
                                    </span>
                                </div>
                                <div class="news-title">{clean_title}</div>
                                <div class="news-desc">{clean_desc}</div>
                                <div class="news-date">📅 {pub_date}</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            st.link_button("기사 읽기 →", link, use_container_width=False)
                            st.divider()
            else:
                st.error(f"❌ Error Code: {rescode}")
                
        except Exception as e:
            st.error(f"❌ 오류가 발생했습니다: {e}")
            st.info("💡 API 키가 올바른지, 인터넷 연결 상태를 확인해주세요.")

elif search_button and not search_keyword:
    st.warning("⚠️ 검색어를 입력해주세요!")

# 사이드바 정보
with st.sidebar:
    st.header("ℹ️ 사용 방법")
    st.write("""
    1. 검색어를 입력하세요
    2. '검색' 버튼을 클릭하세요
    3. 결과를 확인하세요!
    """)
    
    st.divider()
    
    st.header("📌 검색 팁")
    st.write("""
    - 구체적인 키워드 사용
    - 최신 뉴스는 날짜 포함
    - 복합 키워드로 정확도 향상
    """)
    
    if client_id:
        st.success("✅ API 연결됨")
    else:
        st.error("❌ API 키를 확인하세요")