# ==========================================
# SECTION A: DATA PARSING (FLIGHT TICKET SYSTEM)
# ==========================================

def get_departure_airport(ticket_string: str):
    """
    QUESTION 1
    ----------------------------------------
    Extract the Departure Airport Code from the ticket string.
    
    Format of ticket_string: "FL-JO234-JNB-CPT-2023"
    
    Logic:
    - The code is situated between the second and third hyphen (-).
    - In the example "FL-JO234-JNB-CPT-2023", the departure is "JNB".
    
    Harder Twist: You cannot use fixed indices (e.g., [10:13]) because the 
    Flight Number (JO234) can vary in length. You must find it relative to the hyphens.
    """
    # TODO: Write your code here
    new_string = ticket_string.split("-")
    depature_airport_code = new_string[2]
    return depature_airport_code
print(get_departure_airport("FL-JO234-JNB-CPT-2023"))
   
   

def check_baggage_allowance(ticket_string: str):
    """
    QUESTION 2
    ----------------------------------------
    Determine the baggage allowance based on the Flight Class.
    
    Format: The first two letters of the string indicate the class.
    Example: "FL-..." starts with "FL".
    
    Logic:
    - If starts with 'EC': return "Economy - 20kg"
    - If starts with 'BS': return "Business - 40kg"
    - If starts with 'FL': return "First Class - 60kg"
    - For any other code: return "Standard - 0kg"
    """
    # TODO: Write your code here
    new_string = ticket_string.split("-")
    baggage_allowance = new_string[0]
    if baggage_allowance == 'EC':
        return "Economy - 20kg"
    if baggage_allowance == 'BS':
        return "Business - 40kg"
    if baggage_allowance == 'FL':
        return "First Class - 60kg"
    else:
        return "Standard - 0kg"
print(check_baggage_allowance("FL-JO234-JNB-CPT-2023"))

def validate_flight_number(ticket_string: str):
    """
    QUESTION 3
    ----------------------------------------
    Extract the Flight Number (the part between 1st and 2nd hyphen, e.g., "JO234").
    
    Logic:
    - If the number portion (e.g., 234) is Even, return "Valid - Northbound"
    - If the number portion is Odd, return "Valid - Southbound"
    - If the numeric part cannot be converted to a number, return "Invalid Flight"
    """
    # TODO: Write your code here
    new_string = ticket_string.split("-")
    flight_number = new_string[1]
    # I finally figured it out! is.digit() is a str method, and I was using it after I had converted number_portion into an int. Brain cells restored! 
    number_portion = str(flight_number.replace("JO", "").replace("A", ""))
    if not number_portion.isdigit():
        return "Invalid Flight"
    
    number_portion = int(number_portion)

    if number_portion % 2 == 0:
        return "Valid - Northbound"
    if number_portion % 2 != 0:
        return "Valid - Southbound" 
print(validate_flight_number("FL-JOABC-JNB-CPT-2023"))



# ==========================================
# SECTION B: ALGORITHMIC LOGIC (MATH)
# ==========================================

def is_leap_year(year: int):
    """
    QUESTION 4
    ----------------------------------------
    Determine if a given year is a Leap Year.
    This replaces FizzBuzz with harder Modulo logic.
    
    Rules:
    1. If the year is evenly divisible by 4, go to step 2. Otherwise, False.
    2. If the year is evenly divisible by 100, go to step 3. Otherwise, True.
    3. If the year is evenly divisible by 400, True. Otherwise, False.
    
    Return True or False (Boolean).
    """
    # TODO: Write your code here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(1900))


# ==========================================
# SECTION C: COMPLEX LOGIC & TDD
# ==========================================

def reactor_status(temp: int, radiation: int):
    """
    QUESTION 5 (THE LOGIC MONITOR)
    ----------------------------------------
    Analyze a nuclear reactor's status based on Temperature (C) and Radiation (Sv).
    
    TODO: Using TDD, implement tests for the below functionality.
    Create `test_reactor.py` with class `TestReactor`.
    
    Logic Tree:
    1. NEGATIVE CHECKS (Invalid Sensors):
       - If temp OR radiation is less than 0: return "Sensor Error"
       
    2. CRITICAL (Meltdown imminent):
       - If temp > 2000 OR radiation > 500: return "CRITICAL"
       
    3. WARNING (Unstable):
       - If temp is between 1000 and 2000 (inclusive) AND radiation > 100: return "WARNING"
       
    4. MAINTENANCE (Low output):
       - If temp < 500: return "Maintenance Mode"
       
    5. NORMAL:
       - For all other cases: return "Normal Operation"
    """
    # TODO: Write your code here
    if temp in range(1000, 2001) and radiation > 100:
        return "WARNING"
    if temp < 0 or radiation < 0:
        return "Sensor Error"
    if temp > 2000 or radiation > 500:
        return "CRITICAL"
    if temp < 500:
        return "Maintenance Mode"
    else:
        return "Normal Operation"
print(reactor_status(1500, 200))
