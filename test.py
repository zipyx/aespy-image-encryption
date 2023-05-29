from mbedtls import cipher

c = cipher.AES.new(b"My 16-bytes key.", cipher.Mode.CBC, b"CBC needs an IV.")
enc = c.encrypt(b"This is a super-secret message!!")
print(enc)
# b"*`k6\x98\x97=[\xdf\x7f\x88\x96\xf5\t\x19J\xf62h\xf4n\xca\xe8\xfe\xf5\xd7X'\xb1\x8c\xc9\x85"
print(c.decrypt(enc))
# print(enc)
# b'This is a super-secret message!!'
