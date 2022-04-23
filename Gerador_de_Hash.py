import hashlib
print('-'*80)
print('                      | GERADOR DE HASHES EM SHA256 |')
print('-'*80)
while True:
    hash = input('Insira os caracteres que deseja criptografar: ').encode()
    print('Criptofrado:', hashlib.sha256(hash).hexdigest())
    print()
    ds = input('Deseja gerar outra criptografia? (S/N) ').strip().upper()
    if ds == 'N':
        break