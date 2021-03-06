import time

import requests

from ..tx import Tx, TxInput, TxOutput
from .base import ServiceBase


class Blockcypher(ServiceBase):
    URL = 'https://api.blockcypher.com/v1/btc/main'

    @classmethod
    def balance(cls, address, confirmations=0):
        # TODO: use confirmations (?)
        url = cls.URL + "/addrs/{address}/balance"
        url = url.format(address=address)

        request = requests.get(url, data={
            'token': ''
        })
        return request.json()['balance']

    @classmethod
    def block_height(cls):
        url = cls.URL

        request = requests.get(url, data={
            'token': ''
        })
        return request.json()['height']

    @classmethod
    def transactions_for_address(cls, address, confirmations=0):
        url = cls.URL + "/addrs/{address}/full"
        url = url.format(address=address)

        request = requests.get(url, data={
            'confirmations': confirmations,
            'token': ''
        })
        raw_txns = request.json()['txs']
        txns = []

        for raw_tx in raw_txns:
            tx = Tx()
            inputs = []
            outputs = []

            for raw_tx_input in raw_tx['inputs']:
                tx_input = TxInput(
                    from_address=raw_tx_input['addresses'][0],
                    amount=raw_tx_input['output_value']
                )
                inputs.append(tx_input)

            for raw_tx_output in raw_tx['outputs']:
                tx_output = TxOutput(
                    to_address=raw_tx_output['addresses'][0],  # weird list
                    amount=raw_tx_output['value']
                )
                outputs.append(tx_output)

            tx.inputs = inputs
            tx.outputs = outputs
            tx.confirmations = raw_tx['confirmations']
            tx.tx_hash = raw_tx['hash']
            txns.append(tx)

        return txns
