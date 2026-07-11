from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Dave's API", "status": "running"}

@app.get("/info")
def info():
    return {
        "name": "Dave Aashisth Tummala",
        "track": "Backend AI Engineering",
        "program": "FlyRank AI Internship",
        "project": "Pawk - Geospatial Analytics Platform"
    }
