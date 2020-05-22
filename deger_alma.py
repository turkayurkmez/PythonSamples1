print("Lütfen isminizi giriniz...")
 
girilen_isim = input() #girilen ifadeyi değişkene atıyoruz.
print('Merhaba',girilen_isim)

# Vücut - Kitle endeksi: Kilo / boy **2 
print("Lütfen kilonuzu girin:") 
kilo = int(input())
print("Lütfen boyunuzu metre cinsinden girin ")
boy = float(input())
vki = kilo / boy **2 
print('Vücut Kitle endeksiniz',vki) 
