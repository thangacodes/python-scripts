#!/bin/bash

build_and_manage_container() {
    # variables
    IMAGE_TAG_NAME="flaskimage"
    CONT_NAME="fwebapp"
    
    echo "Script runtime is:" $(date '+ %d-%m-%Y %H:%M:%S')
    echo
    echo "Script is used to build image, run container from it.."
    echo
    echo "Checking folder structure of the Flask Web Application.."
    tree
    sleep 2
    read -p "Please enter the image name (feed the image name in lowercase): " DIMAGE
    echo "User entered image name as:" $DIMAGE
    docker build -t $DIMAGE .
    docker images
    sleep 4
    echo "Format of Docker Image Tag.."
    docker tag $DIMAGE:latest $IMAGE_TAG_NAME
    docker images
    sleep 3
    read -p "Would you like to test the flask web application using container (select 'yes or no' in lower case): " USER_INPUT
    echo "User entered input as:" $USER_INPUT
    if [[ $USER_INPUT == "yes" || $USER_INPUT == "y" ]]; then
        echo "You are good to create docker container.."
        echo "Container creation in progress ..."
        docker images
        echo
        docker run -d -p 5000:5000 --name $CONT_NAME $IMAGE_TAG_NAME
        docker ps
        docker logs -f $CONT_NAME
        curl -ivk http://localhost:5000/ | head -n 5
        sleep 5
    else
        echo "User input is: $USER_INPUT, hence no progress.."
    fi
    read -p "Would you like to stop/remove the container (say 'yes or no'): " USER_ACTION
    echo "User entered input as:" $USER_ACTION
    if [[ $USER_ACTION == "yes" || $USER_ACTION == "y" ]]; then
        echo "You are good to stop/remove docker container.."
        echo "Container stop/removing in progress ..."
        echo "list out the running/stopped container list"
        echo 
        docker stop $CONT_NAME
        sleep 3
        echo
        docker rm -f $CONT_NAME
    else
        echo "User input is: $USER_ACTION, hence no progress.."
    fi

    read -p "Would you like to docker image (say 'yes or no'): " USER_FEED
    echo "User entered input as:" $USER_FEED
    if [[ $USER_FEED == "yes" || $USER_FEED == "y" ]]; then
        echo "You are good to remove docker image.."
        echo "Removing docker image in progress ..."
        echo "list out the existing docker images.."
        echo
        docker rmi -f $DIMAGE $IMAGE_TAG_NAME
        sleep 3
        echo "finally testing if the image has deleted or not:"
        docker images
    else
        echo "User input is: $USER_FEED, hence no progress.."
    fi
}

# Calling the function
build_and_manage_container
exit 0