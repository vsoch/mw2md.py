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

# Html to Markdown

I needed a quick script to convert from HTML to Markdown, so I bootstrapped
[python-markdownify](https://github.com/matthewwithanm/python-markdownify) to
handle most of the work. The usage is the same as above, but providing html files
as input, and then also writing markdown. You also need to install
markdownify:

```bash
$ pip install -r requirements.txt
```

And then convert!

```bash
$ python html2md.py index.html
```
