# MediaWiki to Markdown

This is a simple script to convert from MediaWiki files to markdown.
An example [index.rst](index.rst) is provided, along with the [index.md](index.md)
it converts to. 

## Usage

The script will print the resulting markdown to the screen:

```bash
$ python mw2md.py index.rst
```

And then here is an example piping this output to file:

```bash
$ python mw2md.py index.rst > index.md
```

or you can provide the file path to write it directly:

```bash
$ python mw2md.py index.rst index.md
Transforming MediWiki from '/home/vanessa/Documents/Dropbox/Code/srcc/mw2md.py/index.rst' to MarkDown syntax...
Writing output to index.md
```

