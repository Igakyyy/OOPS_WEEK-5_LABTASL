class Triangle:
    count = 0  

    def __init__(self, *args):
        # --- Default values changed ---
        if len(args) == 0:
            self._sideA = 2.0
            self._sideB = 3.0
            self._sideC = 4.0
        
        elif len(args) == 1:
            if isinstance(args[0], Triangle):  
                self._sideA = args[0].sideA
                self._sideB = args[0].sideB
                self._sideC = args[0].sideC
            else:  
                value = float(args[0])
                self._sideA = value
                self._sideB = value + 1
                self._sideC = value + 2
       
        elif len(args) == 2:
            self._sideA = float(args[0])
            self._sideB = float(args[1])
            self._sideC = 5.0
        
        elif len(args) == 3:
            self._sideA = float(args[0])
            self._sideB = float(args[1])
            self._sideC = float(args[2])
        else:
            raise ValueError("A 'TRI'angle with 4 sides??")

        Triangle.count += 1  

    # --- Properties ---
    @property
    def sideA(self):
        return self._sideA

    @sideA.setter  
    def sideA(self, value):
        self._sideA = float(value)

    @property  
    def sideB(self):
        return self._sideB

    @sideB.setter  
    def sideB(self, value):
        self._sideB = float(value)

    @property
    def sideC(self):
        return self._sideC

    @sideC.setter  
    def sideC(self, value):
        self._sideC = float(value)

    # --- Class method ---
    @classmethod
    def objectCount(cls):
        return cls.count

    # --- Instance methods ---
    def perimeter(self):
        return self._sideA + self._sideB + self._sideC

    def isRightAngled(self):
        a, b, c = sorted([self._sideA, self._sideB, self._sideC]) 
        return round(a ** 2 + b ** 2, 5) == round(c ** 2, 5)  

    def __str__(self):
        return f"Sides of triangle : A = {self._sideA} , B = {self._sideB} , C = {self._sideC}"
