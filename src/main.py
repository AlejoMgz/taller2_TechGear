from fastapi import FastAPI, HTTPException, status
from bson import ObjectId
from typing import List

from src.database import get_database
from src.models.product_model import ProductoSchema, ProductoResponseSchema
from src.models.order_model import PedidoSchema, PedidoResponseSchema
from src.models.user_model import UsuarioSchema, UsuarioResponseSchema

app = FastAPI(
    title="TechGear API",
    version="1.0.0",
    description="API REST con CRUD de Productos, Registro de Pedidos y Esquema de Usuarios"
)

db = get_database()

def helper_id(doc) -> dict:
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


# RUTAS DE PRODUCTOS (CRUD)


@app.post("/productos/", response_model=ProductoResponseSchema, status_code=status.HTTP_201_CREATED, tags=["Productos"])
def crear_producto(producto: ProductoSchema):
    producto_dict = producto.dict()
    nuevo = db.productos.insert_one(producto_dict)
    creado = db.productos.find_one({"_id": nuevo.inserted_id})
    return helper_id(creado)

@app.get("/productos/", response_model=List[ProductoResponseSchema], tags=["Productos"])
def listar_productos():
    productos = list(db.productos.find())
    return [helper_id(p) for p in productos]

@app.get("/productos/{producto_id}", response_model=ProductoResponseSchema, tags=["Productos"])
def obtener_producto(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID no válido")
    prod = db.productos.find_one({"_id": ObjectId(producto_id)})
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return helper_id(prod)

@app.put("/productos/{producto_id}", response_model=ProductoResponseSchema, tags=["Productos"])
def actualizar_producto(producto_id: str, producto: ProductoSchema):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID no válido")
    resultado = db.productos.update_one({"_id": ObjectId(producto_id)}, {"$set": producto.dict()})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    prod = db.productos.find_one({"_id": ObjectId(producto_id)})
    return helper_id(prod)

@app.delete("/productos/{producto_id}", status_code=status.HTTP_200_OK, tags=["Productos"])
def eliminar_producto(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID no válido")
    resultado = db.productos.delete_one({"_id": ObjectId(producto_id)})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}


# RUTAS DE PEDIDOS (Registro y Consulta)


@app.post("/pedidos/", response_model=PedidoResponseSchema, status_code=status.HTTP_201_CREATED, tags=["Pedidos"])
def crear_pedido(pedido: PedidoSchema):
    pedido_dict = pedido.dict()
    nuevo = db.pedidos.insert_one(pedido_dict)
    creado = db.pedidos.find_one({"_id": nuevo.inserted_id})
    return helper_id(creado)

@app.get("/pedidos/", response_model=List[PedidoResponseSchema], tags=["Pedidos"])
def listar_pedidos():
    pedidos = list(db.pedidos.find())
    return [helper_id(p) for p in pedidos]

# RUTA INICIAL Y VERIFICACIÓN

@app.get("/", tags=["Inicio"])
def inicio():
    return {"message": "API TechGear en funcionamiento"}