def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
        
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"The letter {letter} is a vowel.")
    elif letter !=['a', 'e', 'i', 'o', 'u']:
        print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid entry. Please enter a single alphabetical letter from a-z.")

check_letter()

def check_voting_eligibility():
    voting_age = 18
    
    try:
        age = int(input("Please enter your age: "))
        
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        elif age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not old enough to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_voting_eligibility()

def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        elif age <= 2:
            dog_years = age * 10
            print(f"The dog's age in dog years is {dog_years}.")
        else:
            dog_years = 20 + (age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

calculate_dog_years()

def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").lower()
    is_raining = input("Is it raining? (yes/no): ").lower()
    
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

weather_advice()

