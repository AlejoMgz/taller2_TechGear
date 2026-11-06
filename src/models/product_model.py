from pydantic import BaseModel, Field
from typing import Optional

class ProductoSchema(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre del producto tecnológico")
    descripcion: str = Field(..., max_length=500, description="Descripción detallada del hardware o accesorio")
    precio: float = Field(..., gt=0, description="Precio unitario")
    stock: int = Field(..., ge=0, description="Cantidad disponible en inventario")
    categoria: str = Field(..., description="Categoría del producto")
    imagen_url: Optional[str] = Field(None, description="URL de la imagen")

class ProductoResponseSchema(ProductoSchema):
    id: str = Field(..., description="ID único generado por MongoDB")