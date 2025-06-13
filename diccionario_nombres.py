estudiantes = { "Ana": 20, "Luis": 21, "Marta": 19 }

for nombre,edad in estudiantes.items():
  print(f"{nombre} tiene {edad} años")
print("***********")
#Si no existe la llave se agrega, sino se modifica ya que no pueden existir dos llaves iguales
estudiantes["Pedro"]=18
estudiantes["Marta"]=21

print(f"La nueva edad de Marta es {estudiantes['Marta']}")
print("***********")
for nombre,edad in estudiantes.items():
  print(f"{nombre} tiene {edad} años")
del estudiantes["Marta"]

print("***********")
for nombre,edad in estudiantes.items():
  print(f"{nombre} tiene {edad} años")