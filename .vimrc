set nocompatible
set showmode
set showcmd
set showmatch
set incsearch
set hlsearch
set ignorecase
set smartcase
set scrolloff=5
set wildmode=longest,list
set number
set autoindent
set smartindent
set nowrap
set shiftwidth=4
set tabstop=4
set mouse=n
set statusline=%F%m%y[%p%%][%l-%L],[%c],[%V]
set laststatus=2
set listchars=tab:>-,trail:-,eol:<
set list


"let python_highlight_all=1
"au BufRead,BufNewFile *.py set filetype=python
"au! Syntax python source $VIM/syntax/python3.0.vim
"autocmd FileType python set complete+=k~/.vim/syntax/python3.0.vim isk+=.,(

au BufWinLeave * mkview
au BufWinEnter * silent loadview
"au FileType xml setlocal equalprg=xmllint\ --format\ --recover\ -\ 2>/dev/null foldmethod=syntax

nnoremap <CR> :noh<CR><CR>
nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>
nnoremap <F3> :set nolist!<CR>
nnoremap <F4> :1,$!xmllint --format --recover - 2>/dev/null<CR>
"let g:xml_syntax_folding=1

filetype on
syntax on
"if version >= 700
"        colo zenburn
"else
"        colo oceandeep
"endif
