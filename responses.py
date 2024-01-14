import random

water_responses = ["thirst", "dry", "dehydrate", "dessicate", "water", "liquid"]

def get_response(message):
    scanned_chat = message.lower()

    for water_response in water_responses:
        if water_response in scanned_chat:
            return "Don't forget to drink water"
    

    ran_number = random.randint(1, 10)

    if ran_number > 8:
        return "Wow love this message!"
        
    else:
        return
