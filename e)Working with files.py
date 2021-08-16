def balanced(expression):
    a = "("
    b = ")"
    global c
    c = []
    d = expression
    e = len(c)
    count = 0
    
    for i in d:
      if i == a or i == b:
        c.insert(count, i)
        count = count + 1
    #print(c)
        
    count1 = 0
    count2 = 0
    for i in c:
      #print(i)
      
      if a in c:
          #print(a)
          c.remove(a)
          

          if b in c:
            c.remove(b)
            
      if len(c) == 0 or len(c) % 2 == 0:
          return True
      else:
          print(c)
          return False

          """
          #print(c)
          for i in c:
              
            count1 = count1 + 1
            if count1 == len(c):
                break
            else:
              c.insert(count1, a)
              c.insert(count2, b)
              print(c)
            if count2 == len(c):
              break
            
        else:
          print("False")
      else:
        print("False")
    
    if e % 2 == 0:
      print(True)
      """
      
        

print(balanced(input()))