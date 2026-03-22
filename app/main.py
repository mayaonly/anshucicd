from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on EC2. and we are checking changes "}

# Health check route
@app.get("/health")
def health():
    return {"status": "OK"}

# Dynamic route
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name} 👋"}

# Example POST route
@app.post("/data")
def receive_data(data: dict):
    return {
        "received": data,
        "message": "Data received successfully"
    }

