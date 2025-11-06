# ---- Main Code (Values changed) ----
print("------------------------------------------------------------")
a = Triangle() 
print(a)
print(f"Perimeter : {a.perimeter()}")
print(f"Right Angle Triangle? : {a.isRightAngled()}")
print("------------------------------------------------------------")

b = Triangle(4)
print(b)
print(f"Perimeter : {b.perimeter()}")
print(f"Right Angle Triangle? : {b.isRightAngled()}")
print("------------------------------------------------------------")

c = Triangle(5, 12)
print(c)
print(f"Perimeter : {c.perimeter()}")
print(f"Right Angle Triangle? : {c.isRightAngled()}")
print("------------------------------------------------------------")

d = Triangle(5, 12, 13)
print(d)
print(f"Perimeter : {d.perimeter()}")
print(f"Right Angle Triangle? : {d.isRightAngled()}")
print("------------------------------------------------------------")

e = Triangle(d)
print(e)
print(f"Perimeter : {e.perimeter()}")
print(f"Right Angle Triangle? : {e.isRightAngled()}")
print("------------------------------------------------------------")
print(f"No of Triangles: {Triangle.objectCount()}")
🧮 New Output Example
mathematica
Copy code
------------------------------------------------------------
Sides of triangle : A = 2.0 , B = 3.0 , C = 4.0
Perimeter : 9.0
Right Angle Triangle? : False
------------------------------------------------------------
Sides of triangle : A = 4.0 , B = 5.0 , C = 6.0
Perimeter : 15.0
Right Angle Triangle? : False
------------------------------------------------------------
Sides of triangle : A = 5.0 , B = 12.0 , C = 5.0
Perimeter : 22.0
Right Angle Triangle? : False
------------------------------------------------------------
Sides of triangle : A = 5.0 , B = 12.0 , C = 13.0
Perimeter : 30.0
Right Angle Triangle? : True
------------------------------------------------------------
Sides of triangle : A = 5.0 , B = 12.0 , C = 13.0
Perimeter : 30.0
Right Angle Triangle? : True
------------------------------------------------------------
No of Triangles: 5
