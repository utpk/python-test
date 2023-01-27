from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/201", status_code=201)
async def r201():
    return {"message": "created"}

@app.get("/404", status_code=404)
async def r404():
    return {"message": "not found"}

@app.get("/500", status_code=500)
async def r500():
    return {"message": "something went wrong"}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        proxy_headers=True,
        server_header=False,
        forwarded_allow_ips="*",
    )
