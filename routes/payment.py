import sys
from datetime import datetime, timedelta

from fastapi import APIRouter, Request
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from os import getenv
from paypalcheckoutsdk.orders import OrdersCreateRequest
from fastapi.responses import JSONResponse

payment_routes = APIRouter()

client_id = getenv('CLIENT_ID')
client_secret = getenv('CLIENT_SECRET')

enviroment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(enviroment)


@payment_routes.post("/create-order")
async def create_order_paypal(request: Request):
    try:
        data = await request.json()
        request = OrdersCreateRequest()
        time_expire=datetime.now() + timedelta(minutes=1)
        request.prefer('return=representation')
        request.request_body(
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "USD",
                            "value": "100.00"
                        }
                    }
                ],
                "items": data,
                "application_context": {
                    "expire_time": f"{time_expire.isoformat()}Z"
                }
            }
        )
        response = client.execute(request)
        response.result.__dict__["expire_time"] = f"{time_expire.isoformat()}Z"
        return JSONResponse(content={"id": response.result.id})
    except Exception as ex:
        print(ex)
        print(sys.exc_info()[-1].tb_lineno)
