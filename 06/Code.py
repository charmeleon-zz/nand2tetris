#!/usr/bin/python3

import sys
from Parser import *

class Code:
    """Translates Hack assembly language mnemonics into binary codes"""
    destmap = {'': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
               'AM': '101', 'AD': '110', 'AMD': '111'}
    jumpmap = {'': '000', 'JGT': '001', 'JEQ': '010', 'JLT': '100',
               'JNE': '101', 'JLE': '110', 'JMP': '111'}
    a0comp = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100',
              'A': '110000', '!D': '001101', '-D': '001111', '-A': '110011',
              'D+1': '011111', 'A+1': '110111', 'D-1': '001110',
              'A-1': '110010', 'D+A': '000010', 'D-A': '010011',
              'A-D': '000111', 'D&A': '000000', 'D|A': '010101'}
    a1comp = {'M': '110000', '!M': '110001', '-M': '110011', 'M+1': '110111',
              'M-1': '110010', 'D+M': '000010', 'D-M': '010011',
              'M-D': '000111', 'D&M': '000000', 'D|M': '010101'}

    @staticmethod
    def dest(mnemonic):
        """Returns the binary code of the dest mnemonic

        Returns 3 bits"""
        return Code.destmap[mnemonic]

    @staticmethod
    def comp(mnemonic):
        """Returns the binary code of the comp mnemonic
        
        Returns 7 bits"""
        if mnemonic in Code.a1comp:
            return '1' + Code.a1comp[mnemonic]
        elif mnemonic in Code.a0comp:
            return '0' + Code.a0comp[mnemonic]

    @staticmethod
    def jump(mnemonic):
        """Returns the binary code of the jump mnemonic

        Returns 3 bits"""
        return Code.jumpmap[mnemonic]
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Code.py FILE")
        sys.exit(1) 
    for arg in sys.argv[1:]:
        p = Parser(arg)
        while p.hasMoreCommands():
            p.advance()
            if (p.commandType() == A_COMMAND):
                # Not clear where A-instructions should be parsed yet, 
                # so I'll do it here for now (also, no labels for now)
                instruction = '{0:016b}'.format(int(p.symbol()))
            elif (p.commandType() == C_COMMAND):
                parts = []
                parts.append('111')
                parts.append(Code.comp(p.comp()))
                parts.append(Code.dest(p.dest()))
                parts.append(Code.jump(p.jump()))
                instruction = ''.join(parts)
            else:
                instruction = p.symbol()
            print(instruction)

