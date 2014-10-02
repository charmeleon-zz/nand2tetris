#!/usr/bin/python3

class Parser:
    """Handles the parsing of a single .vim file, and encapsulates access to the
    input code. It reads VM commands, parses them, and provides convenient
    access to their components. In addition, it removes all whitespace and
    comments"""

    def __init(self, file):
        """Opens the input file/stream and gets ready to parse it"""
        pass

    def hasMoreCommands(self):
        """Are there more commands in the input?"""
        pass

    def advance(self):
        """Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands is true."""
        pass

    def commandType(self):
        """Returns the type of the current VM command. C_ARITHMETIC is returned
        for all the arithmetic commands."""
        pass

    def arg1(self, string):
        """Returns the first arg of the current command. In the case of
        C_ARITHMETIC, the command itself (add, sub, etc.) is returned. Should 
        not be called if the current command is C_RETURN"""
        pass

    def arg2(self, integer):
        """Returns the second arg of the current command. Should be called only
        if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL"""
        pass
