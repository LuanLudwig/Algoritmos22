paes = int (input ("Informe a quantidade de pães vendido: "))
broas = int (input ("Informe a quantidade de broas vendidas: "))

valor_paes = float (paes * 0.50)
valor_broas = float (broas * 1.50)

total = float (valor_paes + valor_broas)
guardar = float (total /10)
print ("Total de vendas nesse dia é R$: " , total)
print ("Deve guardar na poupança R$: ", guardar)