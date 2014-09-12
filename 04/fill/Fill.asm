// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// @KBD: Single-word memory map at RAM[24576]. EQ 0 if nothing is pressed
// @SCREEN: Pixel map starting at 16384, where @KBD begins

// Read keyboard input
(LOOP)
    @24576
    D=A
    @current
    M=D
    @KBD
    D=M
    @FILL
    D;JGT // If a key is pressed, fill the screen
    @CLEAR
    D;JEQ // If nothing is pressed, clear the screen
    @LOOP
    0;JMP
(END)
@LOOP
0;JMP

(FILL) // Blackens the screen if a key is pressed
   @KBD
   D=M
   @LOOP
   D;JEQ // If a key is no longer pressed, go back to main loop
   @current
   D=M-1
   @16384
   D=D-A
   @LOOP
   D;JEQ
   @current
   M=M-1 // go to the next pixel
   A=M // point to current pixel 
   M=1 // Darken pixel
   @FILL
   0;JMP
(FILLEND)

(CLEAR) // Clears the screen if no key is pressed
   @KBD
   D=M
   @LOOP
   D;JGT // Stop clearing and go to main loop if a key is pressed
   @current
   D=M-1  
   @16384
   D=D-A
   @LOOP
   D;JEQ
   @current
   M=M-1 
   A=M 
   M=0 // Clear pixel
   @CLEAR
   0;JMP
(CLEAREND)
