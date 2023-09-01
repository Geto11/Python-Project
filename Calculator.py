app_name = ("🆂🅷🅰🅿🅴🆂 🅰🆁🅴🅰 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁 ")
import sys,time,os
import sys
from termcolor import colored, cprint
text = colored('''䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉
\n ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉๏⁌  🆂🅷🅰🅿🅴🆂 🅰🆁🅴🅰 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁  ⁍๏䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                       \n''', 'yellow', attrs=['reverse', 'blink'])
print(text)

welcome2 = ('''\n____________________________________________________
๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏
  |•____________|• 🅦🅔🅛🅒🅞🅜🅔 🅤🅢🅔🅡 •|____________•|
๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏
____________________________________________________\n''')
for char in welcome2:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
Enter = input('''\n𝙀𝙉𝙏𝙀𝙍  |• 𝙎𝙏𝘼𝙍𝙏 •| 
                     :  ''').upper()

if Enter == "START":
    print("\n____________________________________________________________\n")    
    welcome4 = (f'''
____________________________________________________________\n
         sta        🇸 🇪 🇱 🇪 🇨 🇹  🇲 🇴 🇩 🇪  
|•________________________________________________________•|''')
    for char in welcome4:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.01)
    welcome5 = ('''

        |•__________MODE of SELECTION__________•|
____________________________________________________________     
             ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏
              ⁍ ◯ Circle √ ------ Select A ⁌
              ⁍ ▣  Square √ ------Select B ⁌
              ⁍ △ Triangle √ -----Select C ⁌
              ⁍ ▭ Rectangle √ --- Select D ⁌
              ⁍ ⬭ Ellipse  √ ---- Select E ⁌
              ⁍ ● Sphere   √ ----- Select F ⁌
             ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏
____________________________________________________________ 

''')
    for char in welcome5:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.01)   
    while True:
        print('''____________________________________________________________
              ⁍ |• Enter ' X ' to Quit •| ⁌
                ''')
        Select = input("\n𝐄𝐍𝐓𝐄𝐑 Mode: ").upper()
        if Select == "A":
              print('''\n          |• Getting The Area of The Circle ◯ •|
              ''')
              print('''Determining The Area Using:
                  A1 = Diameter
                  A2 = Radius
____________________________________________________________''')
              selection = input("\nSelect Your Choice: ").upper()
              if selection == "A1":
                 print("\n(|• Using Diameter •|)")                  
                 diameter = float(input("\nEnter Diameter: "))
                 pi = 3.14
                 radius = diameter/2
                 area = pi*(radius**2) 
                 radius_squared = radius**2      
              
                 def area_circle(radius, pi = 3.14):
                     radius = diameter/2
                     area = pi*(radius**2)
                     print("\n")
                     return '''The Area of This Circle with a Diameter of ({}) is ({})
'''.format(diameter, area)
                         
                 a = area_circle(radius, pi = 3.14)
                 print(a)
                     
                 print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
                 
                 bmb = ('''____________________________________________________________

''')
                 for char in bmb:
                       sys.stdout.write(char)
                       sys.stdout.flush()
                       time.sleep(0.01)                 
                 print (''' 
         ___________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ''')

                 time.sleep(5)
                 jhj = ('''____________________________________________________________
''')
                 for char in jhj:
                       sys.stdout.write(char)
                       sys.stdout.flush()
                       time.sleep(0.01)
                 
                 brb = ('''\n
                     |• SOLUTION •|

(Step - 1)
    Given:

             |• formula (A = pi * radius²) 
               |• pi = {}
               |• d = {}
             |• (r = d/2) or  r = {}/2
               |• r = {}

(Step - 2)
    Simplify:

           |• A = pi(r²) which is A = {}({})² •|
           |• A = {}({})
 
(Answer)

           |• The area of the Circle is {} •|'''.format(pi, diameter, diameter, radius, pi, radius,pi, radius_squared, area))           
                 for char in brb:
                       sys.stdout.write(char)
                       sys.stdout.flush()
                       time.sleep(0.1)
                   
                   
              elif selection == "A2":
                     print("\n (|• Using Radius •|)")
                     radius = float(input("\nEnter Radius: "))
                     squared = radius**2
                     pi = 3.14
                     area = pi * (radius**2)
                     def area_circle(radius, pi = 3.14): 
                         print("\n")
                         return "The Area of This Circle with a Radius of ({}) is ({})".format(radius, area)    
                     a = area_circle(radius, pi = 3.14)
                     print(a)

                     print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")

                     bob = ('''____________________________________________________________
''')
                     for char in bob:
                           sys.stdout.write(char)
                           sys.stdout.flush()
                           time.sleep(0.01)
                     print("\n")
                     print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

                     time.sleep(5)
                     jmj = ('''____________________________________________________________
''')
                     for char in jmj:
                           sys.stdout.write(char)
                           sys.stdout.flush()
                           time.sleep(0.01)

                     byb = ('''\n
                     |• SOLUTION •|

(Step - 1)
    Given:

             |• formula (A = pi * radius²)
             |• pi = {}
             |• r = {}

(Step - 2)
    Simplify:

         |• A = pi(r²) which is A = {}({})² •|
         |• A = {}({})

(Answer)

         |• The area of the Circle is {} •|'''.format(pi, radius, pi, radius, pi, squared, area))
           
                     for char in byb:
                           sys.stdout.write(char)
                           sys.stdout.flush()
                           time.sleep(0.1)
              else:
                   print('''                     |• INVALID INPUT •|    
|•________________________________________________________•|''')
              print("\n")
              
