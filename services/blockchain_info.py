import time

import requests

from .base import ServiceBase


class BlockchainInfo(ServiceBase):
    URL = 'https://blockchain.info'

    @classmethod
    def balance(address, confirmations=0):
        url = self.URL + "/q/addressbalance/{address}"
        url = url.format(address=address)

        request = requests.get(url, data={
            'confirmations': confirmations,
            'nonce': time.time(),
            'api_code': ''
        })
        return request.json()


    @classmethod
    def transactions_for_address(address, confirmations):
        # TODO: handle offsets

        url = self.URL + "/q/rawaddr/{address}"
        url = url.format(address=address)

        request = requests.get(url, data={
            'confirmations': confirmations,
            'nonce': time.time(),
            'api_code': ''
        })
        response = request.json()