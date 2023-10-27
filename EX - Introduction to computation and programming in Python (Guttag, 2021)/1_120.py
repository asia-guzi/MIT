# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:43:17 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Remedy the problem described in the previous paragraph. Hint:
a simple way to do this is to create a new book by appending something to the
original book.





KOD Z KSIĄŻKI:
    
'stworzenie szyfru i zakodowanie wiadomoci'


gen_code_keys = (lambda book, plain_text:(
    {c: str(book.find(c)) for c in plain_text}))

encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))





book='In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'
plain_text='no is no' #input('wpisz tekst do zakodowania')
code_keys=gen_code_keys(book, plain_text)
print(code_keys)


pass

'złamanie kodu, odkodowanie wiadomoci'
gen_decode_keys = (lambda book, cipher_text:{s: book[int(s)] for s in cipher_text.split('*')})
gen_decode_keys(book, '1*13*2*6*57*2*1*13')
'''

'stworzenie szyfru i zakodowanie wiadomoci'


gen_code_keys = (lambda book, plain_text:(
    {c: str(book.find(c)) for c in plain_text}))

encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))

# test = (lambda book, plain_text : ( if all (x in book for x in plain_text)))




# new_book = (lambda book: book +  ' .' ) 


# efekt = (lambda book, plain_text: book = new_book(book, plain_text) if test(book,plain_text))

book='Machnęła lewą ręką i udało jej się przywrócić skopek z mlekiem, które spłynęło po literach. A jej prawa ręka puściła nagle drzwi otworzyły się z trzaskiem i w progu stanęły obie panny. PLASK! Kiedy zebrała się razem w ten sposób, ramię w ramię to miała do powiedzenia coś ważnego.'
# book = efekt(book,plain_text)
plain_text='dzien dobry Maksiu!' #input('wpisz tekst do zakodowania')
code_keys=gen_code_keys(book, plain_text)
#print(code_keys)
cipher_text=encrypt(book,plain_text)
print(cipher_text)


# print(book)
pass

# 'złamanie kodu, odkodowanie wiadomoci'
# gen_decode_keys = (lambda book, cipher_text:{s: book[int(s)] for s in cipher_text.split('*')})
# gen_decode_keys(book, '1*13*2*6*57*2*1*13')