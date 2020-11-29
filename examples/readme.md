# example vimrc configuration and wiki structure

These files illustrate more of the practical side of how and why I designed the
code the way I did. Ultimately I want to be able to run one script and
automatically generate HTML files for my wiki. Getting this working requires a
great deal of setup on the Vim side.

You can see this in the `.vimrc` present in this directory. It is a subset of
my current `.vimrc` configuration file containing only the bits most-relevant
to how I use my Vimwiki. The file is full of quick tips I learned from
searching online, reading the documenation, and experimenting on my own that
might be useful to others.

## takeaways from `.vimrc`

1. I use Vim-Plug to handle Vim plugins
2. I have installed Vimwiki and Vim-Zettel. One of them requires FZF.
3. I have 5 heavily customized wikis. Normally you might only want one or two
   wikis, but separating them in this way makes it much easier to compile using
   into separate HTML templates. For example, recipes will probably require
   different metadata then writings posts. Structuring my wikis this way also
   allows me to maintain a private wiki (which is never compiled into HTML) and
   public wikis.
4. I use a vanilla Vim key-value pair datastructure to make it a little more
   readable when stuffing all this information into `g:vimwiki_list`
5. Each wiki uses markdown syntax and compiles using the custom script
   `utils/convert.py`.
6. I have included a couple functions. One is a custom `VimwikiLinkHandler` to
   open `vfile:<LINK>` paths in a new tab. Also, I kept in the
   StartSecretFile() function. Sometimes I keep confidential records in my
   private Vimwiki using YAML format.


### takeaways from `example_wiki/`

This is the way I structure each wiki on my machine. Each wiki is in its own
folder, and each folder contains a subfolder called `templates` which stores
the pandoc templates required to compile to the desired Jinja2 templates input
into Flask.

1. Because each file will be converted using Pandoc, pages can be typed up with
   a more extensive syntax than Vimwiki or vanilla markdown. For example, each
   post example in this folder features a YAML block at the top of the file for
   passing custom metadata into the templates.
2. The `templates` folder houses two templates: one to compile each post into a
   Jinja2 HTML template, and another to only catch metadata in the form of a
   JSON. These are both Pandoc templates and are found by `utils/convert.py` when
   each post is compiled from markdown into Jinja2 HTML templates. This is
   really just a lazy way of building a NoSQL database of all metadata. At
   present posts are just served basically like static webpages, but eventually
   I want to include fancy visuals for tags, keywords, recipe ingredients, etc.
3. Handling images is always one of the hardest things about maintaining an
   elaborate wiki setup. In this case I put a `static/assets` folder in my root
   `~/vimwiki` folder which corresponds to a folder with the same name on the
   website.


