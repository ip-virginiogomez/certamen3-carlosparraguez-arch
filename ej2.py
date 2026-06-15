edad = int(input("ingrese su edad: "))
socio = input("es socio? (s/n): ")
total = float(input("total compra: "))


if edad > 60 and socio.lower() == "s" and total > 1000:
    total_a_pagar = total - total * 0.15
    print(f"califica para descuento total a pagar: {total_a_pagar}")
else:
    print(f"no califica para descuento. total a pagar: {total}")
