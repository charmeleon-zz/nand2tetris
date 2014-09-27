#!/usr/bin/python3

class SymbolTable:
    """Keeps a correspondence between symbolic labels and numeric addresses"""
    
    def __init__(self):
        """Creates a new empty symbol table"""
        pass
        
    def addEntry(self, symbol, address):
        """Adds the pair (symbol, address) to the table"""
        pass
        
    def contains(self, symbol):
        """Does the symbol table contain the given symbol?
        
        returns Boolean"""
        pass

    def GetAddress(self, symbol):
        """Return the address associated with the symbol

        returns int"""
        pass
