import random

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
chords = ['I', 'IV', 'V']
minor_chords = ['ii', 'iii', 'vi']

key = random.choice(keys)
select_chords = ['I']

for x in range(2):
    select_chords.append(random.choice(chords + minor_chords))

select_chords.append(random.choice(chords))

print('Key: ', key)

print('Chords:', select_chords)

print('# Strums: ', random.randint(4, 8))

print('Tempo', random.randint(70, 160))
