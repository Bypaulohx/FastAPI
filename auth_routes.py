from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"message": "Você acessou a rota padrão de autenticação!", "autenticado": False}
