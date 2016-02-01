
class ServiceBase(object):

    @classmethod
    def balance(cls, address, confirmations=0):
        """
        Returns the amount of satoshis on the address
        with the specified number of confirmations.
        """
        raise NotImplementedError

    @classmethod
    def transactions_for_address(cls, address, confirmations):
        raise NotImplementedError

    @classmethod
    def send(cls, from, to, private, amount_in_satoshis):
        raise NotImplementedError

    @classmethod
    def unspents(cls, address, confirmations=0):
        raise NotImplementedError
