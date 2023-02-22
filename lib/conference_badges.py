def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    message = []
    for index in range(len(names)):
        message.append(f"Hello, {names[index]}! You'll be assigned to room {index+1}!")
    return message

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
