GIT_COMPLETION_SCRIPT=~/Home/pi/Documents/git-completion.bash

if [ -f $GIT_COMPLETION_SCRIPT ]; then
    . $GIT_COMPLETION_SCRIPT
fi

# Git-aware prompt -- show git branch in prompt when repo exists in current dir$

 

function parse_git_branch {

ref=$(git symbolic-ref HEAD 2> /dev/null) || return

echo "["${ref#refs/heads/}"]"

}

 

PS1="\[\e[0;32m\]\h\[\033[0m\]:\W\[\e[0;36m\]\$(parse_git_branch)\[\033[0m\] \u$
