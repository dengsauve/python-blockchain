import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates new block, adds to chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Adds new transaction to transaction list

        :param sender:<str> Address of Sender
        :param recipient:<str> Address of Recipient
        :param amount:<int>Amount
        :return:<int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Return the last Block in the chain
        pass