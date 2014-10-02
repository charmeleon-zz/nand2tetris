#!/usr/bin/python3

class CodeWriter:
    """Translates VM commands into Hack assembly code"""

    def __init__(self, outfile):
        """Opens the output file/stream and gets ready to write into it"""
        pass

    def setFileName(self, filename):
        """Informs the code writer that the translation of a new VM file is started"""
        pass

    def writeArithmetic(self, command):
        """Writes the assembly code that is the translation of the given arithmetic command"""
        pass

    def WritePushPop(self, command, segment, index):
        """Writes the assembly code that is the translation of the given command, where command
        is either C_PUSH or C_POP"""
        pass

    def Close(self):
        """Closes the output flie"""
        pass
