print('''Enter the singular name of a non carnivorous land animal
for example Pig, Cow, Sheep.''')
prey = input().capitalize()
print (f'{prey}, okay.')

print()

print('''Enter the singular name of a carnivorous land animal
for example Wolf, Lion, Hyena.''')
predator = input().capitalize()
print (f'{predator}, okay.')

print()

print('''Enter the name of a building material that will not break easily
for example brick, wood, metal.''')
material = input()
print (f'{material}, okay.')

print()

print('''Enter a number in between 5 and 60. Not in words  
for example 10, 20, 40. ''')
count = input()
print(f'{count}, great.')

print()

print('Enter a girls name')
name = input().capitalize()
print(f'{name}, nice name.')

print(f'''
Once upon a time there were three little {prey}'s and the time came for them 
to leave home and seek their fortunes. Before they left, their sister {name}
told them " Whatever you do , do it the best that you can because that's the
way to get along in the world.

The first little {prey} built his house out of straw because it was the 
easiest thing to do. The second little {prey} built his house out of sticks.
This was a little bit stronger than a straw house. The third little {prey}
built his house out of {material}.

One night the big bad {predator} who dearly loved to eat fat little {prey}'s,
came along and saw the first little {prey} in his house of straw. He said 
"Let me in,Let me in, little {prey} or I'll huff and I'll puff and I'll blow
your house in!" "Not by the hair of my chinny chin chin", said the little 
{prey}. But of course the {predator} did blow the house in and ate the 
first little {prey}.

The {predator} then came to the house of sticks. "Let me in ,Let me in little
{prey} or I'll huff and I'll puff and I'll blow your house in" "Not by the 
hair of my chinny chin chin", said the little {prey}. But the {predator} blew
that house in too, and ate the second little {prey}.

The {predator} then came to the house of {material}. "I will give you {count}
seconds to let me in "cried the {predator} "Or I'll huff and I'll puff till 
I blow your house in" "Not by the hair of my chinny chin chin" said the 
{prey}. Well, the {predator} huffed and puffed but he could not blow down that
{material} house.

But the {predator} was a sly old {predator} and he climbed up on the roof to
look for a way into the {material} house.

The little {prey} saw the {predator} climb up on the roof and lit a roaring 
fire in the fireplace and placed on it a large kettle of water.

When the {predator} finally found the hole in the chimney he crawled down and 
KERSPLASH right into that kettle of water and that was the end of his 
troubles with the big bad {predator}.

The next day the little {prey} invited his sister {name} over . She said "You
see it is just as I told you. The way to get along in the world is to do 
things as well as you can." Fortunately for that little {prey}, he learned 
that lesson. And he just lived happily ever after!
''')
