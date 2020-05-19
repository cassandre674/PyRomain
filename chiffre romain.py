I,IV,V,IX,X,XL,L,XC,C,CD,D,CM,M=1,4,5,9,10,40,50,90,100,400,500,900,1000
chiffre=int(input("donner un chiffre:"))

while(chiffre-M >=0):
    chiffre-=M
    print('M')
while(chiffre-CM>=0):
    chiffre-=CM
    print('CM')
while(chiffre-D>=0):
    chiffre-=D
    print('D')
while(chiffre-CD>=0):
    chiffre-=CD
    print('CD')
while(chiffre-C>=0):
    chiffre-=C
    print('C')
while(chiffre-XC>=0):
    chiffre-=XC
    print('XC')
while(chiffre-L>=0):
    chiffre-=L
    print('L')
while(chiffre-XL>=0):
    chiffre-=XL
    print('XL')
while(chiffre-X>=0):
    chiffre-=X
    print('X')
while(chiffre-IX >=0):
    chiffre-=IX
    print('IX')
while(chiffre-V>=0):
    chiffre-=V
    print('V')
while(chiffre-IV>=0):
    chiffre-=IV
    print('IV')
while(chiffre-I>=0):
    chiffre-=I
    print('I')


