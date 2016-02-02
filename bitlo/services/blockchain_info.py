import time

import requests

from ..tx import Tx, TxInput, TxOutput
from .base import ServiceBase


class BlockchainInfo(ServiceBase):
    URL = 'https://blockchain.info'

    @classmethod
    def balance(cls, address, confirmations=0):
        url = cls.URL + "/q/addressbalance/{address}"
        url = url.format(address=address)

        request = requests.get(url, data={
            'confirmations': confirmations,
            'nonce': time.time(),
            'api_code': ''
        })
        return request.json()

    @classmethod
    def block_height(cls):
        url = cls.URL + "/q/getblockcount"

        request = requests.get(url, data={
            'nonce': time.time(),
            'api_code': ''
        })
        return request.json()

    @classmethod
    def transactions_for_address(cls, address, confirmations=0):
        # TODO: handle offsets and confirmations
        url = cls.URL + "/es/rawaddr/{address}"
        url = url.format(address=address)

        request = requests.get(url, data={
            'nonce': time.time(),
            'api_code': ''
        })
        raw_txns = request.json()['txs']
        current_block_height = cls.block_height()
        txns = []

        for raw_tx in raw_txns:
            tx = Tx()
            inputs = []
            outputs = []

            for raw_tx_input in raw_tx['inputs']:
                tx_input = TxInput(
                    from_address=raw_tx_input['prev_out']['addr'],
                    amount=raw_tx_input['prev_out']['value']
                )
                inputs.append(tx_input)

            for raw_tx_output in raw_tx['out']:
                tx_output = TxOutput(
                    to_address=raw_tx_output['addr'],
                    amount=raw_tx_output['value']
                )
                outputs.append(tx_output)

            tx.inputs = inputs
            tx.outputs = outputs
            tx.confirmations = current_block_height - raw_tx['block_height']
            tx.tx_hash = raw_tx['hash']
            txns.append(tx)

        return txns