#Square

        elif Select == "B":     
               print('''\n          |• Getting The Area of The Square ▣ •|
               ''')  
               Length = float(input("\nEnter Length: "))
               area = Length**2
               def area_square(area):
                         print("\n")
                         return "The Area of This Square with a Length of ({}) is ({})".format(Length, area)    
               a = area_square(Length**2)
               print(a)
               
               print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
               b1b = ('''____________________________________________________________
''')
               for char in b1b:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.01)
               print("\n")
               print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

               time.sleep(5)
               jmj = ('''____________________________________________________________
''')
               for char in jmj:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.01)
               b1b = ('''\n
                     |• SOLUTION •|

(Step - 1)
    Given:

               |• formula (A = Length²)
               |• L = {}
 
(Step - 2)
    Simplify:

               |• A = L² which is A = {}² •|

(Answer)

               |• The area of the Square is {} •|'''.format(Length, Length, area))
           
               for char in b1b:
                      sys.stdout.write(char)
                      sys.stdout.flush()
                      time.sleep(0.1)
#Triangle          
        elif Select == "C":
            print('''\n          |• Getting The Area of The Triangle △ •|
               ''')
            Base = float(input("\nEnter Base: "))
            Height = float(input("\nEnter Height: "))
            area = Base * Height/2
            sum = Base * Height
            def area_triangle(area):
                         print("\n")
                         return "The Area of This Triangle with Base({}) and Height({})is ({})".format(Base, Height, area)    
            a = area_triangle(area)
            print(a)
    
            print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
            b1b = ('''____________________________________________________________
''')
            for char in b1b:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.01)
            print("\n")
            print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

            time.sleep(5)
            jmj = ('''____________________________________________________________
''')
            for char in jmj:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.01)
            b1b = ('''\n
                      |• SOLUTION •|

(Step - 1)
      Given:

               |• formula (A = B*H/2)
               |• B = {}
               |• H = {}
 
(Step - 2)
      Simplify:

           |• A = B*H/2  which is A = ({}*{})/2 •|
           |• A = ({})/2

(Answer)

           |• The area of the Triangle is {} •|'''.format(Base, Height, Base, Height, sum, area))
           
            for char in b1b:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.1)

               
#Rectangle
        elif Select == "D":
               print('''\n          |• Getting The Area of The Rectangle ▭ •|
               ''')
               Length = float(input("Enter Length: "))
               Width = float(input("Enter Width: "))
               Area = Length*Width
               def area_rectangle(Area):
                         print("\n")
                         return "The Area of This Rectangle with Length({}) and Width({}) is ({})".format(Length, Width, Area)    
               a = area_rectangle(Length*Width)
               print(a)

               print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
               bqb = ('''____________________________________________________________
''')
               for char in bqb:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.01)
               print("\n")
               print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

               time.sleep(5)
               juj = ('''____________________________________________________________
''')
               for char in juj:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.01)
               bgb = ('''\n
                     |• SOLUTION •|

(Step - 1)
      Given:

                  |• formula (A = L*W)
                  |• L = {}
                  |• W = {}
 
(Step - 2)
      Simplify:

           |• A = L*W which is A = {}*{} •|

(Answer)

           |• The area of the Rectangle is {} •|'''.format(Length, Width, Length, Width, Area))
           
               for char in bgb:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.1)

#Elipse
        elif Select == "E":
            print('''\n          |• Getting The Area of The Ellipse ⬭ •|
               ''')
            pi = 3.14
            a = float(input("Enter 1st Axis: "))
            b = float(input("Enter 2nd Axis: "))
            Area = pi * (a*b)
            sum = a * b
            def area_square(area):
                         print("\n")
                         return "The Area of This Ellipse with Axis of ({}) and ({}) is ({})".format(a, b, Area)    
            Sum = area_square(Area)
            print(Sum)
            
            print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
            bmb = ('''____________________________________________________________
''')
            for char in bmb:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.01)
            print("\n")
            print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

            time.sleep(5)
            jmp = ('''____________________________________________________________
''')
            for char in jmp:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.01)
            b3b = ('''\n
                     |• SOLUTION •|
(Step - 1)
       Given:

                |• formula (A = pi(a*b))
                |• a = {} (1st Axis)
                |• b = {} (2nd Axis)
 
(Step - 2)
       Simplify:

         |• A = pi(a*b) which is A = {}({}*{}) •|
         |• A = {} * ({})

(Answer)

         |• The area of the Ellipse is {} •|'''.format(a, b, pi, a, b, pi, sum, Area))
           
            for char in b3b:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.1)

