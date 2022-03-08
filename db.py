import json
from deta import Deta
from dotenv import load_dotenv
import os
from models import TeaRequests
load_dotenv()


deta = Deta(os.getenv("DETA_PROJECT_KEY"))
requestsDB = deta.Base("REQUESTS")


def store_new_request_to_db(new_request: TeaRequests):
    data = new_request.json()
    return requestsDB.put(json.loads(data))