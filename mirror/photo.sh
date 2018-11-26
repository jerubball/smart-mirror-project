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
            name="${test::-4}"
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
        
        read -p "Enter the name: [$label] " label
        
        if [[ "$label" == "" ]]
        then
            if [[ "$label0" == "" ]]
            then
                echo "No name given."
                continue
            else
                label="$label0"
            fi
        fi
        
        if [[ ! -d "$label" ]]
        then
            mkdir "$label"
        fi
        
        cd "$label"
        
        (( name++ ))
        read -p "Enter file number: [$name] " name
        
        if [[ "$name" == "" ]]
        then
            if [[ "$name0" == "" ]]
            then
                name="$(ls | grep -E ^[0-9]+[.]png | tail -1)"
                name="${test::-4}"
            else
                name="$name0"
            fi
            (( name++ ))
        fi
        
        raspistill -o $name.png -t 1 -p '50,350,800,600'
        
        echo "Exit the preview to continue ..."
        gpicview $name.png
    done
fi
