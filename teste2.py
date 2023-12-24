import matplotlib.pyplot as plt



def mostrar():


# Dados iniciais
    updates = [("Jan", 1000)]

# Adicionando mais dados para meses posteriores
    
   
    updates.append(("Feb", 1500))
    updates.append(("Mar", 2000))
    updates.append(("Apr", 1800))

# Separando meses e valores para plotagem no gráfico
    months = [update[0] for update in updates]
    values = [update[1] for update in updates]

# Plotando o gráfico
    plt.figure(figsize=(8, 5))  # Definindo o tamanho da figura
    plt.plot(months, values, marker='o', linestyle='-', color='b')

# Definindo rótulos e título do gráfico
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.title('Value Over Months')

# Mostrando o gráfico
    plt.tight_layout()
    plt.show()