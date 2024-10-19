import base64
st="this is encode and decode test"
encodedst=base64.b64encode(st.encode('utf-8'))
print('Encoded string: ',encodedst)
decodedst=base64.b64decode(encodedst.decode('utf-8'))
print('Decoded string: ',decodedst)