# import redis
# from fastapi import FastAPI

# app = FastAPI()

# redis_client = redis.Redis(
#     host = "localhost",
#     port = 6379,
#     decode_responses = True
# )

# @app.get("/test")
# def test_redis():
    
#     redis_client.set("name", "rahul")
    
#     name = redis_client.get("name")
    
#     return {
#         "name":name
#     }
    
    
import redis 
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses= True
)

@app.get("/test")
def test_redis():
    
    redis_client.set("name","rahulsingh")
    
    name = redis_client.get("name")
    
    return {
        "name":name
    }