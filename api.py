from models import NewTxnApiRes, Paytm_api_call, TxnStsApiRes
import requests
import json
import os

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
from paytmchecksum import PaytmChecksum


# for Staging
# url = "https://securegw-stage.paytm.in/paymentservices/qr/create"

# for Production
url = "https://securegw.paytm.in/paymentservices/qr/create"

def generate_post_data(amount: int, id: str):
    paytmParams = dict()
    paytmParams["body"] = {
        "mid"           : os.getenv("MERCHANT_ID"),
        "orderId"       : id,
        "amount"        : str(amount),
        "businessType"  : "UPI_QR_CODE",
        "posId"         : "S12_1632"
    }
    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), os.getenv("MERCHANT_KEY"))
    paytmParams["head"] = {
        "clientId"	        : "C11",
        "version"	        : "v1",
        "signature"         : checksum
    }
    print(paytmParams)

    return json.dumps(paytmParams)

def paytm_api_call(paytm:Paytm_api_call):
    post_data = generate_post_data(paytm.amount, paytm.orderId)
    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
    print(response)
    return NewTxnApiRes(**response)

def create_new_task():
    return True

def transaction_status(mid,order_id):
    result = {
        "resultInfo": {
            "resultStatus": "TXN_SUCCESS",
            "resultCode": "01",
            "resultMsg": "Txn Success"
        },
        "txnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "bankTxnId": "xxxxxxxxxxxxxxx",
        "orderId": "xxxxxxx",
        "txnAmount": "100.00",
        "txnType": "SALE",
        "gatewayName": "HDFC",
        "bankName": "HSBC",
        "mid": "xxxxxxxxxxxxxxxxxxxx",
        "paymentMode": "CC",
        "refundAmt": "100.00",
        "txnDate": "2019-02-20 12:35:20.0",
        "authRefId": "50112883"
    }

    return TxnStsApiRes(**result)
       