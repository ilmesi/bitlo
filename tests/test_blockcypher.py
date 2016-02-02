import mock
import unittest

from bitlo.services.blockcypher import Blockcypher
from bitlo.tx import Tx


class BlockcypherTest(unittest.TestCase):

    def test_balance_implemented(self):

        class DummyBalance(object):
            def json(self):
                return {'balance': 123}

        with mock.patch('bitlo.services.blockcypher.requests.get', 
                        return_value=DummyBalance()):
            self.assertEqual(Blockcypher.balance('fake address'), 123)

    def test_block_height_implemented(self):

        class DummyBlockHeight(object):
            def json(self):
                return {'height': 123}

        with mock.patch('bitlo.services.blockcypher.requests.get', 
                        return_value=DummyBlockHeight()):
            self.assertEqual(Blockcypher.block_height(), 123)

    def test_transactions_for_address_implemented(self):

        class EmptyTransactions(object):
            def json(self):
                return {'txs': []}

        with mock.patch('bitlo.services.blockcypher.requests.get', 
                        return_value=EmptyTransactions()):
            self.assertEqual(
                Blockcypher.transactions_for_address('fake address'), 
                [])