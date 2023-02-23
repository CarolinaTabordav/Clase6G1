class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo1= ""
        self.__peso=0
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
    def verlista_medicamentos(self):
        return self.__lista_medicamentos

    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n         

class sistemaV:
    def __init__(self):
    
        self.__felinos={}
        self.__caninos={}
        self.__lista_mascotas = []   

    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)
    
    def verNumerofelinos(self):
        return len(self.__felinos)

    def verNumerocaninos(self):
        return len(self.__caninos)

    def ingresarMascota(self,mascota):
        if self.verificarExiste(mascota.verHistoria()):
            return False
        else:
            self.__lista_mascotas.append(mascota) 
            self.__lista_mascotas[mascota.verHistoria()] = mascota

            return True

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None

    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                # del self.__lista_mascotas[historia]
                # self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False

class Medicamento:
    def __init__(self):
        self.__nombre=""
        self.__dosis=0
        self.__tipo=""
    
    def verNombre(self):
        return self.__nombre

    def verDosis(self):
        return self.__dosis
    
    def verTipo(self):
        return self.__tipo
    
    def asignarTipo(self,med):
        self.__tipo==med

    def asignarNombre(self,med):
        self.__nombre==med
    def asignarDosis(self,med):
        self.__dosis=med 
