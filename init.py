class trabajador:
    empleado=[]
    impuesto=0
    salud=0
    afp=0

    def __init__(self):
        for i in range(3):
            nombre=str(input("Ingrese nombre: "))
            sueldo=int(input("Ingrese sueldo: "))
            diccionario={"nombre":nombre,"sueldo":sueldo}
            self.empleado.append(diccionario)
        
    def imprimir(self):
            print(self.empleado)


    def menu(self):
        print("\nMENÚ:")
        print("1. Mostrar los sueldos líquidos de los 3 empleados")
        print("2. Impuesto que paga cada empleado")
        print("3. Descuento de AFP de cada empleado")
        print("4. Descuento salud de cada empleado")
        print("5. Añadir campos de impuesto, AFP y salud al diccionario")
        print("6. Salir")    
        opcion = input("Ingrese la opción deseada (1-6): ")
        if opcion == "1":
            persona1.calculo_sueldoliquido()
        elif opcion == "2":
            persona1.calculo_impuesto()
        elif opcion == "3":
            persona1.calculo_afp()
        elif opcion == "4":
            persona1.calculo_salud()
        elif opcion == "5":
            print("Esta es la opcion 5") 



    def calculo_impuesto(self):
        
        for i in range(3):
            
            if(self.empleado[i]["sueldo"]<10000):
                self.impuesto=self.empleado[i]["sueldo"]*0.10
                print(f"El empleado: ",self.empleado[i]["nombre"],"no paga impuesto")
                
            if(self.empleado[i]["sueldo"]>=10000 and self.empleado[i]["sueldo"]<=30000):
                self.impuesto=self.empleado[i]["sueldo"]*0.10
                print(f"El decuento para el empleado: ",self.empleado[i]["nombre"],"es de un 10%")
                print(f"el total del descuento es de: {self.impuesto}")
                
            elif(self.empleado[i]["sueldo"]>30000 and self.empleado[i]["sueldo"]<=50000):
                self.impuesto=self.empleado[i]["sueldo"]*0.20
                print(f"El decuento para el empleado: ",self.empleado[i]["nombre"],"es de un 20%")
                print(f"el total del descuento es de: {self.impuesto}")    
                
            elif(self.empleado[i]["sueldo"]>50000):
                self.impuesto=self.empleado[i]["sueldo"]*0.35
                print(f"El decuento para el empleado: ",self.empleado[i]["nombre"],"es de un 35%")
                print(f"el total del descuento es de: {self.impuesto}")
        self.menu()
    
    def calculo_afp(self):
        for i in range(3):
            self.afp = self.empleado[i]["sueldo"]*0.11
            print(f"El total a pagar por AFP del empleado ",self.empleado[i]["nombre"],f"es de {self.afp}")
        self.menu()
    
    def calculo_salud(self):
        for i in range(3):
            self.salud = self.empleado[i]["sueldo"]*0.07
            print(f"El total a pagar por Salud del empleado ",self.empleado[i]["nombre"],f"es de {self.salud}")
        self.menu()
        
    def calculo_sueldoliquido(self):
        self.calculo_impuesto()  # Calcula el impuesto
        self.calculo_afp()  # Calcula el descuento AFP
        self.calculo_salud()  # Calcula el descuento salud
        for i in range(3):
            sueldo_bruto = self.empleado[i]["sueldo"]
            sueldo_liquido = sueldo_bruto - self.impuesto - self.salud - self.afp
            print(f"El sueldo líquido para el empleado",self.empleado[i]['nombre'], f"es de: {sueldo_liquido}")
            self.menu()
        


#Menu

print("********* INGRESO DE DATOS EMPLEADOS *********")
persona1=trabajador()
persona1.imprimir()
persona1.menu()





