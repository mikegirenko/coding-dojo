# coding-dojo

**Working through The Coding Dojo Handbook katas**

_Kata: Args_
Actors:

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