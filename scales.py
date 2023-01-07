import random

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scales = ['Minor Pentatonic', 'Major Pentatonic', 'Major', 'Natural Minor']

key = random.choice(keys)
scale = random.choice(scales)

print(key, scale, random.randint(1,5))
