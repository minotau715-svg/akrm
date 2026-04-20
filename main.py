import base64
with open('result.txt','r',encoding='utf-8') as encoded_file:
    encoded_content=encoded_file.read().strip()
decoded_content=base64.b64decode(encoded_content).decode('utf-8')
exec(compile(decoded_content,'result.txt','exec'))
