import pyqrcode
import math

def generate_qr(text:str):
    qr = pyqrcode.create(text)
    qrData = qr.text(quiet_zone=0).replace('\n', '')
    return qrData , math.sqrt(len(qrData))


def genStr(data):
    str_data = ''
    for i in range(0, len(data), 7):
        temp_data = int(data[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    return str_data


def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal) 