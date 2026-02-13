import os
from dotenv import load_dotenv
from openai import OpenAI

####################
from fastapi import APIRouter  # 추가됨
from fastapi.responses import StreamingResponse  # 추가됨

router = APIRouter(prefix="/sse", tags=["SSE (Server-Sent Events)"])

load_dotenv()
router = APIRouter(prefix="/sse", tags=["SSE (Server-Sent Events)"])
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@router.get("/chat-normal")
def openai_chat_normal(message: str = "안녕하세요, 자기소개 해주세요."):
    """
    OpenAI API 일반 응답 (스트리밍 X)
    → 전체 응답이 한 번에 도착 (스트리밍과 비교용)
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="2문장 이내로 대답해줘.",
        input=[{"role": "user", "content": message}],
    )
    return {"message": response.output_text}


@router.get("/chat")
def openai_chat(message: str = "안녕하세요, 자기소개 해주세요."):
    """
    실제 OpenAI API 스트리밍
    → GPT가 생성하는 답변이 토큰 단위로 실시간 도착
    """
    stream = client.responses.create(
        model="gpt-4o-mini",
        instructions="2문장 이내로 대답해줘.",
        input=[{"role": "user", "content": message}],
        stream=True,
    )

    def generate():
        for event in stream:
            if event.type == "response.output_text.delta":
                yield f"data: {event.delta}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
