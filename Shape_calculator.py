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
    
    side = float(input("Enter the side of equilateral triangle : "))
    eqarea = 3**0.5/4*side
    eqperimeter = side*3
    hypo = float(input("Enter the hypotenous of the triangle : "))

    side1 = float(input("Enter the first side of the triangle : "))
    side2 = float(input("Enter the second of the triangle : "))
    side3 = float(input("Enter the third of the triangle : "))
    perimeter = side1+side2+side3

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
    radius = float(input("Enter the radius of the sphere"))
    sarea = 4*math.pi*radius**2
    volume = 4/3*math.pi*radius**3

def cylinder () :
    radius = float(input("Enter the radius of the cylinder : "))
    height = float(input("Enter the height of cylinder : "))
    sarea = 2*math.pi*radius(height+radius)
    volume = math.pi*radius**2*height
    
def cone () :
    
    radius = float(input("Enter the radius of the cone : "))
    
    height = float(input("Enter the height of the cone : "))
    slant_height = math.sqrt((radius**2+height**2))
    sarea = math.pi*radius(slant_height+radius)
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
    lateral_surface_area = 2*base_area*slant
    volume = 1/3*base_area*height

def rectangular_pyramid () :
    baselen = float(input("Enter the base length of rectangular pyramid : "))
    basewid = float(input("Enter the base width of rectangular pyramid : "))
    height = float(input("Enter vertical height : "))
    slantlen =  math.sqrt((basewid/2)**2+height**2)
    slantwid = math.sqrt((baselen/2)**2+height**2)
    basearea = baselen*basewid


