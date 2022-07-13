from sys import argv
from random import shuffle
from subprocess import check_call
from time import sleep

PAUSE = 3
try:
    if argv[1] != "":
        PAUSE = int(argv[1])
except:
    pass

strings = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth"
}
string_options = list(strings.keys())
shuffle(string_options)

frets = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eigth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}
fret_options = list(frets.keys())
shuffle(fret_options)

voices = [
    "Alex",
    "Daniel",
    "Moira",
    "Samantha"
]

shuffle(voices)

voice_i = 0
string_i = 0
fret_i = 0

while True:
    # select random string
    string = strings[string_options[string_i]]

    # select random fret
    fret = frets[fret_options[fret_i]]

    # select random voice
    voice = voices[voice_i]

    # print prompt to console
    print("{} string, {} fret ({})".format(
        string_options[string_i],
        fret_options[fret_i],
        voice
    ))

    # say prompt
    check_call([
        "say",
        "-v",
        voice,
        "{} string, {} fret".format(string, fret)
    ])

    # pause
    sleep(PAUSE)

    # increment or reshuffle options
    if string_i == len(strings) - 1:
        string_i = 0
        shuffle(string_options)
    else:
        string_i += 1

    if fret_i == len(frets) - 1:
        fret_i = 0
        shuffle(fret_options)
    else:
        fret_i += 1

    if voice_i == len(voices) - 1:
        voice_i = 0
        shuffle(voices)
    else:
        voice_i += 1
