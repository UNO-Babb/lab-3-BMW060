#ApproxPi.py
#Name:Brennan Wood 
#Date: 2/6/25
#Assignment: Lab 3 (ApproxPi)
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)

  precision = input("Please enter the number of digits you would like to calculate pi to: ")
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, int(precision)) != round(realPi, int(precision)):
    print(approxPi)
    approxPi = approxPi + (sign * 4/denom)
    sign = sign * -1
    denom = denom + 2
    
        

  end = time.time()

  elapsedTime = end - start
  print("The time it took to reach this conclusion was: " + str(round(elapsedTime, 5)) + " seconds")

if __name__ == '__main__':
  main()
