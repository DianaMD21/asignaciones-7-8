from contextlib import nullcontext
import requests,json

x= requests.get("http://localhost:7000/api/estudiante/")
print("Item A:")
#y = json.loads(x)
#z = json.dumps(x)
#for x in y:
print(x.text)
print("\n")

print("Item B:")
matricula = input("Introduzca la matricula del estudiante que desea consultar: ")
#print(matricula)
request_matricula=requests.get("http://localhost:7000/api/estudiante/"+matricula)

if request_matricula.text == "Internal server error":
    print("El estudiante con la matricula "+matricula+ " no existe")
else:
    print(request_matricula.text)

print("\n")

print("ITEM C: ")
matricula_new = input("Introduzca la matricula del estudiante que desea agregar: ")
name = input("Introduzca el nombre del estudiante que desea agregar: ")
career = input("Introduzca la carrera del estudiante que desea agregar: ")
data = {
    "matricula": matricula_new,
    "nombre": name,
    "carrera": career,
}
request_itemc=requests.post("http://localhost:7000/api/estudiante/", json=data)
x= requests.get("http://localhost:7000/api/estudiante/")
print(x.text)
print("\n")

print("Item C:")
matricula = input("Introduzca la matricula del estudiante que desea eliminar: ")
#print(matricula)
request_matricula=requests.delete("http://localhost:7000/api/estudiante/"+matricula)

if request_matricula.text == "Internal server error":
    print("El estudiante con la matricula "+matricula+ " no existe")
else:
    print(request_matricula.text+" <-- El estudiante fue eliminado con exito")

