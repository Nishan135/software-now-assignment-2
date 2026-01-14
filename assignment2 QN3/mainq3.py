import turtle
from recursive import edge


  #Defening the main function.  
def main (): 

  screen = turtle.Screen() 
  screen.title("Recursive Pattern Drawer") 
  screen.bgcolor("white") 


  pen = turtle.Turtle()
  pen.speed(0)
  pen.color("black") 
  pen.pensize(1) 
  
#user inputs from the user for sides, length and depth.
  try:
    sides = int(input("Enter the number of sides:"))
    length = float(input("Enter the side length:"))
    depth = int(input("Enter the recursion depth:"))
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    return
  
  
  pen.penup()
  pen.goto(-length / 2, length / 2)
  pen.pendown() 
  
  #Calculating the angle based on the number of sides given by the user.
  angle = 360 / sides   
  for _ in range(sides): 
    edge(pen,length, depth)
    pen.right(angle) 
#Hiding the turtle after drawing is completed.
  pen.hideturtle()  
    
  screen.mainloop()
  
if __name__ == "__main__": 
  main()
