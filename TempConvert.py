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

tempF = input("Input temperature in Farenheit: ")

  #Convert that temperature to celsius, rounding to 1 decimal percision

floatF = float(tempF)
tempC = round(((5*(floatF-32))/9),1)
tempK = round((tempC+273.15),1)

  # Output converted temperature (Celsius and Kelvin).

print(tempF, "degrees Farenheit is ", tempC, "degrees Celsius.")
  
print(tempF, "degrees Farenheit is ", tempK, "degrees Kelvin.")