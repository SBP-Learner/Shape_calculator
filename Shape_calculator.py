import math
def square () :
    side = float(input("Enter the side of square : "))
    area = side*side
    perimeter = 4*side
    
def rectangle () :
    length = float(input("Enter the length of the rectangle : "))
    width = float(input("Enter the width of the rectangle : "))
    area = length*width
    perimeter = 2*(length+width)

def triangle () :
    base = float(input("Enter the base of the triangle : "))
    height = float(input("Enter the height of the triangle : "))
    area = 0.5*base*height

    side1 = float(input("Enter the first side of the triangle : "))
    side2 = float(input("Enter the second of the triangle : "))
    side3 = float(input("Enter the third of the triangle : "))
    perimeter = side1+side2+side3

def right_triangle () :
    base = float(input("Enter the base of the triangle : "))
    height = float(input("Enter the height of the triangle : "))
    area = 0.5*base*height
    perimeter = base + height + math.sqrt(base**2+height**2)


def equilateral_triangle () :
    side = float(input("Enter the side of equilateral triangle : "))
    eqarea = 3**0.5/4*side
    eqperimeter = side*3

def circle () :
    radius = float(input("Enter the radius of circle : "))
    area = math.pi*radius*radius
    circumference = 2*math.pi*radius
    
def parallelogram () :
    base = float(input("Enter the base of the parallelogram : "))
    height = float(input("Enter the height of the parallelogram : "))
    area = base*height
    side1 = float(input("Enter the first side of the parallelogram : "))
    side2 = float(input("Enter the second of the parallelogram : "))
    perimeter = 2*(side1+side2)

def trapezium () :
    side1 = float(input("Enter the first side of the trapezium : "))
    side2 = float(input("Enter the second side of the trapezium : "))
    height = float(input("Enter the height of the trapezium : "))
    area = 0.5*(side1+side2)*height

    side1 = float(input("Enter the first side of the trapezium : "))
    side2 = float(input("Enter the second side of the trapezium : "))
    side3 = float(input("Enter the third side of the trapezium : "))
    side4 = float(input("Enter the fourth side of the trapezium : "))
    perimeter = side2+side1+side3+side4

def rhombus () :
    diagonal1 = float(input("Enter the first diagonal of the rhombus : "))
    diagonal2 = float(input("Enter the second diagonal of the rhombus : "))
    area = 0.5*diagonal1*diagonal2

    side = float(input("Enter side of rhombus : "))
    perimeter = 4*side

def kite () :
     diagonal1 = float(input("Enter the first diagonal of the kite : "))
     diagonal2 = float(input("Enter the second diagonal of the kite : "))
     area = 0.5*diagonal1*diagonal2

     side1 = float(input("Enter the first side of the kite : "))
     side2 = float(input("Enter the second side of the kite : "))
     perimeter = 2*(side1+side2)

def cube () :
    side = float(input("Enter side of the cube : "))
    sarea = 6*side**2
    volume = side**3

def cuboid () :
    length = float(input("Enter the length of cuboid : "))
    width = float(input("Enter the width of cuboid : "))
    height = float(input("Enter the height of cuboid : "))
    surface_area = 2*(length*width+length*height+width*height)
    volume = length*width*height

def sphere () :
    radius = float(input("Enter the radius of the sphere :"))
    sarea = 4*math.pi*radius**2
    volume = 4.0/3*math.pi*radius**3

def cylinder () :
    radius = float(input("Enter the radius of the cylinder : "))
    height = float(input("Enter the height of cylinder : "))
    sarea = 2*math.pi*radius*(height+radius)
    volume = math.pi*radius**2*height
    
def cone () :
    
    radius = float(input("Enter the radius of the cone : "))
    
    height = float(input("Enter the height of the cone : "))
    slant_height = math.sqrt((radius**2+height**2))
    sarea = math.pi*radius*(slant_height+radius)
    volume = 1/3*math.pi*radius**2*height 

def hemisphere () :
    radius = float(input("Enter the radius of the hemisphere : "))
    sarea = 3*math.pi*radius**2
    volume = 2/3*math.pi*radius**3

