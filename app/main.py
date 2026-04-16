import logging
import time
from fastapi import FastAPI, Request
from app.api.routers.url_router import router as url_router


app = FastAPI()

app.include_router(url_router, tags=["URLs"])

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger("api-performance")



#@app.middleware("http")
#async def log_request_time(request: Request, call_next):
#    start_time = time.perf_counter() # Marca o início com precisão
#    
#    response = await call_next(request) # Executa a rota (seu código)
#    
#    process_time = time.perf_counter() - start_time
#    # Converte para milissegundos para facilitar a leitura
#    ms_time = process_time * 1000 
#    
#    # Log formatado: Método | Rota | Status | Tempo
#    logger.info(
#        f"Method: {request.method} | Path: {request.url.path} | "
#        f"Status: {response.status_code} | Duration: {ms_time:.2f}ms"
#    )
#    
#    # Opcional: Adicionar o tempo no Header da resposta para o cliente ver
#    response.headers["X-Process-Time"] = f"{ms_time:.2f}ms"
#    
#    return response