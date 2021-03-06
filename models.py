from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Status(BaseModel):
    water_level: int
    tea_powder: int
    coffee_power: int

class DrinkType(Enum):
    TEA = "tea"
    COFFEE = "coffee"

class NewteaModel(BaseModel):
    count: int
    machine_number: str
    amount:int
    config: Optional[Status]
    type: DrinkType 


class TeaRequests(BaseModel):
    key: str
    time: datetime
    machine_number: str
    amount: int
    status: str
    type : DrinkType
    quantity : int
    orderId : str
    config: Optional[Status]
    

class Paytm_api_call(BaseModel):
    mid          : str
    orderId      : str
    amount       : int
    businessType : str
    posId        : str

class Result_info(BaseModel):
    resultStatus : str
    resultCode : str
    resultMsg : str

class NewTxnApiRes(BaseModel):
    qrCodeId : str
    qrData : str
    image : str
    resultInfo: Result_info

class TxnStsApiRes(BaseModel):
    resultInfo : Result_info
    txnId : str
    bankTxnId : Optional[str]
    orderId : str
    txnAmount : Optional[str]
    txnType : str
    gatewayName : Optional[str]
    bankName : Optional[str]
    mid : str
    paymentMode : Optional[str]
    refundAmt : Optional[str]
    txnDate : str
    authRefId : Optional[str]


class QR_Res_Model(BaseModel):
    qr: str
    request_id: str