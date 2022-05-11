import hashlib
import binascii
import datetime

###############Part 1########################
words = [line.strip().lower() for line in open('dictionary.txt')]

passwords = [line.split(":") for line in open('password1.txt')]

f = open("crackedpassword1.txt", "x")

begin_time = datetime.datetime.now()
for word in words:
  h = word.encode('utf-8')
  hasher = hashlib.sha256(h)
  digest = hasher.digest()
  digest_as_hex = binascii.hexlify(digest)
  digest_as_hex_string = digest_as_hex.decode('utf-8')
  for user in passwords:
    if digest_as_hex_string == user[1]:
      print(user[0] + ": " + word)
      f.write(f"{str(user[0])} : {str(word)}\n")
runtime = datetime.datetime.now() - begin_time
f.close()
print(runtime)

#########Part 2################################
words = [line.strip().lower() for line in open('dictionary.txt')]

passwords = [line.split(":") for line in open('password2.txt')]

f = open("crackedpassword2.txt", "x")

#testing
password = 'moose' # type=string
print(f'password ({type(password)}): {password}')

encoded_password = password.encode('utf-8') # type=bytes
print(f'encodedPassword ({type(encoded_password)}): {encoded_password}')

hasher = hashlib.sha256(encoded_password)
digest = hasher.digest() # type=bytes
print(f'digest ({type(digest)}): {digest}')

digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes
print(f'digest_as_hex ({type(digest_as_hex)}): {digest_as_hex}')

digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
print(f'digest_as_hex_string ({type(digest_as_hex_string)}): {digest_as_hex_string}')

for user in passwords:
  if user[0] == "jondich":
    if user[1] == digest_as_hex_string:
      print("test passed")

begin_time = datetime.datetime.now()
for word in words:
  for word_two in words:
    new_word = word + word_two
    h = new_word.encode('utf-8')
    hasher = hashlib.sha256(h)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    for user in passwords:
      if digest_as_hex_string == user[1]:
        print(user[0] + ": " + word)
        f.write(f"{str(user[0])} : {str(word)}\n")
runtime = datetime.datetime.now() - begin_time
f.close()
print(runtime)