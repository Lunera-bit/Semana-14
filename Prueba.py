# Código sucio - Guardar como citas_sucio.py

def proc(l, p, e, s):
    # 1. Validar especialidad (Estructura de control compleja)
    if e != "Cardiologia" and e != "Pediatria" and e != "Dermatologia":
        print(f"Error: Especialidad {e} no disponible.\n")
        return

    # 2. Calcular costo según especialidad y seguro
    precio_base = 0
    if e == "Cardiologia":
        precio_base = 150.0
    elif e == "Pediatria":
        precio_base = 90.0
    elif e == "Dermatologia":
        precio_base = 110.0

    costo_final = precio_base
    if s == "S":
        costo_final = precio_base * 0.20 # 80% de descuento por seguro

    # 3. Guardar en la lista usando un diccionario genérico
    cita_id = "CITA-" + str(len(l) + 1)
    l.append({"id": cita_id, "p": p, "e": e, "s": s})

    # 4. Imprimir reporte de la cita
    print("=== COMPROBANTE DE CITA ===")
    print("ID: " + cita_id)
    print("Paciente: " + p)
    print("Especialidad: " + e)
    print(f"Costo Base: S/. {precio_base:.2f}")
    print(f"Total a Pagar: S/. {costo_final:.2f}")
    print("---------------------------\n")

# Datos de prueba para que los alumnos lo ejecuten
lista_citas = []
proc(lista_citas, "Juan Perez", "Cardiologia", "S")
proc(lista_citas, "Maria Lopez", "Pediatria", "N")
proc(lista_citas, "Luis Gomez", "Oftalmologia", "N") # Error
