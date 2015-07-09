#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    if os.path.exists(dir):
        matches = []
        filenames = os.listdir(dir)
        for filename in filenames:
            match = re.search(r'.*__\w+__.*',filename)
            if match:
                matches.append(os.path.abspath(os.path.join(dir,match.group())))
        if not matches:
            print """There are no matches for "__w__" pattern"""
            return None
        else:
            return matches
    else:
        print "There is no such directory"
        return None


def copy_to(paths, todir):
    if not os.path.exists(todir):
        os.mkdir(todir)
    if paths is not None:
        for path in paths:
            try:
                print path, todir
                shutil.copy(path, todir)
            except:
                print "This files are already exist in this directory"


def zip_to(paths, zippath):
    if paths is not None:
        for path in paths:
            try:
                os.system('zip -j new ' + path)
            except:
                print "Could not create output file"
        shutil.copy(os.path.join(os.path.dirname(paths[0]), 'new.zip'), zippath)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  for arg in args:
    paths = get_special_paths(arg)
  if todir:
    copy_to(paths,todir)
  if tozip:
    zip_to(paths, tozip)
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
