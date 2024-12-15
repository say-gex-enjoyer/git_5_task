import random

percent_chance_Total = 0
percent_chance_Correct = 0
for i in range(10000000):
    random_Number = random.randint(1,100)
    #print(random_Number)
    if (random_Number >= 59):
        percent_chance_Correct+=1
    percent_chance_Total+=1

        

print(percent_chance_Correct / percent_chance_Total)
        
