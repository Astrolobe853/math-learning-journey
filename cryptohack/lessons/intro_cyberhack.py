### first xor example
# def my_xor_bit(a, b):
#     result = (a and not b) or (not a and b)
#
#     if result:
#         return 1
#     return 0
#
# def my_xor(a, b):
#     result = 0
#     bit_position = 0
#
#     while a > 0 or b > 0:
#         a_bit = a % 2
#         b_bit = b % 2
#
#         xor_bit = my_xor_bit(a_bit, b_bit)
#
#         result = result + xor_bit * (2 ** bit_position)
#
#         a = a // 2
#         b = b // 2
#         bit_position = bit_position + 1
#
#     return result
#
#
# message = "label"
# key = 13
# encrypted = ""
#
# for char in message:
#     encoded = ord(char)
#     result = my_xor(encoded, key)
#     encrypted = encrypted + chr(result)
#
# print(encrypted)

## using xor()
# from pwn import xor
#
# message = "label"
# encrypted = xor(message, 13)
# print(encrypted)

