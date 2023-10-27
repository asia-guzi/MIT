# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:43:57 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Using encoder and encrypt as models, implement the functions
decoder and decrypt. Use them to decrypt the message
22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23
*11*1*57*6*173*7*11
which was encrypted using the opening of Don Quixote.



'''



# stworzenie szyfru i zakodowanie wiadomoci'


# gen_code_keys = (lambda book, plain_text:(
#     {c: str(book.find(c)) for c in plain_text}))

# encoder = (lambda code_keys, plain_text:
#            ''.join(['*' + code_keys[c] for c in plain_text])[1:])

# encrypt = (lambda book, plain_text:
#            encoder(gen_code_keys(book, plain_text), plain_text))





book='Machnęła lewą ręką i udało jej się przywrócić skopek z mlekiem, które spłynęło po literach. A jej prawa ręka puściła nagle drzwi otworzyły się z trzaskiem i w progu stanęły obie panny. PLASK! Kiedy zebrała się razem w ten sposób, ramię w ramię to miała do powiedzenia coś ważnego..'

cipher_text='22*37*19*10*4*8*22*25*174*14*38*8*0*1*16*31*19*21*190'    
#encrypt(book,plain_text)  ##input('wpisz szyfr do odkodowania')
print(cipher_text)




'złamanie kodu, odkodowanie wiadomoci'
gen_decode_keys = (lambda book, cipher_text:
                   {s: book[int(s)] for s in cipher_text.split('*')})
    

decoder = (lambda decode_value, cipher_text: 
           
           ''.join([decode_value[c] for c in cipher_text.split('*')]))

decrypt = (lambda book, cipher_text: decoder(gen_decode_keys(book, cipher_text), cipher_text))



wiadomosc= decrypt(book, cipher_text)

print(wiadomosc)