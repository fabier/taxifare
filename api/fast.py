from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "TaxiFare API is running"}

@app.get("/predict")
def predict(passenger_count: int):

    fare = passenger_count * 2.5

    return {
        "fare_amount": fare
    }
