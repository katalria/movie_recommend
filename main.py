# fast 서버 관련 패키지
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

# langchain 관련 패키지
from langchain_openai import ChatOpenAI





class My_App():
    """
    fastapi 및 langchain 클래스 생성
    """
    def __init__(self):

        # FastAPI 객체 생성
        self.app = FastAPI()

    
    def setup_routes(self):
        @self.app.get("/healthy")
        def healthy_check():
            """
            서버 healthy check용 fastapi 함수
            """
            return JSONResponse(content={"status": "ok"}, status_code=200)
        
        @self.app.post("/chat")
        def chat(request, app: My_App = Depends(self.get_instance)):
            """
            사용자의 질의를 받아서 llm으로 답변을 하는 함수
            """
            response = {}
                    
            llm = ChatOpenAI(
                temperature=0.1,  
                model_name="gpt-3.5-turbo", 
            )


            response = llm.invoke(request)
            
            
            return response
        