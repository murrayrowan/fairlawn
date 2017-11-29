#!/usr/bin/env python

def getString():
       input = raw_input("Enter string to encode / decode: ")
       print "You entered: ", input
       return input

def atbash():
      atbash = {"a" : "z", "b" : "y", "c" : "x", "d" : "w", "e" : "v", "f" : "u", "g" : "t", "h" : "s", "i" : "r", "j" : "q", "k" : "p", "l" : "o", "m" : "n", "n" : "m", "o" : "l",  "p" : "k", "q" : "j", "r" : "i", "s" : "h", "t": "g",  "u" : "f", "v" : "e", "w" : "d", "x" : "c", "y" : "b", "z" : "a" }
      return atbash

# encode / decode the string using for .. in
def encode( string_to_encode ):
      atb = atbash()
      arr = list( string_to_encode ) 
      code = ""
      for el in arr:
            code = code + atb[el]       
      return code 

# no need for encode and decode for atbash. wrote this to show how to use map here
def decode( string_to_encode ):
      atb = atbash()
      def cnv(x): return atb[x]
      arr = list(map(cnv, string_to_encode )) 
      return "".join(arr)

if __name__ == '__main__':
       string_to_encode = getString()
       code = decode( string_to_encode )
       print "The Encoded String is ", code

