![GitHub](https://img.shields.io/github/license/veerendra2/funmotd.svg?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/veerendra2/funmotd.svg?style=for-the-badge)
![PyPI - Status](https://img.shields.io/pypi/status/funmotd.svg?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/funmotd.svg?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/funmotd.svg?style=for-the-badge)
# Funny motd (funmotd)
A cool tool to display random quotes from Movies and TV Shows as [`motd`](https://en.wikipedia.org/wiki/Motd_(Unix)) on Terminal when you open.

![Example](https://raw.githubusercontent.com/veerendra2/funmotd/master/example.gif)

## Installation
#### Using `pip3`
```
$ pip3 install funmotd
```
#### From source
```
$ git clond https://github.com/veerendra2/funmotd.git
$ cd funmotd
$ python3 setup.py install
```
**NOTE:** This package requires `python3` and `pip3` to install it. Install `pip3`: `sudo apt install python3-pip -y`

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
  -v                Version and author information
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
#### Modify Weights
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