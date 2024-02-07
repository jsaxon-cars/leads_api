"""
Fraud Connection Adapter
"""

import hmac
import hashlib
import base64
from datetime import datetime
from urllib.parse import urlunparse

import requests


class Fraudnet:
    """
    Connects to FraudNet endpoints.
    """
    account_key = None
    shared_secret = None
    base_url = None
    risk_path = None
    http_timeout = None
    org_code = None
    event_source = 'WEB'


    model_codes = {
        'nclead_strict': 'NCLEAD_STRICT',
        'nclead_basic': 'NCLEAD_BASIC',
        'nclead_loose': 'NCLEAD_LOOSE',
    }

    def __init__(self, settings):
        """Sets attributes based on the settings dict passed in."""
        [setattr(self, key, value) for key, value in settings.items()]

    def assess_risk(self, model_name, opts):
        """Given data supplied in opts and a path to a specific service, post a request

        :param model_name:
        :param opts:
        :return: response
        """
        url = urlunparse(('https', self.base_url, self.risk_path, '', '', ''))
        date = datetime.utcnow().isoformat()
        body = self.fraudnet_body(opts, date)
        signature = self.create_signature(
            self.shared_secret,
            f'POST\n{date}\n{self.risk_path}\n{body}'
        )
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f"HmacSHA256 {self.account_key}:{signature}",
            'Date': date
        }
        response = requests.post(url, headers=headers, data=body, timeout=self.http_timeout)

        return response

    def create_signature(self, secret, message):
        """Returns the signature for the request to the FraudNet API."""
        signature = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
        return base64.b64encode(signature.digest()).decode()

    def fraudnet_body(self, opts, date):
        """Returns the body of the request to the FraudNet API."""
        return '''
{
    "orgCode": "{org_code}"
    "modelCode": "{self.model_code['model_name']}",
    "event": {
        "source": "{source}",
        "time": "2021-11-11T18:13:12.923004Z",
        "id": "1f2716b9-8f00-4dab-b40d-1d7af2d53925",
        "device": {
            "ip": "127.0.0.1",
            "jsc": "",
            "hdim": {
                "payload": ""
            }
            
        },
        "externalRiskResults": [
            {                                  		
                "source": "neustar",
                "score": "pass",
                "code": "pass"
            }
        ],		
        "contacts": [
            {
                "@id": "CONTACT1",
                "address": {
                    "city": "Chicago",
                    "countryCode": "US",
                    "postal": "60608",
                    "stateProvinceCode": "IL",
                    "streetLine": "111 Nullberry Py",
                    "streetLine2": ""
                },
                "emails": [
                    {
                        "email": "jsaxon@cars.com"
                    }
                ],
                "name": "James Saxon Cars.com Developer",
                "phoneNumbers": []
            },
        ],
        "userAccount": {
            "accountHolder": "CONTACT1",
        }
        "order": {
            "lineItems": [
                {
                    "@id": "LINEITEM1",
                    "category": "Honda",
                    "description": "2016-Honda-Accord",
                    "name": "Accord",
                }
            ],
        },
        "custom": {
            "carscomCustom": [
                {
                    "description": "",
                    "frontDoorAffiliate": "",
                    "listingId": ""
                }
            ]
        },
    },
}
        '''
