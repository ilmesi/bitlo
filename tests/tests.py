import unittest

from .base import ServiceBase


class BaseInterfaceTest(unittest.TestCase):

    def test_balance_not_implemented(self):
        base = ServiceBase
        self.assertRaises(NotImplementedError, base.balance, *[None]*2)

    def test_block_height_not_implemented(self):
        base = ServiceBase
        self.assertRaises(NotImplementedError, base.block_height)

    def test_transactions_for_address_not_implemented(self):
        base = ServiceBase
        self.assertRaises(NotImplementedError, base.transactions_for_address, *[None]*2)

    def test_send_not_implemented(self):
        base = ServiceBase
        self.assertRaises(NotImplementedError, base.send, *[None]*4)

    def test_unspents_not_implemented(self):
        base = ServiceBase
        self.assertRaises(NotImplementedError, base.unspents, *[None]*2)


if __name__ == '__main__':
    unittest.main()