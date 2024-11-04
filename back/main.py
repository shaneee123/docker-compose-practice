from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongodb_config import counter_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] to limit to specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize count document if it doesn't exist
@app.on_event("startup")
async def startup_event():
    if counter_collection.count_documents({}) == 0:
        counter_collection.insert_one({"_id": 1, "count": 0})

@app.post("/increment")
def increment_count():
    counter_collection.update_one({"_id": 1}, {"$inc": {"count": 1}})
    count = counter_collection.find_one({"_id": 1})["count"]
    return {"count": count}

@app.post("/decrement")
def decrement_count():
    counter_collection.update_one({"_id": 1}, {"$inc": {"count": -1}})
    count = counter_collection.find_one({"_id": 1})["count"]
    return {"count": count}

@app.get("/count")
def get_count():
    count = counter_collection.find_one({"_id": 1})["count"]
    return {"count": count}

