class Tx(object):
    tx_hash = ''
    amount = 0
    inputs = []
    outputs = []


class TxInput(object):
    from_address = ''
    amount = 0


class TxOutput(object):
    to_address = ''
    amount = 0