import hashlib

texto = input("Digite o texto para converter: ")
options = int(input('''## HASH GENERATOR by Obelix ##
     1) MD5
     2) SHA1
     3) SHA256
     4) SHA512
     Escolha uma opção acima: '''))

if(options ==1):
    resultado = hashlib.md5(texto.encode('utf-8'))
    print("hash MD5 gerada: ", resultado.hexdigest())
if(options ==2):
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print("Hash SHA1 gerada: ", resultado.hexdigest())
if(options ==3):
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print("Hash SHA256 gerada: ", resultado.hexdigest())
if(options ==4):
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print("Hash SHA512 gerada: ", resultado.hexdigest())
else:
    print("Algo saiu errado!!")
