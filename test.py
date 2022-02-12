import random
data = []
def generate_data(a,b):
    global data
    for i in range(a,b):
        data.append(random.randint(a,b))
    return data