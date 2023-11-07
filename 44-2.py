#https://www.youtube.com/watch?v=483vwaq7qjo&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=64
#still have to elimate duplicates
import random
array = [[0,0,0,],[0,"BINGO",0],[0,0,0]]
used_numbers = set()


for i in range(0,3):
    for z in range(0,3):
            
            var = random.randint(1, 99)
            #als var uniek is append, als var niet uniek is blijf loop until unieke balue
           
            while var in used_numbers:
                var = random.randint(1, 99)

            if array[i][z] != "BINGO":
                array[i][z] = var
                used_numbers.add(var)
          

                
                        
                 

         

while True:
     a=(f"{array[0][0]:^4}|{array[0][1]:^8}|{array[0][2]:>4}")
     b=(f"{array[1][0]:^4}|{array[1][1]:^7} |{array[1][2]:>4}")
     c=(f"{array[2][0]:^4}|{array[2][1]:^8}|{array[2][2]:>4}")

     total_lenght = len(a) +1

     print(a)
     print("-" * total_lenght)
     print(b)
     print("-" * total_lenght)
     print(c)
     print()
     number = input("What's the called out number?: ")
     number = int(number)
     if number == "q":
         break

     for i in range(len(array)):
         for j in range(len(array)):
             if array[i][j] == number:
                 array[i][j] = "X"
                 print(f"{array[i][j]} was crossed off")
     print("number not in array")
     print("")


                 
             
             




