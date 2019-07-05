#!/usr/bin/env python

# Convert an html script to markdown, a la:
# https://github.com/matthewwithanm/python-markdownify

from markdownify import markdownify as md
import sys
import os
import re

# Supporting Functions

def read_file(filename, mode='r'):
    '''read the content of a file into lines'''
    with open(filename, mode) as filey:
        content = filey.read()
    return content

def write_file(filename, content, mode='w'):
    '''read the content of a file into lines'''
    with open(filename, mode) as filey:
        filey.write(content)

# Converter

class MarkdownConverter:

    def __init__(self, source, dest):
        self.source = self._check_path(source)
        self.dest = dest

    def run(self):

        # If printing to terminal, might pipe to file, must be quiet
        if self.dest:
            print("Transforming html from '%s' to MarkDown syntax..." % self.source)

        html = read_file(self.source)
        markdown = md(html, heading_style="SETEXT")
        markdown = self.strip_lines(markdown)

        if self.dest:
            print("Writing output to %s" % self.dest)
            write_file(self.dest, markdown)
        else:
            print(markdown)

    def strip_lines(self, markdown):
        '''the library seems to leave extra spaces at the beginning of lines,
           and these should be stripped.
        '''
        lines = markdown.split('\n')
        lines = [l.strip() for l in lines]
        return '\n'.join(lines)

    def _check_path(self, path):
        path = os.path.abspath(path)
        if os.path.exists(path):
            return path
        else:
            raise ValueError("Cannot access file at '%s'" % path)
 
if __name__=="__main__":
    if len(sys.argv) == 1:
        print("Input file is required!")
        print("Usage: python convert.py input [output]")
        sys.exit(1)

    source = sys.argv[1]

    dest = None
    if len(sys.argv) > 2:
        dest = sys.argv[2]

    converter = MarkdownConverter(source, dest)
    converter.run()