def square_pyramid () :

    baselen = float(input("Enter the base length of square pyramid : "))
    height = float(input("Enter vertical height : "))
    base_area = baselen**2
    slant = math.sqrt(height**2 + (baselen/2)**2)
    total_surface_area = base_area+2*base_area*slant
    lateral_surface_area = 2*baselen*slant
    volume = 1/3*base_area*height

def rectangular_pyramid () :
    baselen = float(input("Enter the base length of rectangular pyramid : "))
    basewid = float(input("Enter the base width of rectangular pyramid : "))
    height = float(input("Enter vertical height : "))
    slantlen =  math.sqrt((basewid/2)**2+height**2)
    slantwid = math.sqrt((baselen/2)**2+height**2)
    basearea = baselen*basewid
    surface_area = basearea+baselen*slantwid+basewid*slantlen
    volume = 1/3*baselen*basewid*height
    
def triangular_pyramid () :
    base = float(input("Enter the base of triangular pyramid :"))
    height_base = float(input("Enter the height of triangular base :"))
    pyramid_height = float(input("Enter the height of triangular pyramid from base :"))
    base_area = 0.5(base*height_base)
    volume = (1/3)*base_area*pyramid_height

    side1 = float(input("Enter the first side of the triangular base : "))
    side2 = float(input("Enter the second side of the triangular base : "))
    side3 = float(input("Enter the third side of the triangular base : "))
    s = (side1+side2+side3)/2
    barea = math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))
    svolume = (1/3)*barea*pyramid_height

while True :
    print("---Welcome to shape calculator---")
    print("\nNOTE - To choose a option enter the number before the option.\n")
    print("Choose the type of shape from below options")
    print("1. 2D shapes\n2. 3D shapes\n3. Exit the program")
    choose = input("Enter your choice : ")
    if choose == '1':
        while True :
         print("Choose the following 2D shapes")
         print("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Parallelogram\n6. Trapezium\n7. Rhombus\n8. Kite\n9. Go back")
         shape = input("Choose from above :")
         if shape == '1' :
            square ()
         elif shape == '2' :
            rectangle ()
         elif shape == '3' :
           while True :
            print("Choose the type of triangle ")
            print("1. Basic triangle\n2. Equilateral triangle\n3. Right angled triangle\n4. Go back")
            tri = input("Choose the following : ")
            if tri == '1' :
                triangle ()
            elif tri == '2' :
                equilateral_triangle () 
            elif tri == '3' :
                right_triangle ()
            elif tri == '4' :
                print("Exiting the current page...")
                break
            else :
                print("Invalid choice\nTry again...")
             
         elif shape == '4' :
            circle ()
         elif shape == '5' :
            parallelogram ()
         elif shape == '6' :
            trapezium ()
         elif shape == '7' :
            rhombus ()
         elif shape == '8' :
            kite ()
         elif shape == '9' :
            print("Exiting the current page...")
            break
         else :
            print("Invalid choice.\nTry again..")

    elif choose == '2' :
       while True :
        print("Choose the following 3D shapes ")
        print("1. Cube\n2. Cuboid\n3. Sphere\n4. Cylinder\n5. Cone\n6. Hemisphere\n7. Pyramid\n8. Go back\n")
        Shape = input("Choose from above :")
        if Shape == '1' :
            cube ()
        elif Shape == '2' :
            cuboid ()
        elif Shape == '3' :
            sphere ()
        elif Shape == '4' :
            cylinder ()
        elif Shape == '5' :
            cone ()
        elif Shape == '6' :
            hemisphere ()
        elif Shape == '7' :
           while True :
            print("Choose the type of pyramid.")
            print("1. Square pyramid\n2. Rectangular pyramid\n3. Triangular pyramid \n4. Exit")
            Pyramid = input("Choose the above option : ")
            if Pyramid == '1' :
                square_pyramid ()
            elif Pyramid == '2' :
                rectangular_pyramid ()
            elif Pyramid == '3' :
                triangular_pyramid ()
            elif Pyramid == '4' :
                print("Exiting the current page ...\n")
                break
            else :
                print("Invalid chioce.\nTry again...\n")
        elif Shape == '8' :
            print("Exiting the current page...\n")
            break
        else :
            print("Invalid choice.\nTry again..\n")

    elif choose == '3' :
        print("Exiting the program....\n")
        break

    else :
        print("Invalid choice.\nTry again...\n")


