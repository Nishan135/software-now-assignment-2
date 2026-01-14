def edge(turtle,length, depth):
  
  if depth == 0:
    turtle.forward(length)
  else:  
    segment= length / 3

    edge(turtle,segment, depth - 1)
    
    turtle.right(60)
    
     
    edge(turtle,segment, depth - 1)
    
    turtle.left(120) 
    
    edge(turtle,segment, depth - 1)
    turtle.right(60)
    edge(turtle,segment, depth - 1)