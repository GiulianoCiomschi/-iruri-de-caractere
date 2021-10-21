S=str(input("Introduceti sirul de caractere: "))
#a
nr_A=S.count(chr(65))
nr_a=S.count(chr(97))
print("Numarul de aparitii ale carcterului 'A' in sirul S este de ", nr_A,"ori.")
print("Numarul de aparitii ale carcterului 'a' in sirul S este de ", nr_a,"ori.")
#b
print("Sirul obtinut prin inlocuirea carcaterului 'A' prin'*' este: ", S.replace('A','*'))
#c
print("Sirul obtinut prin radierea tuturor aparitiilor 'B' este: ",S.replace('B',''))
#d
print("Numarul de aparitii ale silabei MA in S este:", S.count('MA'))
#e
print("Sirul obtinut prin isubstituirea carcaterului MA prin TA este: ", S.replace('MA','TA'))
#f
print("Sirul obtinut prin radierea tuturor aparitiilor 'TO' este: ", S.replace('TO',''))
#g
print("Scrierea inversa a siruluui S este:",S[::-1])