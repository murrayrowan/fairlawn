#!/usr/bin/env python
import sys

def getString():
       input = raw_input("Enter string to encode / decode: ")
       print "You entered: ", input
       return input

def encode( string_to_encode ):
      atbash = {"a" : "z", "b" : "y", "c" : "x", "d" : "w", "e" : "v", "f" : "u", "g" : "t", "h" : "s", "i" : "r", "j" : "q", "k" : "p", "l" : "o", "m" : "n", "n" : "m", "o" : "l",  "p" : "k", "q" : "j", "r" : "i", "s" : "h", "t": "g",  "u" : "f", "v" : "e", "w" : "d", "x" : "c", "y" : "b", "z" : "a" } 
      arr = list( string_to_encode ) 
      code = ""
      for el in arr:
            code = code + atbash[el]       
      return code 

if __name__ == '__main__':

       string_to_encode = getString()
       code = encode( string_to_encode )
       print "The Encoded String is ", code

