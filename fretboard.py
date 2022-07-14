from itertools import product
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

ordinals = {
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

prompts = list(product(
    list(range(1, 7)),
    list(range(1, 13))
))
shuffle(prompts)
prompt_i = 0

voices = [
    "Alex",
    "Daniel",
    "Moira",
    "Samantha"
]
shuffle(voices)
voice_i = 0

completed = 0

try:
    while True:
        # select random string and fret
        string_n, fret_n = prompts[prompt_i]
        string = ordinals[string_n]
        fret = ordinals[fret_n]

        # select random voice
        voice = voices[voice_i]

        # print prompt to console
        print("{} string, {} fret".format(string_n, fret_n))

        # say prompt
        check_call([
            "say",
            "-v", voice,
            "{} string, {} fret".format(string, fret)
        ])

        completed += 1

        # pause
        sleep(PAUSE)

        # increment or reshuffle options
        if prompt_i == len(prompts) - 1:
            prompt_i = 0
            shuffle(prompts)
        else:
            prompt_i += 1

        if voice_i == len(voices) - 1:
            voice_i = 0
            shuffle(voices)
        else:
            voice_i += 1

except KeyboardInterrupt:
    print("\ncompleted {}!".format(completed))
    print("\r  ")
