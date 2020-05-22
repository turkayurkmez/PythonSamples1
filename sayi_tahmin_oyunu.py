# 1. Oyun, 1-100 arasında bir sayı tutar.
# 2. Kullancı sayıyı tahmin eder
# 3. Eğer girilen sayi tutulan sayıdan büyükse ekrana aşağı yazar.
# 4. Eğer girilen sayi tutulandan küçükse ekrana yukarı yazar.
import random
rastgele_sayi = random.randint(1,100)
print(rastgele_sayi)

oyun_bitti_mi = False
while  oyun_bitti_mi == False:
    print('lütfen bir tahmin yapın')
    girilen_sayi = int(input())
    if girilen_sayi < rastgele_sayi:
        print('yukarı')
    elif girilen_sayi > rastgele_sayi:
        print('aşağı')
    else:
        print('tebrikler!')
        oyun_bitti_mi = True
