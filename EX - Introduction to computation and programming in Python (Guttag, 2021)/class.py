# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:03:36 2023

@author: Joanna.Guziwelakis


"""

'''

ogólnie może być jeszcze zalecana foerma i kształt cięcia, zakecana długć, zalecane odżywki, jakie zalecenia peh, polecane odzywki przez inne analogiczne skrety i stylizatory, zakladka nowoci


+ apka na podstawie produktów które się sprawdzały mogłaby wyrzucać konkretne składniki, któree Ci służa lub nie służą i podpowiadać inne odżywki analogicznie 


'''

class wlosy ():
    def __init__ (self, dlugosc, kolor, typ): #typ - proste fale loki
        self.dlugosc = dlugosc
        self.kolor = kolor
        self.typ = typ
        self.produkty = {}
    
    def dodaj_produkt (self, produkt, rodzaj): #do odżywek potem trzeba dodać peh/ eh/ p itp.
         #"L'Biotica - INDIA", "Odżywka")
        self.produkty[produkt] = rodzaj
        
    


class loczki ():
    def __init__ (self, poziom): #np skret poziom 2 typu c , albo np tylko poziom - 2c
        
        self.poziom = poziom
        
        
asia = wlosy ('srednie', 'brazowe', 'falowane') 

print(asia.typ)   
