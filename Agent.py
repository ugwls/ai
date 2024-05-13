import random

def initialize_environment():
    location_condition = {'A': '0', 'B': '0'}
    location_condition['A'] = random.randint(0, 1)
    location_condition['B'] = random.randint(0, 1)
    return location_condition

def simple_reflex_vacuum_agent(environment):
    score = 0
    vacuum_location = random.randint(0, 1)
    
    if vacuum_location == 0:
        print("Vacuum is randomly placed at Location A.")
        if environment['A']==1:
            print("A is dirty")
            
        else:
            print("Location A is Clean.")
        if environment['A'] == 1:
            environment['A'] = 0
            score += 1
            print("Location A has been Cleaned.") 
        print("Moving to Location B...")
        print("Location B is Dirty.") if environment['B'] == 1 else print("Location B is Clean.")
        if environment['B'] == 1:
            environment['B'] = 0
            score += 1
            print("Location B has been Cleaned.")
        print("Environment is Clean.")
        
    elif vacuum_location == 1:
        print("Vacuum randomly placed at Location B.")
        print("Location B is Dirty.") if environment['B'] == 1 else print("Location B is Clean.")
        if environment['B'] == 1:
            environment['B'] = 0
            score += 1
            print("Location B has been Cleaned.")
        print("Moving to Location A...")
        print("Location A is Dirty.") if environment['A'] == 1 else print("Location A is Clean.")
        if environment['A'] == 1:
            environment['A'] = 0
            score += 1
            print("Location A has been Cleaned.")
        print("Environment is Clean.")    
    
    print(environment)
    print("Performance Measurement: " + str(score))

the_environment = initialize_environment()
simple_reflex_vacuum_agent(the_environment)
