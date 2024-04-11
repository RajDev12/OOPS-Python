#Each key is separated from its value by a colon (:), the items are separated by commas,
# and the whole thing is enclosed in curly braces.

ph={'aman':123,'anu':345,'iop':678}
print(ph)

#More than one entry per key not allowed. Which means no duplicate key is allowed.
#When duplicate keys encountered during assignment, the last assignment wins. 
#Keys are immutable but values can be modified

ph={'aman':123,'anu':345,'iop':678, 'aman':555}
# print(ph)

ph['avi']=123345  # adding new value
# print(ph)

ph['anu']=22334 #updating existing value
# print(ph)
ph.values()
ph.keys()
# len(ph)