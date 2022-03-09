from models import NewTxnApiRes, Paytm_api_call, TxnStsApiRes


def paytm_api_call(paytm:Paytm_api_call):

    result = {
        "resultInfo": {
            "resultStatus": "SUCCESS",
            "resultCode": "QR_0001",
            "resultMsg": "SUCCESS"
        },
        "qrCodeId": "2800005050XXXXX2NNGLX9TW",
        "qrData": "upi://pay?pa=paytm-53438207@paytm&pn=Paytm%20Payment&mc=5499&tr=ord_1591357977&am=1&cu=INR&paytmqr=2800005050XXXXX2NNGLX9TW",
        "image": "iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAQAAAABVr4M4AAAEKUlEQVR42u2dPZIjMQiF5erAYR/BR/HReo7mo/gIDh24zLaAh9D8JbvJNq+DXbtHnyahBDwQ0+QvnkaYMGHC/wK+N3uu93aW9/7idnmcXyeRj3bZV7xb2/Yxxxxxpy1fCleBVX39c5dHaCdajjC3rPxKx7dr6xC6ES8FPrHgusCd7hoWJGta+3aprdnMkXBLezyOzHnmc7f+7W9j+jx5M0nchXBvuK7phmWf6aDiGuqm9uoWJEC4Ku6/aPxjcVvNMejDtazbp+8ZR9a2jI3xsOKJe9UO6y28ffgiZCR8ZjufuhtV6aqTbIcQRC4i7qa0/JN+EDw33729ELe6ZzCHh2ZA2I1nyXQiXgtUhiRqWiyzNbE9jHY2DEev4jwiXgkVjXMuWX25GWGFRL5Ilj2w8RyJcCLZgRdMejXpNSZHhtNTm4KssfdqGryJcAe5nDTIiEeTPul1X+c2w8At60OOSHOFKsPkh/T4fQzc7mFTuT75qPsMIV4Bdpc1Rr1WA7EP2Vd2fPbU4dBvJN+EKsBf81J5garr0allTKiHfmku6SeslXAD2grF+94zIfZWeNWpYTVsQVHYxbTcrcYSPD/djCD0oWW1xSeUEud+0OYS/o2OJcAnYxdlUQoaLEhlqyylJuimgIVwBFg9kI3922cUblVA5biHAvb2HiXA12I+YaIJEpyMSaet4m4MewnVgLfNotvNJgJPYDmtCt41jiHAJGL6qP0vqdIyOJXuzePjr1UEhXAo29yN+1nhfrPsqVXJHg6wvntvaCB8ftmw52pJyh73pL95n4ALcEPcJF4JTROsqWxsdSy1kF5GwsCHXEq4Eh9zmt3eS97L8WWEYn8wWRvjwMArGkUiPZoJHuoYRwS5argnXgd1FRZ/BdhutS/BVcTPQ1Lq5akS4ADyakJ6j597MKF/aOfmbKaAhXARGF7Wnzb1O3BbUAud6j9eSvUxIuBScetdG4Qe3/uK2uQU9r7kZhXAF2CNaNaOoJbs2tyI1crUFifQo/BAuAcdlrfvQVlIX7NyxlIYUEK4E28liXbDRWB/iLNLmURzKIgvhKnCyHlR3ltQOOwo/kSyZ7k+4Doz82VZYCdmrO7bLl1lacxc14ePDU+uAV/5iKNK4jyH2C+zDRrgk3K4xkqClgCZuaIxWe7RFEq4ExzC+MXfAVVrotpdc+IkBFoTLwLjZdf18fcs6lqZ9MS6HcDF4TMBBjoQQ5xoqP5Z4Rv3d+BzCR4bTpGBvlfZsedrls6T7ZeAa4UPDMSlYIKmsqfcx+SrJM5UI14LHENh2GnMrzFdh7gkMK1qZCJeEPUnecA0jjTK5wFddMHKacFFYxv1PH2WCzoPU1hayHeFS8PBM0xUvXETPcu04j1bCleA8KRij97yfHhWg3GC9TAEN4RIw/4oUYcKE/1v4D8Tds0yJUwetAAAAAElFTkSuQmCC"
    }

    return NewTxnApiRes(**result)

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
       