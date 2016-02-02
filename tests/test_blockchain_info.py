import mock
import unittest

from bitlo.services.blockchain_info import BlockchainInfo
from bitlo.tx import Tx


class BlockchainInfoTest(unittest.TestCase):

    def test_balance_implemented(self):

        class DummyBalance(object):
            def json(self):
                return 123

        with mock.patch('bitlo.services.blockchain_info.requests.get', 
                        return_value=DummyBalance()):
            self.assertEqual(BlockchainInfo.balance('fake address'), 123)

    def test_block_height_implemented(self):

        class DummyBlockHeight(object):
            def json(self):
                return 123

        with mock.patch('bitlo.services.blockchain_info.requests.get', 
                        return_value=DummyBlockHeight()):
            self.assertEqual(BlockchainInfo.block_height(), 123)

    def test_transactions_for_address_implemented(self):

        class EmptyTransactions(object):
            def json(self):
                return {'txs': []}

        with mock.patch('bitlo.services.blockchain_info.requests.get', 
                        return_value=EmptyTransactions()):
            self.assertEqual(
                BlockchainInfo.transactions_for_address('fake address'), 
                [])