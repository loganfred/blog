diy cms server project
======================

**At least for now this is a solo project while I figure out how to use the Github site.**

rationale
---------

I've always wanted to make a website portfolio, but I decided to finally do it
after some encouragement from Luke Smith and his admonition against internet
serfdom.

In the past I've tried to use wordpress as a blogging platform, but I never
really got into it. There are a couple reasons for this.

1. All the plugins can be overwhelming
2. Creating your own themes is pretty intense
3. I don't like using the WYSIWYG editor

The goal of this project is to create a much more minimal long-form blogging
website using Python and Flask.

Instead of fiddling with an online editor I plan to write articles in Markdown
using Vim over SSH. Then I'll use a script to compile the markdown into HTML,
extract the assets, and stuff them in a database.
