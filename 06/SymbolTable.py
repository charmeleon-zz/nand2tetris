#!/usr/bin/python3

class SymbolTable:
    """Keeps a correspondence between symbolic labels and numeric addresses"""
    predefined = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'R0': 0,
                  'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
                  'R8': 8, 'R9': 9,' R10': 10, 'R11': 11, 'R12': 12, 'R13': 13,
                  'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
    
    def __init__(self):
        """Creates a new empty symbol table"""
        self.table = predefined # fill with predefined symbols
        
    def addEntry(self, symbol, address):
        """Adds the pair (symbol, address) to the table"""
        self.table[symbol] = address
        
    def contains(self, symbol):
        """Does the symbol table contain the given symbol?
        
        returns Boolean"""
        return symbol in self.table

    def GetAddress(self, symbol):
        """Return the address associated with the symbol

        returns int"""
        return self.table[symbol]
