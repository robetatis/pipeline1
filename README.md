To run automatically:
1. Build image from `Dockerfile`: `docker build -t <container_name> .`
2. Run container in detached mode: `docker run -itd <container_name>`

To run manually:
1. Comment out line 27 of Dockerfile: `# CMD ["spark-submit", "./pipeline/pipeline.py"]`
2. Carry out steps 1 and 2 of automatic run
3. Use `docker ps -a` to find `container_id`
4. Access container: `docker exec -it <container_id> sh`
5. Inside container, navigate to project folder and submit spark job: 
	```shell
	cd pipeline
	spark-submit pipeline.py
	```
