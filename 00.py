def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])
 
msg = """
Alice
Bill the Lizard
Pat
The Caterpillar
The Cheshire Cat
The Dodo
The Dormouse
The Duchess
The Duck
The Eaglet
The Gryphon
The Hatter
The King of Hearts
The Knave of Hearts
The Lory
The March Hare
The Mock Turtle
The Mouse
The Puppy
The Queen of Hearts
The White Rabbit"""
print (msg)
enc = caesar(msg, 11)
print (enc)
print (caesar(enc, 11, decode = True))