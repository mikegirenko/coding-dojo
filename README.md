# coding-dojo

**Working through The Coding Dojo Handbook katas**

_Kata: Args_

1. program to parse arguments
    a) accept list of arguments
    b) pass it to parser
    c) ask parser for value of a specific flag
2. parser
    a) accept schema which specifies which arguments accepted
        * flag is one character preceded by minus sign (-)
        * flag value which can be zero or one value
    b) verify list of arguments matches the schema
    c) specify number of flags, types, and accepted values                
    d) return specific flag and it's value to the program
    e) return suitable default value, if flag missing it
    f) verify flag cannot have negative integer
        

_Kata: Bank OCR_

1. machine which reads letters and faxes and produces a file with account numbers
    a) accept letter and fax
    b) produce a file with number of entries
        * each entry is 4 lines long
        * each line has 27 characters
        * the first 3 lines of each entry contain account number
        * each number written using pipes and underscores
        * the fourth line is blank
    c) each account number should have 9 digits, 0-9 only
    d) each account number is a valid checksum:
        * checksum calculation: (d1+2*d2+3*d3+...+9*d9) mod 11 = 0
    e) if some characters are illegible, they are replaced by ?
    f) a file contains around 500 entries


_Kata: Bowling Game_

1. 10 pins
2. each game (line of bowling) consists of 10 turns (frames)
3. each frame have two deliveries of the ball
4. If in two tries, he fails to knock them all down, his score for that frame is the total number 
   of pins knocked down in his two tries.

strike - if you knock down all the pins on your first ball, it is called a strike. If you score a 
strike in the first frame, then an 7 and 1 in the second frame, you would score 18 (10+7+1) for 
the first frame, and 8 for the second frame, making a total of 26 after two frames. 
