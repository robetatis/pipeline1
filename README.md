To run automatically:
1. Build image from `Dockerfile`: `docker build -t <container_name> .`
2. Run container: `docker run <container_name>`

To run manually:
1. Comment out line 28 of Dockerfile: `# CMD ["spark-submit", "pipeline.py"]`
2. Carry out step 1 as in previous section
3. Run container in interactive detached mode `docker run -itd <container_name>`
4. Use `docker ps -a` to find `container_id`
5. Access the running container in interactive mode: `docker exec -it <container_id> sh`
6. Inside container, navigate to project folder and submit spark job: 
	```shell
	spark-submit pipeline.py
	```
