class Tx(object):
    tx_hash = ''
    confirmations = 0
    inputs = []
    outputs = []

    def __str__(self):
        return "Tx - {hash}".format(hash=tx_hash)


class TxInput(object):
    from_address = ''
    amount = 0

    def __init__(self, from_address, amount):
        self.from_address = from_address
        self.amount = amount


class TxOutput(object):
    to_address = ''
    amount = 0

    def __init__(self, to_address, amount):
        self.to_address = to_address
        self.amount = amount