#Sphere
        elif Select == "F":
                  print('''\n          |• Getting The Area of The Sphere ● •|
               ''')
                  print('''|• Determining the Surface Area Using:
                      |• S1 = Radius
                      |• S2 = Diameter
____________________________________________________________''')
                  select = input("Enter Your Choice: ").upper()
                  if select == "S1":
                      print("\n |• Using Radius •|")
                      Radius = float(input("\nEnter Radius: "))
                      radius_squared = Radius**2
                      pi = 3.14
                      sum = pi * radius_squared
                      Area = 4 * pi*(Radius**2)
                  
                      def area_sphere(Radius, pi = 3.14):
                          print("\n")                      
                          return "The Area of this Sphere with Radius of ({}) is ({})".format(Radius, Area)
                      Sum = area_sphere(Radius, pi = 3.14)    
                      print(Sum) 
                      print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
                      bmb = ('''____________________________________________________________
''')
                      for char in bmb:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                      print("\n")
                      print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

                      time.sleep(5)
                      jmp = ('''____________________________________________________________
''')
                      for char in jmp:
                           sys.stdout.write(char)
                           sys.stdout.flush()
                           time.sleep(0.01)  
                                     
                      b4b = ('''\n
                     |• SOLUTION •|
(Step - 1)
       Given:

                |• formula (A = 4 * pi(r)²)
                |• r = {} 
 
(Step - 2)
       Simplify:

      |• A = 4s * pi(r)² which is A = 4 * {}({})² •|
          |• A = 4 * {} ({})
          |• A = 4({} * {})
          |• A = 4 * {}
 
(Answer)

      |• The area of the Sphere is {} •|'''.format(Radius, pi, Radius,pi, radius_squared, pi, radius_squared, sum, Area))
           
                      for char in b4b:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                  elif select == "S2":
                      print("\n |• Using Diameter •|")
                      Diameter = float(input("\nEnter Diameter: "))
                      squared = Diameter**2
                      pi = 3.14
                      Area = pi*(squared)

                      def area_sphere(Diameter, pi = 3.14):
                          print("\n")
                          return "The Area of this Sphere with a diameter of ({}) is ({})".format(Diameter, Area)
                      Sum = area_sphere(Diameter, pi = 3.14)    
                      print(Sum) 
                      print("\n          |• HERE'S THE STEP BY STEP CALCULATION •|")
                      bmb = ('''____________________________________________________________
''')
                      for char in bmb:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                      print("\n")
                      print (''' 
       _____________________________________________
⁍⁍⁍⁍⁍⁍⁍⁍|• GENERATING THE SOLUTION PLEASE STAND BY •|⁌⁌⁌⁌⁌⁌⁌
       ๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏๏''')

                      time.sleep(5)
                      jmp = ('''____________________________________________________________
''')
                      for char in jmp:
                           sys.stdout.write(char)
                           sys.stdout.flush()
                           time.sleep(0.01)  
                                     
                      b4b = ('''\n
                     |• SOLUTION •|

(Step - 1)
    Given:

               |• formula (A = pi(d)²)
                  |• d = {} 
 
(Step - 2)
    Simplify:

          |• A = pi(d)² which is A = {}({})² •|
               |• A = {} * {}

(Answer)

          |• The area of the Sphere is {} •|'''.format(Diameter, pi, Diameter, pi, squared, Area))
           
                      for char in b4b:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                      
                  else:
                        print("       |•___INVALID INPUT___•|")
                        print("\n")            
                                                
 #Quit            
        elif Select == "X":
            print("\n")
            welcomeX = ('''\n       |•________THANK YOU FOR USING THE APP.________•|
|•________________________________________________________•|''')
            for char in welcomeX:
                  sys.stdout.write(char)
                  sys.stdout.flush()
                  time.sleep(0.02)
            break
            
        else:
            print("       |•___INVALID INPUT___•|")
        print("\n")

          
                              
          #End of Loop
elif Enter == "QUIT":
    welcomeA = ('''\n       |•________THANK YOU FOR USING THE APP.________•|
|•________________________________________________________•|''')
    for char in welcomeA:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.02)
else:
    print('''                     |• INVALID INPUT •|    
|•________________________________________________________•|''')

print(text)