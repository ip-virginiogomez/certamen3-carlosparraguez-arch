ventas = [
    [12000, 15000, 8000],
    [10000, 17000, 9000],
    [20000, 10000, 12000],
]

mejor_vendedor = None
mayor_total = 0

for i in range(len(ventas)):
    total_vendedor = 0
    for j in range(len(ventas[i])):
        total_vendedor += ventas[i][j]

    print(f"Vendedor {i + 1}: total ventas = ${total_vendedor:,}")

    if total_vendedor > mayor_total:
        mayor_total = total_vendedor
        mejor_vendedor = i + 1

    if total_vendedor < 30000:
        print(f"El vendedor {i + 1} tuvo bajo desempeño")

if mejor_vendedor is not None:
    print(f"El vendedor con mejor desempeño fue {mejor_vendedor} con ${mayor_total:,} en ventas")
