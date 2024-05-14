def mood_calculator():
    print("Welcome to the Mood Calculator!")
    print("Please answer the following questions to determine your mood.")

    # Ask questions to evaluate mood
    question_1 = input("On a scale of 1 to 10, how would you rate your energy level? ")
    question_2 = input("How would you describe your overall happiness? (e.g., very happy, neutral, sad) ")
    question_3 = input("Are you feeling motivated today? (yes/no) ")
    
    # Convert answers to numerical values
    energy_level = int(question_1)
    happiness = question_2.lower()
    motivation = question_3.lower()
    
    # Evaluate mood based on answers
    if energy_level >= 8 and happiness == "very happy" and motivation == "yes":
        mood = "Fantastic"
    elif energy_level >= 6 and happiness in ["happy", "neutral"] and motivation == "yes":
        mood = "Good"
    elif energy_level < 3 and happiness == "sad" and motivation == "no":
        mood = "Terrible"
    else:
        mood = "Okay"
    
    print(f"\nBased on your answers, your mood is: {mood}")
    
mood_calculator()