#!/bin/bash

if [[ $# > 0 ]]
then
    dirname="$1"
    shift
else
    dirname="opencv/faces/train/"
fi

if [[ ! -d "$dirname" ]]
then
    exit 1
fi

cd "$dirname"

if [[ $# > 0 ]]
then
    label="$1"
    shift
    
    if [[ ! -d "$label" ]]
    then
        mkdir "$label"
    fi
    
    cd "$label"
    
    loop=1
    while [[ $loop == 1 || $# > 0 ]]
    do
        loop=0
        if [[ $# > 0 ]]
        then
            name="$1"
            shift
        else
            name="$(ls | grep -E ^[0-9]+[.]png | tail -1)"
            if [[ "$name" != "" ]]
            then
                name="${name::-4}"
            fi
            (( name++ ))
        fi
        
        raspistill -o $name.png -t 1 -p '50,350,800,600'
    done
else
    label=""
    name=""
    loop=1
    
    while [[ $loop == 1 ]]
    do
        label0="$label"
        name0="$name"
        
        read -p "Enter the name: [$label0] " label
        
        if [[ "$label" == "" ]]
        then
            if [[ "$label0" == "" ]]
            then
                echo "No name given."
                continue
            else
                label="$label0"
            fi
        else
            name0=""
        fi
        
        if [[ ! -d "$label" ]]
        then
            mkdir "$label"
        fi
        
        cd "$label"
        
        if [[ "$name0" == "" ]]
        then
            name0="$(ls | grep -E ^[0-9]+[.]png | tail -1)"
            if [[ "$name0" != "" ]]
            then
                name0="${name0::-4}"
            fi
        fi
        (( name++ ))
        
        read -p "Enter file number: [$name0] " name
        
        if [[ "$name" == "" ]]
        then
            name="$name0"
        fi
        
        raspistill -o $name.png -t 1 -p '50,350,800,600'
        
        echo "Exit the preview to continue ..."
        gpicview $name.png
        
        cd ..
    done
fi
