print('Saat kaç? (dakika hariç)')
saat = int(input())
print('Bugün haftasonu mu (E/H) ?')
cevap = input().upper()

if saat < 12 and cevap == 'H':
    print('günaydın')
elif saat >= 18 and cevap =='H':
    print('iyi akşamlar')  
elif cevap == 'E':
    print('Bugün kapalıyız :)')   
else:
    print('iyi günler')
    

