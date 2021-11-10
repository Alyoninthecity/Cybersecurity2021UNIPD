import base64

original_data = "El Psy Congroo"
encrypted_data = base64.b64decode("IFhiPhZNYi0KWiUcCls=")
encrypted_flag = base64.b64decode("I3gDKVh1Lh4EVyMDBFo=")
key = []
flag = ""

for i in range(len(encrypted_data)):
    key.append(encrypted_data[i] ^ ord(original_data[i]))

for i in range(len(encrypted_flag)):

    flag += chr(encrypted_flag[i] ^ key[i])

print(flag)
