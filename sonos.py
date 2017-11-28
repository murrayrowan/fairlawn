#!/usr/bin/env python
import sys
from soco import SoCo

def printSkull():

 art = '''\
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
 '''
 return art

def askForCode():
       guess = raw_input("Enter Secret Code: ")
       print "you entered ", guess
       sound = checkCode( guess )
       if sound == False:
                print "This is not a valid attack code. Please try again!"
                return askForCode() 
       else:
	        return sound

def checkCode( code ):
        if code == "code1":
                mp3 = 'https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/guns.mp3'

        elif code == "code2":
                mp3 = 'https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/bombs.mp3'

        elif code == "code3":
                mp3 = 'https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/explosion.mp3'
        else:
                mp3 = False;
        return mp3

def attackEnemy( weapon ):
 
        sonos = SoCo('192.168.0.43') # Pass in the IP of your Sonos speaker
        sonos.play_uri( weapon )
        track = sonos.get_current_track_info()
        print track['title'] 
        sonos.pause()
        sonos.play()

if __name__ == '__main__':

 print printSkull()

 mp3 = askForCode()

 attackEnemy( mp3 )


