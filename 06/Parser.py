#!/usr/bin/python3

import sys, re

A_COMMAND = 'A'
C_COMMAND = 'C'
L_COMMAND = 'L'

class Parser:
    """Encapsulates access to the input code. Reads an assembly language
    command, parses it, and provides convenieint access to the command's
    components (fields/symbols). Removes all whitespace and comments"""

    def __init__(self, filepath):
        """Opens the input/file stream and gets ready to parse it"""
        try:
            with open(filepath, 'r') as f:
                self.commands= list(filter(len,
                         [re.sub('//.*$', '', l.strip()) for l in f]))
        except FileNotFoundError:
            print("Could not find %s" % (filepath))

    def hasMoreCommands(self):
        """Are there more commands in the input?"""
        return len(self.commands) > 0

    def advance(self):
        """Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands() is true.
        Initially there is no current command"""
        self.command = self.commands.pop(0)

    def commandType(self):
        """Returns the type of the current command:
        * A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        * C_COMMAND for dest=comp;jump
        * L_COMMAND (pseudo-command) for (Xxx) where Xxx is a symbol"""
        if self.command[0] == '@':
            return A_COMMAND
        elif self.command[0] == '(' and self.command[-1] == ')':
            return L_COMMAND
        return C_COMMAND


    def symbol(self):
        """Returns the symbol or decimal Xxx of the current command @Xxx or
        (Xxx). Should be called only when commandType() is A_COMMAND or
        L_COMMAND

        Returns string"""
        return self.command.strip('@()')

    def dest(self):
        """Returns the dest mnemonic in the current C-command (8 possibilities)
        Should be called only when commandType() is C_COMMAND

        Returns string"""
        if '=' not in self.command:
            return ''
        return self.command.split('=')[0]

    def comp(self):
        """Returns the comp mnemonic in the current C-command (28 possibilities)
        Should be called when comandType() is C_COMMAND

        Returns string"""
        
        return self.command.split('=')[-1].split(';')[0]

    def jump(self):
        """Returns the jump mnemonic in the current C-command (8 possibilities)
        Should be called only when commandType() is C_COMMAND

        Returns string"""
        if ';' not in self.command:
            return ''
        return self.command.split('=')[-1].split(';')[-1]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Parser.py FILE")
    else:
        print("Running parser")
    for arg in sys.argv[1:]:
        p = Parser(arg)
        while p.hasMoreCommands():
            p.advance()
            print("Symbol: %s, instruction: %s, dest: %s, comp: %s, jump: %s"
                  % (p.symbol(), p.commandType(), p.dest(), p.comp(), p.jump()))
