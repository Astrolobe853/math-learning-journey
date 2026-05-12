# a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# for i in a: print(chr(i))
#----#
# a = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# print(bytes.fromhex(a))
#----#
# import base64
# a = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# b = bytes.fromhex(a)
# c = base64.b64encode(b)
# print(b)
# print(c)
#----#
# from Crypto.Util.number import long_to_bytes
# a = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# b = long_to_bytes(a)
# print(b)
#----#
from pwn import xor
from Crypto.Util.number import bytes_to_long

def my_xor(a, b):
    if a != b:
        return 1
    else:
       return 0

a = "label"
for i in a: print(ord(i))
# xored = my_xor(b, 13)
# print(xored)
print(xor(a,13))
