from suds.client import Client
url = "http://localhost:7000/ws/EstudianteWebServices?wsdl"
client = Client(url)
#print (client)
print("ITEM A: ")
listaEstudiantes=client.service.getListaEstudiante()
for x in listaEstudiantes:
    print(x)
print("")

print("ITEM B: ")
matricula = input("Introduzca la matricula del estudiante que desea consultar: ")
estudiante=client.service.getEstudiante(int(matricula))
if estudiante is None:
    print("El estudiante con la matricula "+matricula+ " no existe")
else:
    print(estudiante)
print("")

print("ITEM C: ")
matricula_new = input("Introduzca la matricula del estudiante que desea agregar: ")
name = input("Introduzca el nombre del estudiante que desea agregar: ")
career = input("Introduzca la carrera del estudiante que desea agregar: ")
data = {
    "matricula": matricula_new,
    "nombre": name,
    "carrera": career,
}
newEstudiante=client.service.crearEstudiante(data)
print("El estudiante fue agregado con exito. Lista de estudiantes actualizada:")
listaEstudiantes=client.service.getListaEstudiante()
for x in listaEstudiantes:
    print(x)
print("")

print("ITEM D: ")
matricula = input("Introduzca la matricula del estudiante que desea eliminar: ")
deleted=client.service.eliminarEstudiante(matricula)
print(deleted)
print(" <-- El estudiante fue eliminado con exito. Lista de estudiantes actualizada: ")
listaEstudiantes=client.service.getListaEstudiante()
for x in listaEstudiantes:
    print(x)
print("")
