
class ServiceBase(object):

    @classmethod
    def balance(cls, address, confirmations=0):
        """
        Returns the amount of satoshis on the address
        with the specified number of confirmations.
        """
        raise NotImplementedError

    @classmethod
    def block_height(cls):
        """
        Returns the height of the block.
        """
        raise NotImplementedError

    @classmethod
    def transactions_for_address(cls, address, confirmations=0):
        """
        Returns all the Tx related to the address
        """
        raise NotImplementedError

    @classmethod
    def send(cls, from, to, private, amount_in_satoshis):
        raise NotImplementedError

    @classmethod
    def unspents(cls, address, confirmations=0):
        raise NotImplementedError
