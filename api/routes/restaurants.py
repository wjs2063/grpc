from fastapi import APIRouter
from schemas.orders import OrderCreate

router = APIRouter()

@router.post(
    "",
    status_code=201,
    name="create_order",
)
def create_order(
        order_create: OrderCreate,
):
    return {"Say": "Order created!"}