nnoremap <leader>c :call Compile()<CR>
nnoremap <leader>v :call Run()<CR>

nnoremap <leader>1 :call LoadTemplate(1)<CR>
nnoremap <leader>2 :call LoadTemplate(2)<CR>
nnoremap <leader>3 :call LoadTemplate(3)<CR>

" Normal paste in inline terminal
tmap <C-v> <C-w>"+

" Utility
let g:utilDir = $CP_COMMON_UTIL_DIR
let g:templates = ["template-basic.cpp", "template.cpp", "template-ext.cpp"]

function! LoadTemplate(id)
	let s = ":0r " . g:utilDir . "/templates/" . g:templates[a:id - 1]
	" Delete first
	execute ":normal ggdG"
	execute s
endfunction

function! ExecCommand(cmd)
  execute ":vertical belowright term cmd.exe /c (" . a:cmd . ")"
endfunction

function! Compile()
	execute ":w"
	call ExecCommand("python " . g:utilDir . "/processor.py -compile %")
endfunction

function! Run()
	call ExecCommand("python " . g:utilDir . "/processor.py -run %")
endfunction
