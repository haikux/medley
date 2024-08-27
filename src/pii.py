from src.const import PRESIDIO_ANOM_URL, PRESIDIO_ANALYZER_URL
import requests as req
import json

class PII:
    def __init__(self):
        self.anom_url = PRESIDIO_ANOM_URL
        self.analyzer_url = PRESIDIO_ANALYZER_URL
    
    def analyze(self, text: str, lang: str="en") -> dict:
        headers = {"Content-type": "application/json"}
        data = json.dumps({"text": text, "language": lang})
        resp = {}
        try:
            resp = req.post(self.analyzer_url, headers=headers, data=data).json()
        except Exception as e:
            print(str(e))
        return resp

    def anonymize(self, text: str, analyzer_res: list, replace_text: str="ANONYMIZED", lang: str="en"):
        headers = {"Content-type": "application/json"}
        data = json.dumps({"text": text, "analyzer_results": analyzer_res, 
                           "anonymizers": {"DEFAULT": {"type": "replace", "new_value": replace_text}}})
        resp = {}
        try:
            resp = req.post(self.anom_url, headers=headers, data=data).json()
        except Exception as e:
            print(str(e))
        return resp

        