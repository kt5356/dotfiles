# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
ZSH_THEME="steeef"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"


# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="false"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git git-extras brew meteor osx pip pyenv python sudo zsh-syntax-highlighting zsh-history-substring-search osx)

# User configuration

export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
# export MANPATH="/usr/local/man:$MANPATH"

source $ZSH/oh-my-zsh.sh
source ~/.bash_profile

export AWS_PROFILE=nextdev
export AWS_SDK_LOAD_CONFIG=1
export LC_ALL=en_US.UTF-8

alias o2a="okta2aws"
alias tf="terraform"
alias gs="git status"
alias gd="git diff"
alias ga="git add -A"
alias gc="git commit"
alias gca="git commit --amend"
alias gp="git push"
alias cdi="cd ~/inf_iaas_api/iaas"
alias copy='fc -ln -1 | sed "1s/^[[:space:]]*//" | awk 1 ORS="" | pbcopy '
alias edit="atom ~/inf_portal_api ~/inf_iaas_api"
alias mkdir="mkdir -p"
alias mv="mv -iv"
alias cp="cp -iv"
alias rm="rm -v"
alias del="mv $1 ~/.unixtrash"
alias rd="rm -rfv"
alias hd="head"
alias tl="tail"
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias bashconfig="vim ~/.bash_profile"
function hide(){
    defaults write com.apple.finder AppleShowAllFiles -bool NO
    killall Finder
}
function show(){
    defaults write com.apple.finder AppleShowAllFiles -bool YES
    killall Finder
}
function removetest(){
    mkdir ~/.Trash
    mv $1 ~/.Trash
}

# bind UP and DOWN arrow keys
zmodload zsh/terminfo
# bind UP and DOWN arrow keys
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
zmodload zsh/terminfo

# tabtab source for serverless package
# uninstall by removing these lines or running `tabtab uninstall serverless`
[[ -f /usr/local/lib/node_modules/serverless/node_modules/tabtab/.completions/serverless.zsh ]] && . /usr/local/lib/node_modules/serverless/node_modules/tabtab/.completions/serverless.zsh
# tabtab source for sls package
# uninstall by removing these lines or running `tabtab uninstall sls`
[[ -f /usr/local/lib/node_modules/serverless/node_modules/tabtab/.completions/sls.zsh ]] && . /usr/local/lib/node_modules/serverless/node_modules/tabtab/.completions/sls.zsh
# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/kevin.tahmoresi/Downloads/google-cloud-sdk/path.zsh.inc' ]; then source '/Users/kevin.tahmoresi/Downloads/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/kevin.tahmoresi/Downloads/google-cloud-sdk/completion.zsh.inc' ]; then source '/Users/kevin.tahmoresi/Downloads/google-cloud-sdk/completion.zsh.inc'; fi

export NVM_DIR="$HOME/.nvm"
. "/usr/local/opt/nvm/nvm.sh"

export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH
[ -d $GOPATH/bin ] && export PATH=$PATH:$GOPATH/bin

autoload -U +X bashcompinit && bashcompinit
complete -o nospace -C /usr/local/bin/vault vault

# tabtab source for slss package
# uninstall by removing these lines or running `tabtab uninstall slss`
[[ -f /Users/kevin.tahmoresi/next/identity/cloud-directory/deployments/serverless/directory/node_modules/tabtab/.completions/slss.zsh ]] && . /Users/kevin.tahmoresi/next/identity/cloud-directory/deployments/serverless/directory/node_modules/tabtab/.completions/slss.zsh
