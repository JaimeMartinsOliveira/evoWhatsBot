from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()
    print("Recebido webhook:", payload)

    return {"message": "Webhook recebido com sucesso"}