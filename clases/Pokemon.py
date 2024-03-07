class Pokemon:
    _nombre = None #2 __ es mas seguro, sino cagaste
    _HP = None
    _Ataque = None
    _Defensa = None
    _Nivel = None
    _tipo = None

    def __init__(self, HP, Ataque, Defensa, tipo , nombre):
        self._nombre = nombre
        self._HP = HP
        self._Ataque = Ataque
        self._Defensa = Defensa
        self._tipo = tipo
        
        
    @property
    def nombre(self):
        self._nombre
        
    @nombre.getter
    def nombre(self):
        return self._nombre
    
    @property
    def HP(self):
        self._HP
        
    @HP.getter
    def HP(self):
        return self._HP
    
    @property
    def Ataque(self):
        return self._Ataque
    
    @Ataque.getter
    def Ataque(self):
        return self._Ataque 
    
    @property
    def Defensa(self):
        return self._Defensa
    
    @Ataque.getter
    def Defensa(self):
        return self._Defensa

    @property
    def tipo(self):
        return self._tipo
    
    @Ataque.getter
    def tipo(self):
        return self._tipo
   
    def recibirDanio(self, cantidad):
        self._HP -= cantidad
        if self._HP < 0:
            self._HP = 0
        print(self.HP)
    
    def curarse(self, cantidad):
        self._HP += cantidad
        print("me cure puto")
        if self._HP < 0:
            self._HP = 0   
        
    def atacar(self,pokemon:Pokemon):
        if(self.Ataque>pokemon._Defensa):
            pokemon.recibirDanio(self.Ataque - pokemon)  #no usar _hp
        else:
            pokemon._HP -= pokemon._Defensa - self.Ataque #error cuando ataque es mayor a defensa
        