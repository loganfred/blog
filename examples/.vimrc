set nocompatible
filetype plugin on
syntax on
setlocal cm=blowfish2

set nofoldenable

call plug#begin('~/.vim/plugged')

"Plug 'VundleVim/Vundle.vim'
Plug 'https://github.com/vimwiki/vimwiki.git'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'michal-h21/vim-zettel'

call plug#end()

let s:main = {}
let s:main.name = 'private'
let s:main.path = '~/vimwiki/private'
let s:main.path_html = '~/vimwiki/html/private'
let s:main.template_path = '~/vimwiki/private/templates'
let s:main.template_default = 'main'
let s:main.template_ext = 'html'
let s:main.custom_wiki2html = '~/source/blog/convert.py'
let s:main.links_space_char = '_'
let s:main.syntax = 'markdown'
let s:main.automatic_nested_syntaxes = 1
let s:main.ext = '.md'

let s:zettelkasten = {}
let s:zettelkasten.name = 'zettelkasten'
let s:zettelkasten.path = '~/vimwiki/zettelkasten'
let s:zettelkasten.path_html = '~/vimwiki/html/public/zettelkasten'
let s:zettelkasten.template_path = '~/vimwiki/zettelkasten/templates'
let s:zettelkasten.template_default = 'zettelkasten'
let s:zettelkasten.template_ext = 'html'
let s:zettelkasten.custom_wiki2html = '~/source/blog/convert.py'
let s:zettelkasten.links_space_char = '_'
let s:zettelkasten.syntax = 'markdown'
let s:zettelkasten.automatic_nested_syntaxes = 1
let s:zettelkasten.ext = '.md'
let s:zettelkasten.auto_toc = 1
let s:zettelkasten.auto_tags = 1
let s:zettelkasten.auto_generate_tags = 1
let s:zettelkasten.auto_generate_links = 1

let s:writings = {}
let s:writings.name = 'writings'
let s:writings.path = '~/vimwiki/writings'
let s:writings.path_html = '~/vimwiki/html/public/writings'
let s:writings.template_path = '~/vimwiki/writings/templates'
let s:writings.template_default = 'article'
let s:writings.template_ext = 'html'
let s:writings.custom_wiki2html = '~/source/blog/convert.py'
let s:writings.links_space_char = '_'
let s:writings.syntax = 'markdown'
let s:writings.automatic_nested_syntaxes = 1
let s:writings.ext = '.md'

let s:books = {}
let s:books.name = 'books'
let s:books.path = '~/vimwiki/books'
let s:books.path_html = '~/vimwiki/html/public/books'
let s:books.template_path = '~/vimwiki/books/templates'
let s:books.template_default = 'books'
let s:books.template_ext = 'html'
let s:books.custom_wiki2html = '~/source/blog/convert.py'
let s:books.links_space_char = '_'
let s:books.syntax = 'markdown'
let s:books.ext = '.md'

let s:recipes = {}
let s:recipes.name = 'recipes'
let s:recipes.path = '~/vimwiki/recipes'
let s:recipes.path_html = '~/vimwiki/html/public/recipes'
let s:recipes.template_path = '~/vimwiki/recipes/templates'
let s:recipes.template_default = 'recipes'
let s:recipes.template_ext = 'html'
let s:recipes.custom_wiki2html = '~/source/blog/convert.py'
let s:recipes.links_space_char = '_'
let s:recipes.syntax = 'markdown'
let s:recipes.ext = '.md'

" vim wiki
let g:vimwiki_list = [s:main, s:zettelkasten, s:writings, s:books, s:recipes]

let g:vimwiki_global_ext = 0
let g:vimwiki_listsym_rejected = '/'
let g:vimwiki_listsyms = ' ◴↻x'
let g:vimwiki_filetypes = ['markdown', 'pandoc']
let g:vimwiki_dir_link = 'index'
let g:vimwiki_folding = 'expr:quick'
let g:vimwiki_auto_chdir = 1
let g:vimwiki_auto_header = 1
let g:vimwiki_automatic_nested_syntaxes = 1
let g:vimwiki_markdown_link_ext = 1
"" let g:vimwiki_conceal_pre = 1

" vim zettel
let g:zettel_options = [{},
                        \{'zettelkasten':{'tags': ''},
                        \'template': '~/vimfiles/zettelkasten/template.tpl'}]

let g:zettel_format = "%y%m%d-%H%M-%title"

" mappings for vimwiki / vimzettel
nnoremap <leader>vt :VimwikiSearchTags<space>
nnoremap <leader>vs :VimwikiSearch<space>
nnoremap <leader>bl :VimwikiBacklinks<cr>
nnoremap <leader>gt :VimwikiRebuildTags!<cr>:VimwikiGenerateTagLinks<cr><c-l>
nnoremap <leader>zs :ZettelSearch<cr>
nnoremap <leader>zn :ZettelNew<space>
nnoremap <leader>zo :ZettelOpen<cr>

function! VimwikiLinkHandler(link)
" Use Vim to open external files with the 'vfile:' scheme.  E.g.:
"   1) [[vfile:~/Code/PythonProject/abc123.py]]
"   2) [[vfile:./|Wiki Home]]
let link = a:link
if link =~# '^vfile:'
  let link = link[1:]
else
  return 0
endif
let link_infos = vimwiki#base#resolve_link(link)
if link_infos.filename == ''
  echomsg 'Vimwiki Error: Unable to resolve link!'
  return 0
else
  exe 'tabnew ' . fnameescape(link_infos.filename)
  return 1
endif
endfunction

" remember to update 508: ~/.vim/plugged/vimwiki/ftdetect/vimwiki.vim

endif

" open any secret files with encryption
au BufRead .secret call StartSecretFile()

function StartSecretFile()
    set filetype=yaml
    set noundofile viminfo=
    set nonu nocursorcolumn nocursorline
    set wrap tw=125
    set cc=0 nonu
    set nohlsearch
endfunction
