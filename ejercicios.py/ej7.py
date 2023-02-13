elementos = [1, 5, -2]
def agregar_una_vez(e):
  if e in elementos:
    print(f"Error al añadir elementos duplicados => {e}")
  else: 
    elementos.append(e)
    
agregar_una_vez(1)
print(elementos)
print("")