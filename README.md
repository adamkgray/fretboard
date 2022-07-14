# Fretboard App

A python app for the terminal to help drill notes on the first 12 frets of a guitar on all 6 strings.

It works like this:
- the app prompts for a string and a fret. For example "2nd string, 7th fret"
- you say the name of the note (and maybe play it too, but I avoid doing that because hearing the note can be a giveaway if you're good with pitch)

The app is written to guarantee that all 6 strings and all 12 frets are prompted for. There are 72 unique combinations of strings and frets ($6 \times 12$). So after 72 prompts you will have played every note. 

It also uses randomises the voices so that it doesn't get _too_ repetitive. Voices have been selected for the clearest pronunciation, but you can edit the code to add any other voices you want.

The app continues infinitely until you hit `ctrl-c`, whereupon it prints the number of exercises completed.

The app is only intended to run on MacOS (using the `say` command).

## Usage

```shell
$ python fretboard.py
```

## Config

```shell
# custom delay of 12s between prompts
$ python fretboard.py 12
```
