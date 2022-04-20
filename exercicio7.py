camiseta_p = int (30)
camiseta_m = int (35)
camiseta_g = int (40)

valor_p = int (input ("Informe a quantidade de camisetas P: "))
valor_m = int (input ("Informe a quantidade de camisetas M: "))
valor_g = int (input ("Informe a quantidade de camisetas G: "))

total_p = valor_p * camiseta_p
total_m = valor_m * camiseta_m
total_g = valor_g * camiseta_g

total = total_p + total_m + total_g

print ("O total do pedido é: ", total)