import random

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
strings = [7, 2, 10, 5, 0, 7]

while True:
    string = random.randint(0, len(strings)-1)
    fret = random.randint(0, len(notes)-1)

    answer = input('%s %s: ' % (string+1, fret))

    if answer.upper() == notes[(strings[string] + fret) % len(notes)]:
        print('Correct')
    else:
        print('Wrong')
