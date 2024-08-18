#!/bin/bash
# Print the execution time
echo "Execution date/time: " $(date '+%Y-%m-%d %H:%M:%S')
# Provide information about the script functionality
echo "Building docker image and runs the contianer of it"
# Define the location of the Dockerfile
DFILE="/Users/murugat/Downloads/dock/flask_development/second_proj/flask_mysql"
echo "The Dockerfile is located at: ${DFILE}"
# Prompt for the Image name
read -p "Please enter the Image name: " IMAGE
echo "You've entered IMAGE name as: ${IMAGE}"
# Build the Docker image
echo "Image preparation begins shortly..."
docker build -t ${IMAGE} ${DFILE}
if [ $? -ne 0 ]; then
    echo "Error: Docker build failed."
    exit 1
fi
# List Docker images
docker images
# Prompt for the container name
read -p "Enter the name that you want to setup for the container: " DCONT

# Run the Docker container
docker run -dit --name ${DCONT} -p 5000:5000 ${IMAGE}
if [ $? -ne 0 ]; then
    echo "Error: Docker run failed."
    exit 1
fi
# List Docker containers
echo "list out running and stopped containers list.."
docker ps -a

# List Docker images 
echo "list out available Docker Images in local system.."
docker image ls 

# Sleep for 1 minutes to do post-checkouts
echo "sleep for 60 seconds to do your post checkouts"
sleep 60
## Checkouts using localhost
# http://localhost:5000    

# Stop/Delete Docker container and Image
read -p "Hope you have done with the testing, hence would you like to stop/delete the container, say yes or no:" TEST_STATUS
echo "You've entered the testing_status as:" $TEST_STATUS

if [[ $TEST_STATUS == yes ]]; then
echo "delete container in progress followed by stop container."
read -p "Enter the container name or container_id pls:" CNOID
docker stop $CNOID
docker ps -a
docker rm -f $CNOID
sleep 2
docker ps -a
elif [[ $TEST_STATUS == no ]]; then
echo "Ignoring stop/delete container operations"
else:
echo "Please choose the right option"
fi
docker rmi -f ${IMAGE}
docker image ls
exit 0
