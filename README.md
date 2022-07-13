# Fretboard App

A python app for the terminal to help drill notes on the first 12 frets of a guitar on all 6 strings.

The app is written to guarantee that all 6 strings and all 12 frets are prompted for at least once per cycle. That is to say, in 6 prompts you will have to play all 6 strings, and in 12 prompts you will have to use all 12 frets. It also uses randomises the voices so that it doesn't get _too_ repetitive.

## Usage

```shell
$ python fretboard.py

# custom delay of 12s between prompts
$ python fretboard.py 12
```

## Config

The app is only intended to run only on MacOS (it uses the `say` command).

Voices have been selected for the clearest pronunciation, but you can edit the code to add any other voices you want.