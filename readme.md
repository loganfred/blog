personal website project
========================

I've always wanted to make a blog and website portfolio, but I decided to
finally do it after some encouragement from Luke Smith and his admonition
against internet serfdom.

In the past I've tried to use wordpress as a blogging platform, but I never
really got into it. There are a couple reasons for this.

1. I don't care for WYSIWYG text editors
2. All the plugins can be overwhelming
3. Customizing themes requires some hardcore web development knowledge

I want to find a better solution that fits in with the tools I already enjoy
using.

1. Write content in markdown with the Vim text editor and the Vimwiki plugin.
2. Compile markdown into Jinja2 HTML templates using custom Pandoc templates.
3. Scrape metatada at compile time for simple JSON-based CMS database.
4. Use the Python Flask framework to host a lightweight website.

Spelled out, we have:

Vim, but using the Vimwiki plugin, but with markdown syntax rather than wiki
syntax, compiled using a custom python script calling pandoc, but compiled
into Jinja2 templates rather than HTML, and displayed using a flask webserver.

It's a niche solution to a niche problem.

## Why so convoluted?

1. I already use Vim and the Vimwiki / Vim-Zettel plugins for organizing all my
   notes, passwords, bookmarks, thoughts, etc. so this part makes my life
   easier. I already have a library of content in this system.

2. Even though Pandoc isn't the most lightweight way to compile markdown to
   HTML, I find the Pandoc markdown syntax to be the most robust and
   convenient. I especially like that I can define custom metadata using a
   clean YAML section at the top of each document. At compile-time I can tell
   Pandoc to generate separate JSONs from the YAML metadata in each file as a
   simple way of aggregating metadata for an eventual database.

3. Compiling to Jinja2 templates as an intermediary rather than directly to
   HTML is nice because it lets me use template inheritance.

The ultimate goal here is to use Git hooks to make everything seamless.
