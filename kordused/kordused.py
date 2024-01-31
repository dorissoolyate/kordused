#1
while True:
    n=input("skolko zajcev (ot 1 do 9): ")
    if n.isdigit() and 1 <= int(n) <= 9:
        n = int(n)
        break
    else:
        print("tolko ot 1 do 9")
for i in range(n):
    print("  (\\_/)")
    print("  (o o)")
    print(" / | \\*")
    if i<n-1:
        print()
        
#2
while True:
    try:
        L = int(input("vvedi chislo L: "))
        if L>=0:
            break 
        else:
            print("bez -")
    except ValueError:
        print("celoe chislo")
sum_rezultat=sum(range(L+1))
print(f"summa ot 0 do 9 {L} {sum_rezultat}")

#3
import  random
zag_chislo=random.randint(0, 100)
max_popqtok=10
for popqtki in range(1, max_popqtok + 1):
    ugadano=int(input(f"popqtka {popqtki} davaj ugadqvaj"))
    if ugadano==zag_chislo:
        print("ura, ugadali")
        break
    elif ugadano>zag_chislo:
        print("menshe")
    else:
        print("bolshe")
if ugadano !=zag_chislo:
    print(f"haha ne ugadali za {max_popqtok} i eto chislo {zag_chislo}")

#4
num=int(input("vvedi chislo"))
revers_num=0
while num>0:
    cifra=num%10
    revers_num=revers_num*10+cifra
    num=num//10
print(f"v reverse {revers_num}")

#5
num=int(input("vvedi celoe 4islo"))
sum_cifer=0
proizv_cifer=1
while num>0:
    cifra=num%10
    sum_cifer+=cifra
    proizv_cifer*=cifra
    num=num//10
print(f"summa {sum_cifer}")
print(f"proizvedenie {proizv_cifer}")