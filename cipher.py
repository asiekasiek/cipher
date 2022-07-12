#!/usr/bin/env python3

wybor = int(input("Wybierz: 1 - szyfrowanie; 2 - deszyfrowanie"))

if wybor == 1:

	#Szyfrowanie wiadomości z przesunięciem
	przesuniecie = int(input("Wprowadź wartość przesunięcia: "))	#Wprowadzenie wartości przesunięcia jako zmiennej typu int
	import os							#Import modułu os, żeby móc korzystać z poleceń terminala
	os.system("stty -echo")						#ukrycie wpisywanego tekstu poleceniem z terminala
	wiadomosc = input("Wprowadź wiadomość: ")			#wprowadzanie wiadomości do zaszyfrowania
	os.system("stty echo")						#wprowadzane znaki znowu są widoczne
	print()								#nowy wiersz
	print("Wiadomość zaszyfrowana: ")
	i = 0
	for litery in wiadomosc :					#pętla for dzięki której kolejne znaki w wiadomości są szyfrowane o przesunięcie
	#       print(litery)
		P = ord(wiadomosc[i])					#zamiana string na int, aby znaki przyjęły wartość ASCII
		R = chr(P+przesuniecie)					#zaszyfrowanie znaku o przesunięcie w ASCII i zamina int na string (liczba na znak)
	#       print(P, R)
		print(R, end="")					#wyświetlenie zaszyfrowanego znaku, bez tworzenia nowej linii
		i=i+1
	print()								#nowa linia na końcu zaszyfrowanej wiadomości

elif wybor == 2:

	#Deszyfrowanie wiadomości z przesunięciem
	przesuniecie = int(input("Wprowadź wartość przesunięcia: "))    #Wprowadzenie wartości przesunięcia jako zmiennej typu int
	import os                                                       #Import modułu os, żeby móc korzystać z poleceń terminala
	os.system("stty -echo")                                         #ukrycie wpisywanego tekstu poleceniem z terminala
	wiadomosc = input("Wprowadź zaszyfrowaną wiadomość: ")          #wprowadzanie wiadomości do zaszyfrowania
	os.system("stty echo")                                          #wprowadzane znaki znowu są widoczne
	print()                                                         #nowy wiersz
	print("Wiadomość zdeszyfrowana: ")
	i = 0
	for litery in wiadomosc :                                       #pętla for dzięki której kolejne znaki w wiadomości są szyfrowane o przesunięcie
		#       print(litery)
        	P = ord(wiadomosc[i])                                   #zamiana string na int, aby znaki przyjęły wartość ASCII
        	R = chr(P-przesuniecie)                                 #zaszyfrowanie znaku o przesunięcie w ASCII i zamina int na string (liczba na znak)
	#       print(P, R)
        	print(R, end="")                                        #wyświetlenie zaszyfrowanego znaku, bez tworzenia nowej linii
        	i=i+1
	print()                                                         #nowa linia na końcu zaszyfrowanej wiadomości

else:

	print("Błąd")
