#!/bin/bash

function sizing() {
	result=
    if [ -f "$1" ]; then
        result=`du -sch $1`
    else 
        if [ -d "$1" ]; then
            result=`tree $1 --du -h`
        fi
    fi
    echo "$result"
}
