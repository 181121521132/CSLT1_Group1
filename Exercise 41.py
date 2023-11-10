x= input()

c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88
frequency = 0

if note[0] == 'C':
    frequency = c4 / 2**(4 - int(x[1]))
elif note[0] == 'D':
    frequency = d4 / 2**(4 - int(xx[1]))
elif note[0] == 'E':
    frequency = e4 / 2**(4 - int(note[1]))
elif note[0] == 'F':
    frequency == f4 / 2**(4 - int(note[1]))
elif note[0] == 'G':
    frequency = g4 / 2**(4 - int(note[1]))
elif note[0] == 'A':
    frequency = a4 / 2**(4 - int(note[1]))
elif note[0] == 'B':
    frequency = b4 / 2**(4 - int(note[1]))

print(frequency)