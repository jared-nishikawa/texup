#!/usr/bin/python

""" texup.py
This is a helper script designed to bootstrap creation
of latex templates.
Options will be:
    article
    beamer
    book
    exam
    letter (of recommendation)
    report (reports containing several chapters, small books, thesis...)
    syllabus
    screenplay
    ???
"""

import argparse
import os
import sys

def copy(path1, path2):
    with open(path1) as f:
        with open(path2, 'w') as g:
            g.write(f.read())

def makefile(name):
    with open('/usr/local/etc/skel/Makefile') as f:
        _raw = f.read()
        base = os.path.basename(name)
        raw = _raw.replace('XXXXXX', base)
        with open(name + "/Makefile", 'w') as g:
            g.write(raw)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name',
            help="name of the file to create")
    parser.add_argument('-t',
            '--type',
            help="type of tex template "\
                    "[empty, article, exam, letter,  syllabus, screenplay]",
            required=False,
            default="empty")
    args = parser.parse_args()

    NAME = args.name
    TYPE = args.type

    base = os.path.basename(NAME)

    if TYPE not in ['empty', 'article', 'exam', \
            'letter', 'syllabus', 'screenplay']:
        sys.stderr.write("TYPE must be one of [empty, article, exam, letter, syllabus, screenplay]" + '\n')
        sys.stderr.write("*** Texup failed.  Exiting...\n")
        sys.exit(4)


    #print "Name:", NAME
    #print "Type:", TYPE

    try:
        os.mkdir(NAME)
    except Exception, e:
        sys.stderr.write(e.__str__())
        sys.stderr.write("*** Texup failed.  Exiting...\n")
        sys.exit(1)


    try:
        copy('/usr/local/etc/skel/' + TYPE + '.tex', NAME + '/' + base + '.tex')
    except IOError, e:
        sys.stderr.write(e.__str__())
        sys.stderr.write("*** Texup failed.  Exiting...\n")
        sys.exit(2)

    try:
        makefile(NAME)
    except IOError, e:
        sys.stderr.write(e.__str__())
        sys.stderr.write("*** Texup failed.  Exiting...\n")
        sys.exit(3)

    print "Texup completed."
    print NAME + " has been successfully created."




