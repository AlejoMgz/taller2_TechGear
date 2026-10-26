from pydantic import BaseModel, EmailStr, Field

class UsuarioSchema(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre completo del usuario")
    email: EmailStr = Field(..., description="Correo electrónico del usuario")
    password: str = Field(..., min_length=6, description="Contraseña del usuario")
    rol: str = Field(default="cliente", description="Rol del usuario (cliente/admin)")

class UsuarioResponseSchema(BaseModel):
    id: str = Field(..., description="ID único generado por MongoDB")
    nombre: str
    email: EmailStr
    rol: str