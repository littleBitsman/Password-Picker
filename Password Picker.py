import random
import string

adjectives = ['sleepy','slow','fluffy','wet','fat','Sleepy','Slow','Fluffy','Wet','Fat']
nouns = ['apple','dinosaurs','pizza','plane','shirt','plane','fairy','otter','dinosaur','apples','ball','balls','goat','goats','dragon','dragons','hammer','hammers','duck','ducks','panda','pandas','Apple','Dinosaurs','Pizza','Plane','Shirt','Planes','Fairy','Otter','Dinosaur','Apples','Ball','Balls','Goat','Goats','Dragon','Dragons','Hammer','Hammers','Duck','Ducks','Panda','Pandas']
colors = ['Red','Orange','Yellow','Green','Blue','Purple','Black','red','orange','yellow','green','blue','purple','black']
print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    color = random.choice(colors)
    special_char = random.choice(string.punctuation)
    password = adjective + color + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like another password? Type yes or no: ')
    if response == 'no':
        break