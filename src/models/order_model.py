from pydantic import BaseModel, Field
from typing import List

class ItemPedidoSchema(BaseModel):
    producto_id: str = Field(..., description="ID del producto solicitado")
    cantidad: int = Field(..., gt=0, description="Cantidad de unidades")
    precio_unitario: float = Field(..., gt=0, description="Precio unitario al comprar")

class PedidoSchema(BaseModel):
    cliente_id: str = Field(..., description="Identificador o email del cliente")
    items: List[ItemPedidoSchema] = Field(..., description="Lista de productos en el pedido")
    total: float = Field(..., gt=0, description="Monto total del pedido")
    estado: str = Field(default="Pendiente", description="Estado actual del pedido")

class PedidoResponseSchema(PedidoSchema):
    id: str = Field(..., description="ID único del pedido generado por MongoDB")