#!/bin/bash

# Print the current date and time
echo "Script execution time: $(date '+%Y-%m-%d %H:%M:%S')"

# Get User Input
IMAGE="flask"
CONTAINER_NAME="fapi"
PORT="5000"

# Get the User Input
read -p "Please enter, you want to build image or rm image: " BD
if [[ $BD == "build" ]];
then 
docker build -t $IMAGE .
echo "starting/running a container.."
docker run -dit --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE
docker ps -a
elif [[ $BD == "rm" ]];
then
echo "stopping/removing container and image forcefully.."
docker stop $CONTAINER_NAME
docker $BD -f $CONTAINER_NAME
docker ${BD}i -f $IMAGE
sleep 2
else
echo "Please try with the correct options.."
fi
echo "######################################################"
echo "Finally listing docker images/containers available in local system.."
docker images
docker ps -a
exit 0
