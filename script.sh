#!/bin/sh

# https://jnduli.co.ke/vimwiki-website-deployment-using-git-hooks.html

cmd="VimwikiAll2HTML"$(test "$1" = '-f' && echo '!')

vim -R -c ':VimwikiIndex'   -c $cmd -c 'qa!' < /dev/tty
vim -R -c ':VimwikiIndex 2' -c $cmd -c 'qa!' < /dev/tty
vim -R -c ':VimwikiIndex 3' -c $cmd -c 'qa!' < /dev/tty
vim -R -c ':VimwikiIndex 4' -c $cmd -c 'qa!' < /dev/tty
vim -R -c ':VimwikiIndex 5' -c $cmd -c 'qa!' < /dev/tty

# sync
rsync -rav ~/vimwiki/html/public/ ~/source/blog/flaskapp/templates/content
rsync -rav ~/vimwiki/static/assets/ ~/source/blog/flaskapp/static/assets
