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
    * each inventory item has SellIn value which is number of days we have to sell the item
    * each inventory item has Quality value which denotes how valuable the item is
    * at the end of each day system lowers both values for every item
    * once the sell by date has passed, Quality degrades twice as fast
    * the Quality of an item is never negative
    * “Aged Brie” actually increases in Quality the older it gets
    * the Quality of an item is never more than 50
    * “Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
2. add new feature to existing system which will handle new category of items
    * “Conjured” items degrade in Quality twice as fast as normal items


_Kata: Leap Years_

1. All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year),
2. All years divisible by 100 but not by 400 are NOT leap years (so, for example, 1700, 1800, and 1900 were NOT leap 
   years, NOR will 2100 be a leap year),
3. All years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016),
4. All years not divisible by 4 are NOT leap years (e.g. 2017, 2018, 2019).


_Kata: Minesweeper_

1. The goal of the game is to find all the mines within an MxN field


_Kata: Monty Hall_


_Kata: Phone Numbers_

1. Given a list of phone numbers, determine if it is consistent
2. In a consistent phone list no number is a prefix of another


_Kata: Poker Hands_

1. Compare pairs of poker hands to indicate which has higher rank


_Kata: Potter_

1. Calculate the price of any conceivable shopping basket, giving as big a discount as possible.


_Kata: Prime Factors_

1. Factorize a positive integer number into the prime factors.


_Kata: Racing Car Theme_

1. Write unit tests


_Kata: Text Converter_

1. Write unit tests


_Kata: Turn Ticket Dispenser_

1. Write unit tests and refactor TicketDispenser class


_Kata: Telemetry System_

1. Write unit tests


_Kata: Reversi_

1. Write a program  that takes a current board position together with information about whose turn it is, and returns
a list of the legal moves for that player.


_Kata: Roman Numerals_
1. Write a function to convert from normal numbers to Roman Numerals


_Kata: String Calculator_
1. Write a function to receive a string and then calculate it
2. The function adds n number of arguments


_Kata: Tennis_
1. Implement tennis game
2. Each set is one game
3. Each player can have either of these points in one game “love” “15” “30” “40”


_Kata: Anagram_
1. Implement Anagram game
2. This game generates all two-word anagrams of the string “documenting”


_Kata: Birthday Greetings_
1. Send a birthday note to all the friends you have
2. Friends born on February, 29th should have their Birthday greeted on February, 28th
3. Send a Birthday Reminder note when it is someone else birthday
4. Send a single Birthday Reminder note


_Kata: Code Cracker_
1. Create a program that can crack any message using the decryption key


_Kata: Cupcake_
1. Write a program that can build many cakes with many toppings
2. Write a function or method they can show the name of cake
3. Write a function that can show the price of cake


_Kata: Train Reservation_
1. Write a program that can reserve seats on a particular train