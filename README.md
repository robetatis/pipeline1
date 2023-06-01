To run pipeline in a Docker container:

0. Clone repo
1. Build image from `Dockerfile`: `docker build -t <container_name> .`
2. Run container in interactive detached mode `docker run -itd <container_name>`
3. Use `docker ps -a` to find `container_id`
4. Access the running container in interactive mode: `docker exec -it <container_id> sh`
5. Inside the container, create credentials for postgresql: navigate to folder (`/pipeline1/resources/credentials`) and create a python file named `connection_data.py`, containing the following object (you'll have to install vim in the container by doing `apt-get install vim`):
```python
connection_dict = {
    'user': 'xxxxxx', # your postgresql user name
    'password': 'xxxxxxxx', # your postgresql password
    'host': 'localhost',
    'database': 'postgres'
}
```

6. Inside the container, navigate to the main project folder `/pipeline/`; there, submit spark job: 
	```shell
	spark-submit pipeline.py
	```
