#Pyta o punktację z egzaminu
score = input ("Enter Score: ")
#Wczytuje punktację z egzaminu w postaci liczby zmiennoprzecinkowej
s = float(score)
#Stwaia warunek kiedy można stwierdzić, że wartość jest błędna
if 0.0 > s > 1.0:
    print("Error")
    quit()
#Jeśli wartość mieści się w zakresie to wystawia poszczególne oceny za daną punktację
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
