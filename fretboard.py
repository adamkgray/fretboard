from itertools import product
from sys import argv, exit
from random import shuffle
from subprocess import check_call
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Fretboard app')

parser.add_argument('--min-fret', type=int, help='min fret number')
parser.add_argument('--max-fret', type=int, help='max fret number')
parser.add_argument('--min-string', type=int, help='min string number')
parser.add_argument('--max-string', type=int, help='max string number')
parser.add_argument('--pause', type=int,
                    help='duration between prompts in seconds')

ordinals = {
    0: "zeroth",
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
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth",
    21: "twenty-first",
    22: "twenty-second",
    23: "twenty-third",
    24: "twenty-fourth"
}


voices = [
    "Alex",
    "Daniel",
    "Moira",
    "Samantha"
]


if __name__ == "__main__":

    args = parser.parse_args()

    min_fret = 1
    if args.min_fret is not None:
        min_fret = args.min_fret

    max_fret = 12
    if args.max_fret is not None:
        max_fret = args.max_fret

    min_string = 1
    if args.min_string is not None:
        min_string = args.min_string

    max_string = 6
    if args.max_string is not None:
        max_string = args.max_string

    pause = 3
    if args.pause is not None:
        pause = args.pause

    prompts = list(product(
        list(range(min_string, max_string + 1)),
        list(range(min_fret, max_fret + 1))
    ))

    shuffle(prompts)
    shuffle(voices)

    prompt_i = 0
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
            sleep(pause)

            # increment or reshuffle options
            if prompt_i == len(prompts) - 1:
                prompt_i = 0
                shuffle(prompts)
                print("--- all notes completed! ---")
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
