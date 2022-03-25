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
create_url = "https://securegw.paytm.in/paymentservices/qr/create"
txn_url = "https://securegw.paytm.in/v3/order/status"

def generate_post_data(amount: int, id: str):
    paytmParams = dict()
    paytmParams["body"] = {
        "mid": os.getenv("MERCHANT_ID"),
        "orderId": id,
        "amount": str(amount),
        "businessType": "UPI_QR_CODE",
        "posId": "S12_1632",
    }
    checksum = PaytmChecksum.generateSignature(
        json.dumps(paytmParams["body"]), os.getenv("MERCHANT_KEY")
    )
    paytmParams["head"] = {"clientId": "C11", "version": "v1", "signature": checksum}
    print(paytmParams)
    return json.dumps(paytmParams)


def generate_txn_get_data(orderid: str):
    paytmParams = dict()
    paytmParams["body"] = {
        "mid": os.getenv("MERCHANT_ID"),
        "orderId": orderid,
    }
    checksum = PaytmChecksum.generateSignature(
        json.dumps(paytmParams["body"]), os.getenv("MERCHANT_KEY")
    )
    paytmParams["head"] = {"signature": checksum}
    return json.dumps(paytmParams)


def paytm_api_call(paytm: Paytm_api_call):
    post_data = generate_post_data(paytm.amount, paytm.orderId)
    response = requests.post(
        create_url, data=post_data, headers={"Content-type": "application/json"}
    ).json()
    print(response)
    return NewTxnApiRes(**response["body"])


def create_new_task():
    return True


def transaction_status(mid, order_id):
    post_data = generate_txn_get_data(order_id)
    response = requests.post(txn_url, data = post_data, headers = {"Content-type": "application/json"}).json()
    print(response)
    return TxnStsApiRes(**response["body"])
