path = 'c:\\path\\to\\nowhere'
print(path)

s1='\x61' #\x-2digits 
print(s1) # a
s2 = '\u2122' # \u - 4 digits (8482 in hex) 
print(s2) # TM
s3 = '\U00002122' # \U - 8 digits 
print(s3) # TM
s4 = '\N{trade mark sign}' 
print(s4) # TM