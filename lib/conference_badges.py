#Function to create a badge message
def badge_maker(name):
    return f"Hello, my name is {name}."

# Function to create a list of badge messages for a list of names
def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

# Function to assign rooms to a list of names
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i + 1}!" for i, name in enumerate(names)]

# Function to print the results of batch_badge_creator() and assign_rooms()
def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for room in rooms:
        print(room)