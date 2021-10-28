![GitHub](https://img.shields.io/github/license/veerendra2/funmotd.svg)
![GitHub stars](https://img.shields.io/github/stars/veerendra2/funmotd.svg)
![PyPI - Status](https://img.shields.io/pypi/status/funmotd.svg)
![PyPI](https://img.shields.io/pypi/v/funmotd)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/funmotd.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/funmotd)
[![Release](https://github.com/veerendra2/funmotd/actions/workflows/releases.yml/badge.svg)](https://github.com/veerendra2/funmotd/actions/workflows/releases.yml)
# Funny motd (funmotd)
A cool tool to display random quotes from Movies and TV Shows as [`motd`](https://en.wikipedia.org/wiki/Motd_(Unix)) on Terminal when you open.

![Example](https://user-images.githubusercontent.com/8393701/139233945-d44c1465-97fd-45ed-89f3-84ce19bcfeff.gif)

## Installation
```
$ pip3 install funmotd
```

## How it works?
The [`__init__.py`](https://github.com/veerendra2/funmotd/blob/master/funmotd/__init__.py) first picks a random `TV Shows/Movies` with [`weights`](https://docs.python.org/3/library/random.html#random.choices) and again picks a quote randomly from selected `TV Show/Moves`. You can see available  of quotes in [`quotes_db.py`](https://github.com/veerendra2/funmotd/blob/master/funmotd/quotes_db.py)

When you install package, the CLI will add entry in `.bashrc`, it will execute whenever `bash` is loaded

## Usage
```
$ funmotd --help
usage: funmotd [-h] [-l] [-e MODIFY MODIFY] [-n NSFW] [-v]

Displays TV Show and Movie Quotes as 'motd' on Terminal

optional arguments:
  -h, --help        show this help message and exit
  -l                View Available TV Show/Movies & Configuration
  -e MODIFY MODIFY  Modify Weights
  -n NSFW           Enable/Disable NSFW Quotes
  -v                show program's version number and exit
```  

## How to Configure?
#### List Available TV Show/Movies
```
$ funmotd -l
         ** Configuration **
+------------------------+-------------+
| TV Shows/Movies Quotes | Weights     |
+------------------------+-------------+
| breaking_bad           | 60          |
| friends                | 10          |
| game_of_thrones        | 100         |
| jokes                  | 0           |
| movies                 | 10          |
+------------------------+-------------+
|  NSFW                  | True        |
+------------------------+-------------+
```
#### Modify Weights
You can modify weights to see which `TV Shows/Movies` mostly
```
$ funmotd -e game_of_thrones 90
[*] Configuration Modified

$ funmotd -l
         ** Configuration **
+------------------------+-------------+
| TV Shows/Movies Quotes | Weights     |
+------------------------+-------------+
| breaking_bad           | 60          |
| friends                | 10          |
| game_of_thrones        | 90          |
| jokes                  | 0           |
| movies                 | 10          |
+------------------------+-------------+
|  NSFW                  | True        |
+------------------------+-------------+
```
#### Enable/Disable `NSFW` Quotes
There are some quotes "NSFW", so this option helps to enable/disable.
```
$ funmotd -n no
[*] Configuration Modified
$ funmotd -l
         ** Configuration **
+------------------------+-------------+
| TV Shows/Movies Quotes | Weights     |
+------------------------+-------------+
| breaking_bad           | 60          |
| friends                | 10          |
| game_of_thrones        | 90          |
| jokes                  | 0           |
| movies                 | 10          |
+------------------------+-------------+
|  NSFW                  | False       |
+------------------------+-------------+
``` 
## Can I add any other quotes?
Yes, but not with CLI (may be in future versions). Right now, you have to edit `quotes_db.py` and run `funmotd -l` to update the configuration.

The [`quotes_db.py`](https://github.com/veerendra2/funmotd/blob/master/funmotd/quotes_db.py) follow below dictionary structure.
```
all_quotes = {
  '<tv_show_movie_name>' : [
        [ # NSFW Quote's list
            {'quote': '<whatever the NSFW quote it is>', 'character': '<name of the character>', 'name': '<name of the TV Show/ Movie>'}
        ],
        [ # NON-NSFW Quote's list
            {'quote': '<whatever the NORMAL quote it is>', 'character': '<name of the character>', 'name': '<name of the TV Show/ Movie>'}
        ]
    ]
}

```

## Uninstall
```
$ pip3 uninstall funmotd
```
And remove CLI entry in `.bashrc`
