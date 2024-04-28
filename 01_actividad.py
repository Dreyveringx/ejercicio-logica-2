#actividad profesor david

valor_unitario = int(input("Ingrese valor unitario: "))
cantidad = int(input("Ingrese Cantidad: "))
subtotal = int(valor_unitario * cantidad)

print("subtotal: ", subtotal)

iva = (subtotal * 0.19)

print("Valor IVA generado: ", iva)

total = (subtotal * iva)

print("Total transacción: ", total)
