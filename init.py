class trabajador:
    empleado=[] # este es el arreglo que guarda el diccionario y los datos de los empleados 
    c_impuesto=[] # este arreglo guarda el comentario del calculo de impuesto
    c_afp=[] # este arreglo guarda el comentario del calculo de afp
    c_salud=[] # este arreglo guarda el comentario del calculo de salud
    v_impuesto=[] # este arreglo guarda los valor de el calculo de impuesto 
    v_afp=[] # este arreglo guarda los valor de el calculo de salud 
    v_salud=[] # este arreglo guarda los valor de el calculo de afp 
    
    
    
    impuesto=0
    salud=0
    afp=0
    comentario= ""
    comentario2= ""
    comentario3= ""

    def __init__(self):
        for i in range(3):
            nombre=str(input("Ingrese nombre: "))
            sueldo=int(input("Ingrese sueldo: "))
            diccionario={"nombre":nombre,"sueldo":sueldo}
            self.empleado.append(diccionario)
        
  #  def imprimir(self):
         #  print(self.empleado)

#**************************************************** MENU ****************************************************
    def menu(self):
        print("\nMENÚ:")
        print("1. Mostrar los sueldos líquidos de los 3 empleados")
        print("2. Impuesto que paga cada empleado")
        print("3. Descuento de AFP de cada empleado")
        print("4. Descuento salud de cada empleado")
        print("5. Añadir campos de impuesto, AFP y salud al diccionario")
        
        opcion = input("Ingrese la opción deseada (1-5): ")
        if opcion == "1":
            persona1.calculo_sueldoliquido()
        elif opcion == "2":
            persona1.mostrar_calculo_impuesto()
        elif opcion == "3":
            persona1.mostrar_caculo_afp()
        elif opcion == "4":
            persona1.mostrar_calculo_salud()
        elif opcion == "5":
            persona1.ingreso_datos()


#**************************************************** calculo de impuesto ****************************************************
    def calculo_impuesto(self):
        
        for i in range(3):         
            if(self.empleado[i]["sueldo"]<10000):
                self.impuesto=0
                comentario =  " ".join(("El empleado ",self.empleado[i]["nombre"],"no paga impuesto"))
                self.c_impuesto.append(comentario)
                
            if(self.empleado[i]["sueldo"]>=10000 and self.empleado[i]["sueldo"]<=30000):
                self.impuesto=self.empleado[i]["sueldo"]*0.10
                comentario = " ".join(("El descuento para el empleado ", self.empleado[i]['nombre'], "es de un 10%", "con un total de descuento de", str(self.impuesto)))
                self.c_impuesto.append(comentario) 
                
            elif(self.empleado[i]["sueldo"]>30000 and self.empleado[i]["sueldo"]<=50000):
                self.impuesto=self.empleado[i]["sueldo"]*0.20
                comentario = " ".join(("El descuento para el empleado ", self.empleado[i]['nombre'], "es de un 20%", "con un total de descuento de", str(self.impuesto)))
                self.c_impuesto.append(comentario)
                
            elif(self.empleado[i]["sueldo"]>50000):
                self.impuesto=self.empleado[i]["sueldo"]*0.35
                comentario = " ".join(("El descuento para el empleado ", self.empleado[i]['nombre'], "es de un 35%", "con un total de descuento de", str(self.impuesto)))
                self.c_impuesto.append(comentario)
            self.v_impuesto.append(self.impuesto) # aqui guardamos los valores de impuesto de cada uno de los empleados, para sumarlos mas adelante
        #self.menu()
        
    
#**************************************************** Calculo AFP ****************************************************
    def calculo_afp(self):
        for i in range(3):
            self.afp = self.empleado[i]["sueldo"]*0.11
            #print(f"El total a pagar por AFP del empleado ",self.empleado[i]["nombre"],f"es de {self.afp}")
            comentario1 = " ".join(("El total a pagar por AFP del empleado", self.empleado[i]['nombre'], "es de", str(self.afp)))
            self.c_afp.append(comentario1)
            self.v_afp.append(self.afp) #guardamos el valor de afp   
       # self.menu()
#**************************************************** Calculo Salud ****************************************************    
    def calculo_salud(self):
        for i in range(3):
            self.salud = self.empleado[i]["sueldo"]*0.07
            #print(f"El total a pagar por Salud del empleado ",self.empleado[i]["nombre"],f"es de {self.salud}")
            comentario2 = " ".join(("El total a pagar por salud del empleado", self.empleado[i]['nombre'], "es de", str(self.salud)))
            self.c_salud.append(comentario2)
            self.v_salud.append(self.salud) #guardamos el valor de salud
       # self.menu()
#**************************************************** Calculo sueldo liquido ****************************************************        
    def calculo_sueldoliquido(self):
        self.calculo_impuesto()  # Calcula el impuesto
        self.calculo_afp()  # Calcula el descuento AFP
        self.calculo_salud()  # Calcula el descuento salud
        for i in range(3):
            sueldo_bruto = self.empleado[i]["sueldo"]
            sueldo_liquido = sueldo_bruto - (self.v_impuesto[i] + self.v_afp[i] + self.v_salud[i])
            print(f"El sueldo líquido para el empleado",self.empleado[i]['nombre'], f"es de: {sueldo_liquido}")
            #self.menu()
#**************************************************** Agregar datos a diccionario **********************************************

    def ingreso_datos(self):
        self.calculo_impuesto()  # Calcula el impuesto
        self.calculo_afp()  # Calcula el descuento AFP
        self.calculo_salud()  # Calcula el descuento salud
        
        for i in range(3):  
            diccionario = self.empleado[i]  # Obtener el diccionario existente en cada iteración
            impuesto = self.v_impuesto[i]  
            afp = self.v_afp[i]
            salud = self.v_salud[i]
            diccionario.update({"impuesto": impuesto, "afp": afp, "salud": salud})#agregamos los nuevos valores al diccionario
       #print(self.empleado)#print para comprobar el valor nuevo del diciconario
            




        
#**************************************************** Mostar calculos  ****************************************************

    def mostrar_calculo_impuesto(self):
        self.calculo_impuesto()
        print("********** TOTAL DE IMPUESTOS POR EMPLEADOS **********")
        print
        for i in range(3):
            print(self.c_impuesto[i]) 
       #print(self.v_impuesto) #print solo para mostrar que hay dentro
        print("******************************************************")
        
        
    def mostrar_caculo_afp(self):
        self.calculo_afp()
        print("********** DESCUENTO DE AFP POR EMPLEADOS **********")
        for i in range(3):
            print(self.c_afp[i]) 
        #print(self.v_afp) #print solo para mostrar que hay dentro
        print("******************************************************")
        
        
    def mostrar_calculo_salud(self):
        self.calculo_salud()
        print("********** DESCUENTO DE SALUD POR EMPLEADOS **********")
        for i in range(3):
            print(self.c_salud[i]) 
        #print(self.v_salud) #print solo para mostrar que hay dentro
        print("******************************************************")


#Menu

print("********* INGRESO DE DATOS EMPLEADOS *********")
persona1=trabajador()
#persona1.imprimir()
persona1.menu()





