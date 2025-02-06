#TempConvert.py
#Name: Brennan Wood
#Date: 2/6/25
#Assignment: Lab 3 (TempConvert)


  #Defining the name of the program

def main():
  print("\033[34mTempConvert\033[0m")
if __name__ == '__main__':
    main()

  #Prompt the user for a Fahrenheit temperature

tempF = input("Input temperature in Fahrenheit: ")

  #Convert that temperature to Celsius, rounding to 1 decimal precision

floatF = float(tempF)
tempC = round(((5*(floatF-32))/9),1)
tempK = round((tempC+273.15),1)

  # Output converted temperature (Celsius and Kelvin).

print(tempF, "degrees Fahrenheit is ", tempC, "degrees Celsius.")
  
print(tempF, "degrees Fahrenheit is ", tempK, "degrees Kelvin.")