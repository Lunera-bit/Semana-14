from dataclasses import dataclass


ESPECIALIDADES_VALIDAS = {
    "Cardiologia": 150.0,
    "Pediatria": 90.0,
    "Dermatologia": 110.0,
}
DESCUENTO_SEGURO = 0.20


@dataclass
class Cita:
    id: str
    paciente: str
    especialidad: str
    tiene_seguro: str


def validar_especialidad(especialidad):
    if especialidad not in ESPECIALIDADES_VALIDAS:
        print(f"Error: Especialidad {especialidad} no disponible.\n")
        return False
    return True


def obtener_precio_base(especialidad):
    return ESPECIALIDADES_VALIDAS[especialidad]


def calcular_costo_final(precio_base, tiene_seguro):
    if tiene_seguro == "S":
        return precio_base * DESCUENTO_SEGURO
    return precio_base


def generar_id_cita(lista_citas):
    return "CITA-" + str(len(lista_citas) + 1)


def guardar_cita(lista_citas, cita_id, paciente, especialidad, tiene_seguro):
    lista_citas.append(Cita(cita_id, paciente, especialidad, tiene_seguro))


def imprimir_comprobante(cita_id, paciente, especialidad, precio_base, costo_final):
    print("=== COMPROBANTE DE CITA ===")
    print("ID: " + cita_id)
    print("Paciente: " + paciente)
    print("Especialidad: " + especialidad)
    print(f"Costo Base: S/. {precio_base:.2f}")
    print(f"Total a Pagar: S/. {costo_final:.2f}")
    print("---------------------------\n")


def registrar_cita(lista_citas, paciente, especialidad, tiene_seguro):
    if not validar_especialidad(especialidad):
        return

    precio_base = obtener_precio_base(especialidad)
    costo_final = calcular_costo_final(precio_base, tiene_seguro)
    cita_id = generar_id_cita(lista_citas)

    guardar_cita(lista_citas, cita_id, paciente, especialidad, tiene_seguro)
    imprimir_comprobante(cita_id, paciente, especialidad, precio_base, costo_final)


def main():
    lista_citas = []
    registrar_cita(lista_citas, "Juan Perez", "Cardiologia", "S")
    registrar_cita(lista_citas, "Maria Lopez", "Pediatria", "N")
    registrar_cita(lista_citas, "Luis Gomez", "Oftalmologia", "N")


if __name__ == "__main__":
    main()
