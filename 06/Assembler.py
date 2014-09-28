#!/usr/bin/python3

import sys, os
from Parser import *
from Code import *
from SymbolTable import *

class Assembler:
    """Handles file I/O"""

    def __init__(self, files):
        self.files = files
        self.symtable = SymbolTable()

    def hasFiles(self):
        """Are there more files to process?"""
        return len(self.files) > 0

    def dummyPass(self):
        """Do a soft pass to determine the location for labels (Xxx)"""
        filename = self.files[0]
        p = Parser(filename)
        current_address = 0
        while p.hasMoreCommands():
            p.advance()
            cmd_type = p.commandType()
            if cmd_type is A_COMMAND or cmd_type is C_COMMAND:
                current_address += 1
            elif cmd_type is L_COMMAND:
                self.symtable.addEntry(p.symbol(), current_address)

    def processFile(self):
        """Translates the next file in the queue"""
        filename = self.files.pop(0)
        p = Parser(filename)
        if filename.endswith('.asm'):
            fileout = filename.replace('.asm', '.hack')
        else:
            fileout = filename + '.hack'
        f = open(fileout, 'w')
        print("Translating %s" % (filename))
        self.current_address = 16
        while p.hasMoreCommands():
            p.advance()
            if p.commandType() is A_COMMAND:
                address = self._getAddress(p.symbol())
                instruction = '{0:016b}'.format(int(address))
            elif p.commandType() is C_COMMAND: # dest=comp;jump
                instruction = ''.join(['111', Code.comp(p.comp()),
                               Code.dest(p.dest()), Code.jump(p.jump())])
            else: # L_COMMAND (Xxx)
                continue
            #print("Symbol: %s. Instruction: %s" % (p.symbol(), instruction))
            print(instruction, end='\n', file=f)
        f.close()

    def _getAddress(self,  symbol):
        if symbol.isdigit():
            return symbol
        else:
            if not self.symtable.contains(symbol):
                self.symtable.addEntry(symbol, self.current_address)
                self.current_address += 1
            return self.symtable.GetAddress(symbol)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Assembler.py FILE")
        sys.exit(1) 
    a = Assembler(sys.argv[1:])
    while a.hasFiles():
        a.dummyPass()
        a.processFile()

