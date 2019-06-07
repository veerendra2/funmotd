#!/usr/bin/python3
"""
Displays TV Show and Movie Quotes as 'motd' on Terminal
"""
import random
import argparse
import json
import textwrap
import os

from .quotes_db import all_quotes

__author__ = "Veerendra Kakumanu (veerendra2)"
__license__ = "Apache 2.0"
__version__ = "0.3"
__maintainer__ = "Veerendra Kakumanu"


config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')


def banner():
    print("+----------------------------------------------+")
    print("|Funny MOTD (funmotd) v0.3                     |")
    print("|Author: Veerendra Kakumanu (veerendra2)       |")
    print("|Blog: https://veerendra2.github.io            |")
    print("|Repo: https://github.com/veerendra2/funmotd   |")
    print("+----------------------------------------------+\n")


def read_config():
    with open(config_file) as f:
        config = json.load(f)
    return config


def write_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, sort_keys=True, indent=4)


def display_config():
    config = read_config()
    diff = set(all_quotes) - set(config["quotes"])
    if diff:
        for i in diff:
            config["quotes"][i] = 0
            write_config(config)
    print("** Configuration **".rjust(28, " "))
    print("+".ljust(25, "-") + "+".ljust(14, "-") + "+")
    print("| TV Shows/Movies Quotes".ljust(25, " ") + "| Weights".ljust(13, " ") + " |")
    print("+".ljust(25, "-") + "+".ljust(14, "-") + "+")
    for name, prob in config["quotes"].items():
        print("| " + name.ljust(22, " ")+" | "+str(prob).ljust(11)+" |")
    print("+".ljust(25, "-") + "+".ljust(14, "-") + "+")
    print("|  NSFW".ljust(24, " ") + " | " + str(config["nsfw"]).ljust(11) + " |")
    print("+".ljust(25, "-") + "+".ljust(14, "-") + "+")


def modify_config(nsfw, prob):
    config = read_config()
    if nsfw is None and prob:
        if prob[0] in config["quotes"]:
            config["quotes"][prob[0]] = int(prob[1])
        else:
            print("[-] {} not found in configuration".format(prob[0]))
            exit(1)
    else:
        config["nsfw"] = nsfw
    write_config(config)
    print("[*] Configuration Modified")


def show_motd():
    config = read_config()
    quotes_list = list()
    prob = list()
    for key, value in config["quotes"].items():
        quotes_list.append(key)
        prob.append(value)
    name = random.choices(quotes_list, prob, k=1)[0]
    if config["nsfw"]:
        quote = random.choice(all_quotes[name][0] + all_quotes[name][1])
    else:
        quote = random.choice(all_quotes[name][1])
    print("### Quote of the Day ###\n")
    print(textwrap.fill('"'+quote["quote"]+'"', 90))
    print("   ~{} ({})\n".format(quote["character"], quote["name"]))


def main():
    arg = argparse.ArgumentParser(description="Displays TV Show and Movie Quotes as 'motd' on Terminal")
    arg.add_argument("-l", action="store_true", dest="view", default=False, help="View Available TV Show/Movies & \
        Configuration")
    arg.add_argument("-e", action="store", dest="modify", default=False, nargs=2, help="Modify Weights")
    arg.add_argument("-n", action="store", dest="nsfw", default=False, help="Enable/Disable NSFW Quotes")
    arg.add_argument('-v', action='store_true', dest="version_info",  default=False, help="Version and author \
        information")
    results = arg.parse_args()
    if results.version_info:
        banner()
    elif results.view:
        display_config()
    elif results.modify:
        if not results.modify[1].isdigit():
            print("[-] Weight should be integer")
            exit(1)
        modify_config(None, results.modify)
    elif results.nsfw:
        if results.nsfw.lower() in ('yes', 'true', 't', 'y', '1'):
            modify_config(True, None)
        elif results.nsfw.lower() in ('no', 'false', 'f', 'n', '0'):
            modify_config(False, None)
        else:
            print("[-] Invalid Arguments")
    else:
        show_motd()


if __name__ == '__main__':
    main()
