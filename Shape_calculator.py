import math

## Explaination of this block is similar to all other defination and main block of code

def square () : # creates a function 
   while True : # runs a loop until the user select a option where it breakes this loop 
    print("\nWhat do you want to calculate\n1. Perimeter of square\n2. Area of square\n3. Go back")
    choose = input("Choose the following : ") # accepts all input 
    if  choose == '1' : # filters and only see if 1 as a input has been given or not
     try: # it will not let the whole programm crash due to non float input by user.
        side = float(input("Enter the side of the square (in cm): ")) # accepts only float
        if side <= 0: # sides cannot be 0 and negetive for shapes
         print("Side length must be a positive number.")
         continue # it skips this part which is not valid length
     except ValueError: # will show the below massage and skip the invalid part.
         print("Invalid input! Please enter a number.")
         continue
     perimeter = 4*side # calculates the perimeter 
     print(f"Perimeter of the square is {perimeter}") 
    elif choose == '2' : # checks if 2 is given as input
     try:
       side = float(input("Enter the side of the square (in cm): "))
       if side <= 0:
           print("Side length must be a positive number.")
           continue
     except ValueError:
       print("Invalid input! Please enter a number.")
       continue
     area = side*side
     print(f"Area of square is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break # breakes the current loop and takes back to previous loop
    else : # if no input matches it will run this block of code.
       print("Invalid choice\nTry again...\n") 
    
def rectangle () :
   while True : 
    print("\nWhat do you want to calculate\n1. Perimeter of rectangle\n2. Area of rectangle\n3. Go back")
    choose = input("Choose the following : ") 
    if  choose == '1' :
     try:  
        length = float(input("Enter the length of the rectangle (in cm) : ")) 
        width = float(input("Enter the width of the rectangle (in cm) : "))
        if length <= 0 and width <= 0: 
         print("length and width must be a positive number.")
         continue 
     except ValueError: 
         print("Invalid input! Please enter a number.")
         continue
     perimeter = 2*(length+width)  
     print(f"Perimeter of the rectangle is {perimeter}sq.cm") 
    elif choose == '2' :
     try:
      length = float(input("Enter the length of the rectangle (in cm) : ")) 
      width = float(input("Enter the width of the rectangle (in cm) : "))
      if length <= 0 and width <= 0: 
         print("length and width must be a positive number.")
         continue
     except ValueError :
       print("Please enter a number.")
       continue
     area = length*width
     print(f"Area of rectangle is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break 
    else : 
       print("Invalid choice\nTry again...\n")

def triangle () :
  while True :
    print("\nWhat do you want to calculate\n1. Perimeter of triangle\n2. Area of triangle\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
       side1 = float(input("Enter the first side of the triangle (in cm) : "))
       side2 = float(input("Enter the second of the triangle (in cm) : "))
       side3 = float(input("Enter the third of the triangle (in cm) : "))
       if side1 <= 0 and side2 <= 0 and side3 <= 0 :
          print("Number should be positive.")
          continue
       perimeter = side1+side2+side3
       print(f"Perimeter of triangle is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       base = float(input("Enter the base of the triangle (in cm) : "))
       height = float(input("Enter the height of the triangle (in cm) : "))
       if base <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      area = 0.5*base*height
      print(f"Area of triangle is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")
    
def right_triangle () :
    while True :
     print("\nWhat do you want to calculate\n1. Perimeter of triangle\n2. Area of triangle\n3. Hypotenous of the triangle\n4. Go back")
     choose = input("Choose the following : ")
     if choose == '1' :
      try :
       base = float(input("Enter the base of the triangle (in cm) : "))
       height = float(input("Enter the height of the triangle (in cm) : "))
       if base <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
       perimeter = base + height + math.sqrt(base**2+height**2) 
       print(f"Perimeter of triangle is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
     elif choose == '2' :
      try :
       base = float(input("Enter the base of the triangle (in cm) : "))
       height = float(input("Enter the height of the triangle (in cm) : "))
       if base <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      area = 0.5*base*height
      print(f"Area of triangle is {area}sq.cm")

     elif choose == '3' :
      try :
       base = float(input("Enter the base of the triangle (in cm) : "))
       height = float(input("Enter the height of the triangle (in cm) : "))
       if base <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      hypo = math.sqrt(base**2+height**2)
      print(f"Hypotenous of triangle is {hypo}sq.cm")
     elif choose == '4' :
       print("Exiting the current page....")
       break
     else :
       print("Invalid input\nTry again...")

def equilateral_triangle () :
    
    while True :
      print("\nWhat do you want to calculate\n1. Perimeter of triangle\n2. Area of triangle\n3. Go back")
      choose = input("Choose the following : ")
      if choose == '1' :
       try :
        side = float(input("Enter the side of equilateral triangle (in cm) : "))
        if side <= 0 :
          print("Number should be positive.")
          continue
        eqperimeter = side*3 
        print(f"Perimeter of equilateral triangle is {eqperimeter}sq.cm")
       except ValueError :
         print("Please enter a number.")
         continue
      elif choose == '2' :
       try :
        side = float(input("Enter the side of equilateral triangle (in cm) : "))
        if side <= 0 :
          print("Number should be positive.")
          continue
       except ValueError :
        print("Please enter a number.")
        continue
       eqarea = math.sqrt(3)/4*side**2
       print(f"Area of equilateral triangle is {eqarea}sq.cm")
      elif choose == '3' :
         print("Exiting the current page....")
         break
      else :
       print("Invalid input\nTry again...")

def circle () :
 while True :
      print("\nWhat do you want to calculate\n1. Circumference of circle\n2. Area of circle\n3. Go back")
      choose = input("Choose the following : ")
      if choose == '1' :
       try :
        radius = float(input("Enter the radius of the circle (in cm) : "))
        if radius <= 0 :
          print("Number should be positive.")
          continue
        circumference = 2*math.pi*radius
        print(f"Circumference of circle is {circumference}sq.cm")
       except ValueError :
         print("Please enter a number.")
         continue
      elif choose == '2' :
       try :
        radius = float(input("Enter the radius of circle (in cm) : "))
        if radius <= 0 :
          print("Number should be positive.")
          continue
       except ValueError :
        print("Please enter a number.")
        continue
       area = math.pi*radius*radius
       print(f"Area of circle is {area}sq.cm")

      elif choose == '3' :
       print("Exiting the current page....")
       break
      else :
       print("Invalid input\nTry again...")
    
def parallelogram () :
 while True :
    print("\nWhat do you want to calculate\n1. Perimeter of parallelogram\n2. Area of parallelogram\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
       side1 = float(input("Enter the first side of the parallelogram : "))
       side2 = float(input("Enter the second of the parallelogram : "))
       if side1 <= 0 and side2 <= 0 :
          print("Number should be positive.")
          continue
       perimeter = 2*(side1+side2)
       print(f"Perimeter of parallelogram is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       base = float(input("Enter the base of the parallelogram : "))
       height = float(input("Enter the height of the parallelogram : "))
       if base <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      area = base*height
      print(f"Area of parallelogram is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def trapezium () :
 while True :
    print("\nWhat do you want to calculate\n1. Perimeter of trapezium\n2. Area of trapezium\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        side1 = float(input("Enter the first side of the trapezium (in cm) : "))
        side2 = float(input("Enter the second side of the trapezium (in cm) : "))
        side3 = float(input("Enter the third side of the trapezium (in cm) : "))
        side4 = float(input("Enter the fourth side of the trapezium (in cm) : "))
        if side1 <= 0 and side2 <= 0 and side3 <=0 and side4 <= 0 :
          print("Number should be positive.")
          continue
        perimeter = side2+side1+side3+side4
        print(f"Perimeter of parallelogram is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        side1 = float(input("Enter the first side of the trapezium (in cm) : "))
        side2 = float(input("Enter the second side of the trapezium (in cm) : "))
        height = float(input("Enter the height of the trapezium (in cm) : "))
        if side1 <= 0 and side2 <= 0 and height <=0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      area = 0.5*(side1+side2)*height
      print(f"Area of parallelogram is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def rhombus () :
 while True :
    print("\nWhat do you want to calculate\n1. Perimeter of rhombus\n2. Area of rhombus\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        side = float(input("Enter side of rhombus : "))
        if side <= 0 :
          print("Number should be positive.")
          continue
        perimeter = side*4
        print(f"Perimeter of rhombus is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        diagonal1 = float(input("Enter the first diagonal of the rhombus : "))
        diagonal2 = float(input("Enter the second diagonal of the rhombus : "))
        if diagonal1 <= 0 and diagonal2 <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
       print("Please enter a number.")
       continue
      area = 0.5*diagonal1*diagonal2
      print(f"Area of rhombus is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def kite () :
 while True :
    print("\nWhat do you want to calculate\n1. Perimeter of kite\n2. Area of kite\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        side1 = float(input("Enter the first side of the kite : "))
        side2 = float(input("Enter the second side of the kite : "))
        if side1 <= 0 and side2 <=0 :
          print("Number should be positive.")
          continue
        perimeter = 2*(side1+side2)
        print(f"Perimeter of kite is {perimeter}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        diagonal1 = float(input("Enter the first diagonal of the kite : "))
        diagonal2 = float(input("Enter the second diagonal of the kite : "))
        if diagonal1 <= 0 and diagonal2 <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      area = 0.5*diagonal1*diagonal2
      print(f"Area of kite is {area}sq.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def cube () :
 while True :
    print("\nWhat do you want to calculate\n1. Surface area of cube\n2. volume of cube\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        side = float(input("Enter side of the cube : "))
        if side <= 0 :
          print("Number should be positive.")
          continue
        sarea = 6*side**2
        print(f"Surface area of cube is {sarea}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        side = float(input("Enter side of the cube : "))
        if side <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = side**3
      print(f"Volume of cube is {volume}cube.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def cuboid () :
 while True :
    print("\nWhat do you want to calculate\n1. Surface area of cuboid\n2. volume of cuboid\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        length = float(input("Enter the length of cuboid : "))
        width = float(input("Enter the width of cuboid : "))
        height = float(input("Enter the height of cuboid : "))
        if length <= 0 and width <=0 and height <=0 :
          print("Number should be positive.")
          continue
        surface_area = 2*(length*width+length*height+width*height)
        print(f"Surface area of cuboid is {surface_area}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       length = float(input("Enter the length of cuboid : "))
       width = float(input("Enter the width of cuboid : "))
       height = float(input("Enter the height of cuboid : "))
       if length <= 0 and width <=0 and height <=0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = length*width*height
      print(f"Volume of cuboid is {volume}cube.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")
    
def sphere () :
  while True :
    print("\nWhat do you want to calculate\n1. Surface area of sphere\n2. volume of sphere\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        radius = float(input("Enter the radius of the sphere :"))
        if radius <= 0 :
          print("Number should be positive.")
          continue
        sarea = 4*math.pi*radius**2
        print(f"Surface area of sphere is {sarea}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       radius = float(input("Enter the radius of the sphere :"))
       if radius <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = 4.0/3*math.pi*radius**3
      print(f"Volume of sphere is {volume}cube.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def cylinder () :
  while True :
    print("\nWhat do you want to calculate\n1. Surface area of cylinder\n2. volume of cylinder\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        radius = float(input("Enter the radius of cylinder : "))
        height = float(input("Enter the height of cylinder : "))
        if radius <= 0 and height <=0 :
          print("Number should be positive.")
          continue
        sarea = 2*math.pi*radius*(height+radius)
        print(f"Surface area of cylinder is {sarea}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       radius = float(input("Enter the radius of the cylinder : "))
       height = float(input("Enter the height of cylinder : "))
       if radius <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = math.pi*radius**2*height
      print(f"Volume of cylinder is {volume}cube.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def cone () :
  while True :
    print("\nWhat do you want to calculate\n1. Slant height of cone\n2. Surface area of cone\n3. Volume of cone\n4. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        radius = float(input("Enter the radius of the cone : "))
        height = float(input("Enter the height of the cone : "))
        if radius <= 0 and height <=0 :
          print("Number should be positive.")
          continue
        slant_height = math.sqrt((radius**2+height**2))
        print(f"Slant height of cone is {slant_height}cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       radius = float(input("Enter the radius of the cone : "))
       height = float(input("Enter the height of the cone : "))
       if radius <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      slant_height = math.sqrt((radius**2+height**2))
      sarea = math.pi*radius*(slant_height+radius)
      print(f"Surface area of cone is {sarea}sq.cm")
    elif choose == '3' :
      try :
       radius = float(input("Enter the radius of the cone : "))
       height = float(input("Enter the height of the cone : "))
       if radius <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = 1/3*math.pi*radius**2*height
      print(f"Volume of cone is {volume}cube.cm")
    elif choose == '4' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...") 

def hemisphere () :
 
 while True :
    print("\nWhat do you want to calculate\n1. Surface area of hemisphere\n2. volume of hemisphere\n3. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
      try :
        radius = float(input("Enter the radius of the hemisphere : "))
        if radius <= 0 :
          print("Number should be positive.")
          continue
        sarea = 3*math.pi*radius**2
        print(f"Surface area of hemisphere is {sarea}sq.cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
       radius = float(input("Enter the radius of the hemisphere : "))
       if radius <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = 2/3*math.pi*radius**3
      print(f"Volume of hemisphere is {volume}cube.cm")
    elif choose == '3' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...")

def square_pyramid () :
 while True :
    print("\nWhat do you want to calculate\n1. Base area of square pyramid\n2. Slant height of square pyramid\n3. Lateral surface area of square pyramid\n4. Total surface area of square pyramid\n5. Volume of square pyramid\n6. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
     try :
        baselen = float(input("Enter the base length of square pyramid : "))
        if baselen <= 0 :
          print("Number should be positive.")
          continue
        base_area = baselen**2
        print(f"Base area of square pyramid is {base_area}sq.cm")
     except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        baselen = float(input("Enter the base length of square pyramid : "))
        height = float(input("Enter vertical height : "))
        if baselen <= 0 and height <=0 :
          print("Number should be positive.")
          continue
        slant = math.sqrt(height**2 + (baselen/2)**2)
        print(f"Slant height of square pyramid is {slant}cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '3' :
      try :
       baselen = float(input("Enter the base length of square pyramid : "))
       height = float(input("Enter vertical height of square pyramid : "))
       if baselen <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      slant = math.sqrt(height**2 + (baselen/2)**2)
      lateral_surface_area = 2*baselen*slant
      print(f"Lateral surface area of cone is {lateral_surface_area}sq.cm")
    elif choose == '4':
      try :
       baselen = float(input("Enter the base length of square pyramid : "))
       height = float(input("Enter vertical height : "))
       if baselen <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      base_area = baselen**2
      slant = math.sqrt(height**2 + (baselen/2)**2)
      total_surface_area = base_area+2*base_area*slant
      print(f"Total surface area of cone is {total_surface_area}sq.cm")
    elif choose == '5':
      try :
       baselen = float(input("Enter the base length of square pyramid : "))
       height = float(input("Enter vertical height : "))
       if baselen <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      base_area = baselen**2
      volume = 1/3*base_area*height
      print(f"Volume of square pyramid is {volume}cube.cm")
    elif choose == '6' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...") 

def rectangular_pyramid () :
 while True :
    print("\nWhat do you want to calculate\n1. Base area of rectangular pyramid\n2. Slant height of rectangular pyramid\n3. Slant width of rectangular pyramid\n4. Total surface area of rectangular pyramid\n5. Volume of rectangular pyramid\n6. Go back")
    choose = input("Choose the following : ")
    if choose == '1' :
     try :
        baselen = float(input("Enter the base length of rectangular pyramid : "))
        basewid = float(input("Enter the base width of rectangular pyramid : "))
        if baselen <= 0 and basewid <=0 :
          print("Number should be positive.")
          continue
        base_area = baselen*basewid
        print(f"Base area of rectangular pyramid is {base_area}sq.cm")
     except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '2' :
      try :
        basewid = float(input("Enter the base width of rectangular pyramid : "))
        height = float(input("Enter vertical height : "))
        if basewid <= 0 and height <=0 :
          print("Number should be positive.")
          continue
        slantlen =  math.sqrt((basewid/2)**2+height**2)
        print(f"Slant length of rectangular pyramid is {slantlen}cm")
      except ValueError :
         print("Please enter a number.")
         continue
    elif choose == '3' :
      try :
       baselen = float(input("Enter the base length of rectangular pyramid : "))
       height = float(input("Enter vertical height of rectangular pyramid : "))
       if baselen <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      slantwid = math.sqrt((baselen/2)**2+height**2)
      print(f"Slant width of rectangular pyramid is {slantwid}sq.cm")
    elif choose == '4':
      try :
       baselen = float(input("Enter the base length of rectangular pyramid : "))
       basewid = float(input("Enter the base width of rectangular pyramid : "))
       height = float(input("Enter vertical height : "))
       if baselen <= 0 and height <= 0 and basewid <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      slantlen =  math.sqrt((basewid/2)**2+height**2)
      slantwid = math.sqrt((baselen/2)**2+height**2)
      base_area = baselen*basewid
      surface_area = base_area+baselen*slantwid+basewid*slantlen

      print(f"Total surface area of cone is {surface_area}sq.cm")
    elif choose == '5':
      try :
       basewid = float(input("Enter the base width of rectangular pyramid : "))
       baselen = float(input("Enter the base length of rectangular pyramid : "))
       height = float(input("Enter vertical height : "))
       if baselen <= 0 and height <= 0 :
          print("Number should be positive.")
          continue
      except ValueError :
        print("Please enter a number.")
        continue
      volume = 1/3*baselen*basewid*height
      print(f"Volume of rectangular pyramid is {volume}cube.cm")
    elif choose == '6' :
       print("Exiting the current page....")
       break
    else :
       print("Invalid input\nTry again...") 
    
def triangular_pyramid () :
 while True:
    print("\nWhat do you want to calculate?")
    print("1. Base area of triangular pyramid")
    print("2. Volume using base and height")
    print("3. Volume using Heron's formula")
    print("4. Lateral surface area")
    print("5. Total surface area")
    print("6. Go back")
    choice = input("Choose the following: ")

    if choice == '1':
     try:
      base = float(input("Enter the base of the triangular base: "))
      height_base = float(input("Enter the height of the triangular base: "))
      if base <= 0 or height_base <= 0:
       print("Numbers should be positive.")
       continue
      base_area = 0.5 * base * height_base
      print(f"Base area of triangular pyramid is {base_area} sq.cm")
     except ValueError:
         print("Please enter valid numbers.")
     continue

    elif choice == '2':
     try :
       base = float(input("Enter the base of the triangular base : "))
       height_base = float(input("Enter the height of the triangular base : "))
       pyramid_height = float(input("Enter the height of the pyramid : "))
       if base <= 0 or height_base <= 0 or pyramid_height <= 0:
        print("Numbers should be positive.")
        continue
       base_area = 0.5 * base * height_base
       volume = (1/3) * base_area * pyramid_height
       print(f"Volume of triangular pyramid is {volume} cubic cm")
     except ValueError:
      print("Please enter valid numbers.")
     continue
     

    elif choice == '3':
     try:
      side1 = float(input("Enter the first side of the triangular base: "))
      side2 = float(input("Enter the second side of the triangular base: "))
      side3 = float(input("Enter the third side of the triangular base: "))
      pyramid_height = float(input("Enter the height of the pyramid: "))
      if side1 <= 0 or side2 <= 0 or side3 <= 0 or pyramid_height <= 0:
       print("Numbers should be positive.")
       continue
      s = (side1 + side2 + side3) / 2
      base_area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
      volume = (1/3) * base_area * pyramid_height
      print(f"Base area using Heron's formula: {base_area} sq.cm")
      print(f"Volume of triangular pyramid is {volume} cubic cm")
     except ValueError:
      print("Please enter valid numbers.")
      continue

    elif choice == '4':
        try:
         side1 = float(input("Enter the first side of the triangular base: "))
         side2 = float(input("Enter the second side of the triangular base: "))
         side3 = float(input("Enter the third side of the triangular base: "))
         slant_height = float(input("Enter the slant height of the pyramid: "))
         if side1 <= 0 or side2 <= 0 or side3 <= 0 or slant_height <= 0:
          print("Numbers should be positive.")
         continue
         perimeter = side1 + side2 + side3
         lateral_area = 0.5 * perimeter * slant_height
         print(f"Lateral surface area is {lateral_area} sq.cm")
        except ValueError:
         print("Please enter valid numbers.")
        continue

    elif choice == '5':
     try:
      side1 = float(input("Enter the first side of the triangular base: "))
      side2 = float(input("Enter the second side of the triangular base: "))
      side3 = float(input("Enter the third side of the triangular base: "))
      slant_height = float(input("Enter the slant height of the pyramid: "))
      if side1 <= 0 or side2 <= 0 or side3 <= 0 or slant_height <= 0:
       print("Numbers should be positive.")
       continue
      s = (side1 + side2 + side3) / 2
      base_area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
      perimeter = side1 + side2 + side3
      lateral_area = 0.5 * perimeter * slant_height
      total_area = base_area + lateral_area
      print(f"Total surface area is {total_area} sq.cm")
     except ValueError:
      print("Please enter valid numbers.")
      continue

    elif choice == '6':
     print("Exiting triangular pyramid calculator...")
     break

    else:
     print("Invalid input. Try again.")


print("---Welcome to shape calculator---")
print("\nNOTE - To choose a option enter the number before the option.\n")
while True :
    print("\nChoose the type of shape from below options")
    print("1. 2D shapes\n2. 3D shapes\n3. Exit the program")
    choose = input("Enter your choice : ")
    if choose == '1':
        while True :
         print("\nChoose the following 2D shapes")
         print("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Parallelogram\n6. Trapezium\n7. Rhombus\n8. Kite\n9. Go back")
         shape = input("Choose from above : ")
         if shape == '1' :
            square ()
         elif shape == '2' :
            rectangle ()
         elif shape == '3' :
           while True :
            print("\nChoose the type of triangle ")
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
        print("\nChoose the following 3D shapes ")
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
            print("\nChoose the type of pyramid.")
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


