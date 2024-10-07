
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    if number < cutoff:
        print(str(number) + " is less than " + str(cutoff))
        return True
    else:
        print(str(number) + " is not less than " + str(cutoff))
        return False
        

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    if type(decimal_number) != float:
        return "invalid"
    if decimal_number == 0:
        return "zero"
    elif decimal_number > 0:
        return "positive"
    elif decimal_number < 0:
        return "negative"


def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    if type(year) != int:
        return "invalid"
    if year >= 2001 and year <= 2100:
        return "21st century"
    elif year >= 1901 and year <= 2000:
        return "20th century"
    elif year >= 1801 and year <= 1900:
        return "19th century"
    elif year < 1801:
        return "ancient"

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    Nums = [number_1, number_2, number_3]
    for x in Nums:
        if type(x) != float and type(x) != int:
            return "None"
    return max(Nums)
    
def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature - 
    # Return "Solid" if water is in solid state at that temperature - 0
    # Return "Gas" if water is in gas state at that temperature - 100
    # Return "Invalid" if the temperature or scale are invalid
    if type(temperature) != int:
        return "invalid"
    if scaled_used == 'F':
        convertF = (temperature * 9/5) + 32
        if convertF > 0 and convertF < 100:
            return "Liquid"
        elif convertF <= 0:
            return "Solid"
        elif convertF >= 100:
            return "Gas"
        

    

