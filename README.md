# Fretboard App

A python app for the terminal to help drill notes given string and fret numbers.

It works like this:
- the app prompts for a string and a fret. For example "2nd string, 7th fret"
- you say the name of the note (and maybe play it too, but I avoid doing that because hearing the note can be a giveaway if you're good with pitch)

The app is written to guarantee that all selected strings and frets are prompted for. It calculates the cartesian product of the strings to frets, shuffles the relation, and then iterates through it.

It also uses randomises the voices so that it doesn't get _too_ repetitive. Voices have been selected for the clearest pronunciation, but you can edit the code to add any other voices you want.

The app continues infinitely until you hit `ctrl-c`, whereupon it prints the number of exercises completed.

The app is only intended to run on MacOS (using the `say` command).

## Usage

```
$ python fretboard.py -h
usage: fretboard.py [-h] [--min-fret MIN_FRET] [--max-fret MAX_FRET] [--min-string MIN_STRING]
                    [--max-string MAX_STRING] [--pause PAUSE]

Fretboard app

optional arguments:
  -h, --help            show this help message and exit
  --min-fret MIN_FRET   min fret number
  --max-fret MAX_FRET   max fret number
  --min-string MIN_STRING
                        min string number
  --max-string MAX_STRING
                        max string number
  --pause PAUSE         duration between prompts in seconds
```