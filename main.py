from itertools import count
from time import time
from urllib import request
from uuid import uuid4
from fastapi import FastAPI
from datetime import datetime
from api import create_new_task, paytm_api_call, transaction_status
from db import get_request_from_db, store_new_request_to_db

from models import DrinkType, NewteaModel, Paytm_api_call, TeaRequests

app = FastAPI()

MERCHANT_ID = '123456'
POS_ID = "lajksdkljdfhj"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tea/new")
def newtea(tea:NewteaModel):
    # Calculate Date

    newdata = TeaRequests(
        key = uuid4().hex,
        time = datetime.now(),
        machine_number= tea.machine_number,
        amount=tea.amount,
        status="New Request",
        config=tea.config,
        type = tea.type,
        orderId = uuid4().hex,
        quantity= tea.count
    )
    
    # Store request in db
    
    store_new_request_to_db(newdata)

    # Check Status and Levels

    if  tea.config :
        if tea.config.water_level < 10:
            return 'Not Enough Water'
        if tea.type == DrinkType.TEA and tea.config.tea_powder < 10:
            return 'Not Enough Tea Powder'
        if tea.type == DrinkType.COFFEE and tea.config.coffee_power < 10:
            return 'Not Enough Coffee Powder'

    # Call paytm api
    data = Paytm_api_call(
        mid = MERCHANT_ID,
        orderId = newdata.orderId,
        amount = newdata.amount,
        businessType="UPI_QR_CODE",
        posId=POS_ID
    )

    result = paytm_api_call(data)
    
    # Check result status

    if result.resultInfo.resultStatus != 'SUCCESS':
        return "API Generation Failed"
        
    # Update status in DB 
    newdata.status = "QR GENERATED"
    store_new_request_to_db(newdata)

    # Create new task to poll txn resul api.

    create_new_task()
    # return qr response

    return {
        'qr' : result.qrData,
        'request_id': newdata.key
    }


@app.get("/payment/status/{request_id}")
def get_payment_status(request_id:str):
    request = get_request_from_db(request_id)
    
    # request exists?
    if request is None:
        return "Request Not Found"
    # request status check

    # Paytm api call
    transaction = transaction_status(MERCHANT_ID,request.orderId)

    # update request status
    request.status = transaction.resultInfo.resultStatus
    store_new_request_to_db(request)

    if transaction.resultInfo.resultStatus == 'TXN_SUCCESS':
        return {
            'amount' : transaction.txnAmount,
            'status' : "SUCCESS"

        }
    if transaction.resultInfo.resultStatus == 'PENDING':
        return {
            'amount' : transaction.txnAmount,
            'status' : "PENDING"
        }

    return False
