cipher = 'C:\Documents and Settings\zq5586\Desktop\Personal\Coding\Python\cipher1.txt'

with open(cipher, 'r') as raw_cipher:
    cipher_nums = raw_cipher.read().split(',')

for i, num in enumerate(cipher_nums):
    cipher_nums[i] = int(num)

"""
for first_letter in xrange(97, 123):
    for second_letter in xrange(97, 123):
        for third_letter in xrange(97, 123):
            key = [first_letter, second_letter, third_letter]
            decipher_nums = [0]*len(cipher_nums)
            key_num = 0
            for i, cipher_num in enumerate(cipher_nums):
                decipher_nums[i] = cipher_num^key[key_num]
                if key_num == 2:
                    key_num = 0
                else:
                    key_num += 1
            message = ''.join([chr(num) for num in decipher_nums])
            try:
                check = message.index('the')
            except:
                pass
"""

solution = [103, 111, 100]
decipher_nums = [0]*len(cipher_nums)
key_num = 0
for i, cipher_num in enumerate(cipher_nums):
    decipher_nums[i] = cipher_num^solution[key_num]
    if key_num == 2:
        key_num = 0
    else:
        key_num += 1
print ''.join([chr(num) for num in decipher_nums])
print sum(decipher_nums)
                

