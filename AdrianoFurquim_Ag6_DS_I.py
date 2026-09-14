valor = float(input("Valor da compra (R$): ")) #Entrada (usuário) do valor da compra

if valor >= 300: #Caso a compra seja maior ou igual a 300 reais
    desconto = valor * 0.15 #Aplica o desconto de 15%

elif valor >= 200: #Caso a compra seja maior ou igual a 200 reais e menor que 300 reais
    desconto = valor * 0.1 #Aplica o desconto de 10%

else: #Caso a compra seja menor que 200 reais
    desconto = valor * 0.05 #Aplica o desconto de 5%

valor_final = valor - desconto #Calcula o valor final
print(f"Valor total da compra R${valor:.2f}")
print(f"Valor do desconto R${desconto:.2f}")
print(f"Valor final da compra R${valor_final:.2f}")