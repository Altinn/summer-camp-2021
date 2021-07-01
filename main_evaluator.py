
def getHouseholdIncome(user):
        
    userIncome = getUserIncome(user)
    tempHouseholdIncome = userIncome

    householdUsers = findHousehold(user)
        
    for householdUser in householdUsers:
        tempHouseholdIncome += getUserIncome(householdUser)
    
    return tempHouseholdIncome

def getUserIncome(user):
    # Get user Income from external data source (The Norwegian Tax Administration)
    return 500000

def findHousehold(user):
    # Get users of user household from external data source (National Population Register)
    otherUser = 1
    differentUser = 2
    return [otherUser, differentUser]

def getIncomeCap():
    # Get income cap from external data source (Law data source)
    return 583650

def getMaxPercentageToPay(municipality):
    # Get percentage from external data source (Law data source)
    # Might also be lower based on municpality
    return 0.06

def getRequiredPayment(municipality):
    # Get required pay from external data source (Varies based on municipality)
    return 3000


    
def evaluateReducedPay(user):
    householdIncome = getHouseholdIncome(user)
    maxPay = getMaxPercentageToPay() * householdIncome
    requiredPay = getRequiredPayment()
    if maxPay > requiredPay:
        return maxPay
    return requiredPay
     

def evaluateFreeHours(user):
    householdIncome = getHouseholdIncome(user)
    requriment = getIncomeCap()
    if (householdIncome < requriment):
        return True
    return False