class Paciente:
    nombre_completo = "José Antonio Torres Alves"
    run = "22.123.124-2"
    sexo = "masculino"
    operaciones = "Apendicectomía"
    enfermedades = "Asma"
    alergias = "Alergia al polen"
    diagnostico  = "Hepatitis B"

print("Ficha Clínica\n")

paciente1 = Paciente()
print("Nombre del paciente: ",paciente1.nombre_completo)
print("run: ",paciente1.run)
print("sexo: ",paciente1.sexo)
print("Operaciones previas: ",paciente1.operaciones)
print("Enfermedades crónicas: ",paciente1.enfermedades)
print("Alergias: ",paciente1.alergias)
print("Último diagnóstico: ",paciente1.diagnostico)
