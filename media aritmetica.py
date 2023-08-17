nome=input("digite seu nome: ")
bm1=int(input("digite a nota da primeiro bimestre: "))
bm2=int(input("digite a nota do segundo bimestre: "))
bm3=int(input("digite a nota do terceiro bimestre: "))
bm4=int(input("digite a nota do quarto bimeste: "))
media=float(bm1+bm2+bm3+bm4/4)
print ("media final do aluno: ",(bm1+bm2+bm3+bm4/4))
if media >= 9:
    print("aprovado")
elif media >= 7:
    print("aprovado com louvor")
elif media < 7:
    print("reprovado")