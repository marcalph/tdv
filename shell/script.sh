#!/bin/bash

function testcat(){
    local title="my sysinfo"
    cat <<- _EOF_
    <html>
    <head>
        <title>
        $title $HOSTNAME
        </title>
    </head>

    <body>
    <h1>$title $HOSTNAME</h1>
        <p>Updated on $(date +"%x %r %Z") by $USER</p>
    </body>
    </html>
_EOF_
}

if [ -f .bash_profile ]
then echo "You have a .bash_profile. Things are fine."
echo "wow"
else echo "Yikes! You have no .bash_profile!"
echo "waw"
fi

for filename in "$@"; do
    result=
    if [ -f "$filename" ]; then
        result="$filename is a regular file"
    else
        if [ -d "$filename" ]; then
            result="$filename is a directory"
        fi
    fi
    if [ -w "$filename" ]; then
        result="$result and it is writable"
    else
        result="$result and it is not writable"
    fi
    echo "$result"
done
# echo "You start with $# positional parameters"

# # Loop until all parameters are used up
# while [ "$1" != "" ]; do
#     echo "Parameter 1 equals $1"
#     echo "You now have $# positional parameters"

#     # Shift all the parameters down by one
#     shift

# done