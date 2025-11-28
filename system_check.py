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
    ticket_string = ticket_string.strip().split("-")
    code = ticket_string[2]
    return code

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
    if ticket_string.startswith("EC"):
        return "Economy - 20kg"
    elif ticket_string.startswith("BS"):
        return "Business - 40kg"
    elif ticket_string.startswith("FL"):
        return "First Class - 60kg"
    else:
        return "Standard - 0kg"

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
    ticket_string = ticket_string.strip().split("-")
    flight_info = ticket_string[1]
    checker = int(flight_info[-1])

    if checker % 2 == 0:
        return "Valid - Northbound"
    if checker % 2 != 0:
        return "Valid - Southbound"
    else:
        return "Invalid flight"        #probably had to use exceptions somewhere here



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
        if year % 100 == 0:
            if year % 4 == 0:
                return True
            return False



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
    if temp < 500:
        return "Maintenance Mode"
    elif temp < 0 or radiation < 0:
        return "Sensor Error"
    elif temp > 2000 or radiation > 500:
        return "CRITICAL"
    elif 1000 < temp < 2000 and radiation > 100:
        return "WARNING"
    else:
        return "Normal Mode"
    
    
    
