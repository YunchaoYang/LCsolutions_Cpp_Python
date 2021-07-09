
if [1 == 2] then

   # How to configure git
   git config --global alias.add-commit '!git add -A && git commit'

   # How to reboot gnome if it is frozen
   killall -HUP gnome-shell

   # How to use ffmpeg to generate video
   ffmpeg -r 15 -start_number 1 -f image2 -i "img.%04d.jpeg" -vcodec png Myvideo.avi
   # generate mkv
   ffmpeg -framerate 30 -i "rotate_sphere.%04d.jpeg" -codec copy output.mkv
   # convert avi gif   
   ffmpeg -i video.avi -t 10 out%02d.gif


   # useful find command

   # find and rename
   find . -name "*.png" -exec bash -c 'convert "$1" "${1%.png}".jpg' - '{}' \;
   # find and convert .png to .jpg
   find . -name "*.png" -exec bash -c 'convert "$1" "${1%.png}".jpg' - '{}' \;
   # find a file and grep the line containing "outpost" 
   find . -name 'uniform.usr'  -exec grep -H "outpost" {} \;
   
   # rename
   # option 1
   for file in *.dat
   do
       mv "$file" "${file%.dat}.txt"
   done
   # option 2
   find . -iname "*dbg*" -exec rename _dbg.txt .txt '{}' \;

   # How to fix nvidia driver issue
   sudo apt-get remove --purge nvidia-*
   # dmesg

    # install nvidia
    # sudo apt-get install nvidia-*
    alias tial="tail"
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'

    # some more ls aliases
    alias emacs='emacs -nw'
    alias emac='emacs -nw'
    alias pointwise='/opt/Pointwise/PointwiseV18.0R1/pointwise'
    alias bjobs="top -u hityangsir"
    alias bkill="kill"
    alias ll='ls -alF'
    alias la='ls -A'
    alias l='ls -CF'
    alias l='ls'
    alias llt='ls -altr'
    alias la='ls -altr'
    alias c='clear'

    export PATH=$HOME/Nek5000/Nek5000-v1/bin:$PATH

# How to Find Out Top Directories and Files (Disk Space) in Linux
# https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/
du -hs * | sort -rh | head -5
# enable color support of ls and also add handy aliases
   if [ -x /usr/bin/dircolors ]; then
       test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
       
       alias gima="git commit -a -m "
       alias ls='ls --color=auto'
       #alias dir='dir --color=auto'
       #alias vdir='vdir --color=auto'

   fi
fi
