try:
    numBooksPurchased = int(input("How many books have you purchased this month? "))
    if(numBooksPurchased < 1):
        pointsEarned = 0
    elif(numBooksPurchased <= 3):
        pointsEarned = 5
    elif(numBooksPurchased <= 5):
        pointsEarned = 15
    elif(numBooksPurchased <= 7):
        pointsEarned = 30
    elif(numBooksPurchased >= 8):
        pointsEarned = 60
    print(f'The number of points you earned this month are: {pointsEarned}')
except ValueError:
    print('please enter a correct value')