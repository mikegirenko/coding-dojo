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
4. If in two tries player fails to knock all pins down, score for that frame is the total number 
   of pins knocked down in two tries
5. If in two tries player knocks all pins down, this is called a “spare” and score for the 
   frame is ten plus the number of pins knocked down on next throw (in his next turn)
6. If on his first try in the frame player knocks down all the pins, this is called a “strike”. The 
   turn is over, and score for the frame is ten plus the simple total of the pins knocked 
   down in his next two rolls.
7. If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus 
   balls, respectively.


_Kata: Gilded Rose_

1. system which updates inventory
    * each inventory item has SellIn value (number of days left to sell this item)
    * each inventory item has Quality value which denotes how valuable the item is
    * at the end of each day system lowers both values for every item
    * once the sell by date has passed, Quality degrades twice as fast
2. add new feature to existing system which will handle new category of items
