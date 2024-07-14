from fastapi import APIRouter
import api.routes.restaurants as restaurants



api_router = APIRouter()
api_router.include_router(restaurants.router,prefix="/api/restaurants")

