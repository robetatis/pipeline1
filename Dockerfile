FROM python:3.9

# jdk 11
RUN apt-get update && apt-get install -y openjdk-11-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# install spark 3.0.1 with hadoop 2.7
RUN curl -O https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz \
	&& tar xf spark-3.0.1-bin-hadoop2.7.tgz \
	&& mv spark-3.0.1-bin-hadoop2.7 /opt/spark \
	&& rm spark-3.0.1-bin-hadoop2.7.tgz

# set up environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYSPARK_PYTHON=/usr/local/bin/python
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$SPARK_HOME/python/:$PYTHONPATH

# install python dependencies
RUN pip install numpy pandas psycopg2 pyspark

# copy app files
COPY *.py ./pipeline/
COPY resources/ ./pipeline/resources/

# set working directory 
WORKDIR /pipeline
