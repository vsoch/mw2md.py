#!/usr/bin/env python

import sys
import os
import re

# Supporting Functions

def read_file(filename, mode='r'):
    '''read the content of a file into lines'''
    with open(filename, mode) as filey:
        content = filey.readlines()
    return content

def write_file(filename, content, mode='w'):
    '''read the content of a file into lines'''
    with open(filename, mode) as filey:
        filey.write(content)

def apply_lines(func, content):
    def wrapper():
        lines = []
        for line in content:
            line = func(line)
            lines.append(line)
        return lines
    return wrapper

# Converter

class MarkdownConverter:

    def __init__(self, source, dest):
        self.source = self._check_path(source)
        self.dest = dest

    def run(self):

        # If printing to terminal, might pipe to file, must be quiet
        if self.dest:
            print("Transforming MediWiki from '%s' to MarkDown syntax..." % self.source)

        lines = read_file(self.source)
        lines = apply_lines(self._convert_headers, lines)()
        lines = apply_lines(self._convert_emphasis, lines)()
        lines = apply_lines(self._convert_links, lines)()
        lines = apply_lines(self._convert_codeblocks, lines)()
        lines = apply_lines(self._convert_lists, lines)()

        if self.dest:
            print("Writing output to %s" % self.dest)
            write_file(self.dest, ''.join(lines))
        else:
            print(''.join(lines))

    def _convert_lists(self, line):
        '''handle bullets in lists.
        '''
        if line.startswith('::-'):
            line = line.replace('::-', '  -', 1)
        return line

    def _convert_links(self, line):
        '''convert a media wiki link to a standard markdown one.

           [https://slurm.schedmd.com/pdfs/summary.pdf Slurm commands]
           to
           [Slurm Commands](https://slurm.schedmd.com/pdfs/summary.pdf)
        '''
        # Internal Links convert to markdown
        for match in re.findall("\[\[(.+\|.+)\]\]", line):
            title, markdown = match.split('|')
            markdown = "[%s](%s.md)" %(title.strip(), 
                                       markdown.lower().strip().replace(' ', '-'))
            line = line.replace("[[%s]]" % match, markdown)
             
        markup_regex = '\[(http[s]?://.+?)\]'

        # First address external links
        for match in re.findall(markup_regex, line):
            url, text = match.split(" ", 1)
            markdown = "[%s](%s)" %(text.strip(), url.strip())
            line = line.replace("[%s]" % match, markdown)
        return line
         

    def _convert_headers(self, line):
        '''convert headers to markdown, e.g
           == Cluster description == --> ## Cluster Description
           This function should be handled by the apply_lines wrapper.
        '''
        if line.startswith('='):
            header = line.split(" ")[0]
            line = line.rstrip().rstrip(header).strip()
            line = line.replace('=', "#", len(header))
        return line


    def _convert_codeblocks(self, line):
        '''convert source blocks (<source lang="sh">) to ```
        '''
        code = "```"
        if line.startswith("<source"):
             lang = (line.replace("<source lang=", "").replace(
                     ">", "").replace("'","").replace('"','').strip())
             if lang:
                 code = "%s%s\n" %(code, lang)
             line = code
        line = line.replace("</source>", "```")
        return line


    def _convert_emphasis(self, line):
        '''convert in text code (e.g. ''only'') to markdown for bold
           or italic.
        '''
        groups = [("''", "''", "*"),         # bold
                  ("<code>", "</code>", "`") # code blocks
                 ]
        for group in groups:
            left, right, new = group
            for match in re.findall("%s.+%s" %(left, right), line):
                inner = match.replace(left, new).replace(right, new)
                line = line.replace(match, inner)
        return line


    def _check_path(self, path):
        path = os.path.abspath(path)
        if os.path.exists(path):
            return path
        else:
            raise ValueError("Cannot access file at '%s'" % path)
 
if __name__=="__main__":
    if len(sys.argv) == 1:
        print("Input file is required!\n")
        print("Usage: python rst2md.py input [output]")
        sys.exit(1)

    source = sys.argv[1]

    dest = None
    quiet = True
    if len(sys.argv) > 2:
        dest = sys.argv[2]
        quiet = False

    converter = MarkdownConverter(source, dest, quiet)
    converter.run()
