from fastapi import FastAPI
from routers import users, pets, inventory, transactions, mini_games, leaderboard
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Guinea Games API")

app.include_router(users.router)
app.include_router(pets.router)
app.include_router(inventory.router)
app.include_router(transactions.router)
app.include_router(mini_games.router)
app.include_router(leaderboard.router)

@app.get("/")
def root():
    return {"message": "Welcome to Guinea Games Backend"}