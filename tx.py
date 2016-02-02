class Tx(object):
    tx_hash = ''
    inputs = []
    outputs = []


class TxInput(object):
    from_address = ''
    amount = 0


class TxOutput(object):
    to_address = ''
    amount = 0