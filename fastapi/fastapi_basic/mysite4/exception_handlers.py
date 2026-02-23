# mysite4/exception_handlers.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from mysite4.exceptions import AppException


def register_exception_handlers(app: FastAPI):
    """앱에 예외 핸들러들을 등록하는 함수"""

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500, content={"detail": "서버 내부 오류가 발생했습니다."}
        )
