import hashlib

ar1 = 'h.txt'
ar2 = 'a.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(ar1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(ar2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {ar1}, é diferente do arquivo: {ar2}')
    print(f'Hash do arquivo h.tx: {hash1.hexdigest()}')
    print(f'Hash do arquivo a.tx: {hash2.hexdigest()}')

else:
    print(f'O arquivo: {ar1}, é igual ao arquivo: {ar2}')
    print(f'Hash do arquivo h.tx: {hash1.hexdigest()}')
    print(f'Hash do arquivo a.tx: {hash2.hexdigest()}')
