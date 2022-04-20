peso_total = float (input ("Informe o peso total: "))
tara_prato = 0.135

peso_comida = float (peso_total - tara_prato)

total = peso_comida * 45

print ("O total a pagar é: ", total)