#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'


start_process() {
    echo "${GREEN}Starting script!!!!!!"

    echo "${GREEN}Entering into frontend folder"

    cd frontend

    echo "${YELLOW} Cleaning the frontend folder..."
    rm -rf node_modules build 
    
    if ! command -v yarn &> /dev/null
    then
        echo "${RED}yarn not found installing...."
        npm i -g yarn
        echo "${GREEN}yarn installed sucessfully"
        exit
    fi

    echo "${GREEN}Running yarn install..."
    npx yarn install

    echo "${GREEN}Building and relocate the static files..."
    yarn run relocate    

    echo "${GREEN}Frontend is Depolyed now processing backend..."

}

start_process