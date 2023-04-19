# RPCDemo

## RPC Model
In this demo we seek to convey the RPC model that provides the basis for distributed systems. The diagram below summarizes how the functions in the client and server code fit into the model.

![RPC_Image](https://user-images.githubusercontent.com/66653384/230818654-a3c51de1-8699-4874-906f-ea7117bc5757.png)

## Running the Demo (in 10 easy steps!)
1) Download docker: https://docs.docker.com/engine/install/
2) Clone this repo
3) Navigate to "Server" folder
4) Run `docker build -t calc_server .`. This will build an image of the server container
5) Run `docker run -p 5000:5000 calc_server` This will create the container (run the image). At this step you'll also want to copy the IPAddress of the server container
6) Navigate to the "Client" folder
7) Update the "ip" variable with the IPAddress field value of server
8) Run `docker build -t calc_client .`. This will create an image of the client container
9) Run `docker run -p 5050:5050 calc_client` This will create the container (run the image)
10) Open localhost:5050 in your browser :)

## Cleaning Up
1) Run `docker container ls`. Copy the container ids for the calc_client and calc_server containers
2) Run `docker stop [container_id_1] [container_id_2]`
3) Optional: user `docker image ls` and `docker image rm [image_id]` to delete the images
