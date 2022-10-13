from fastapi import FastAPI

# Define application
app = FastAPI(
    title="ML/DL App",
    description="Classify machine learning projects.",
    version="0.1",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to ML/DL App."}
