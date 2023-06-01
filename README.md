To run pipeline in a Docker container:

0. Clone repo
1. Navigate to project folder (`/pipeline1/`)
2. Build image from `Dockerfile`: `docker build -t <container_name> .`
3. Run container in interactive detached mode `docker run -itd <container_name>`
4. Use `docker ps -a` to find `container_id`
5. Access the running container in interactive mode: `docker exec -it <container_id> sh`
6. Inside container, you'll be taken automatically to project folder; there, submit spark job: 
	```shell
	spark-submit pipeline.py
	```
