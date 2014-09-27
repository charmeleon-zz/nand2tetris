#!/usr/bin/python3

import sys, os
from Parser import *
from Code import *

class Assembler:
    """Handles file I/O"""

    def __init__(self, files):
        self.files = files

    def hasFiles(self):
        """Are there more files to process?"""
        return len(self.files) > 0

    def processFile(self):
        """Process the next file in the queue and translates it"""
        filename = self.files.pop(0)
        p = Parser(filename)
        path, basename = os.path.split(filename)
        fileout = os.path.join(path, os.path.splitext(basename)[0] + ".hack")
        f = open(fileout, 'w')
        print("Translating %s" % (basename))
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
            print(instruction, end='\n', file=f)
        f.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Assembler.py FILE")
        sys.exit(1) 
    a = Assembler(sys.argv[1:])
    while a.hasFiles():
        a.processFile()

