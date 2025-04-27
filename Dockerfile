FROM bitnami/spark:3.5.3 as spark_base

USER root
ARG SPARK_VERSION=3.5.5
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      unzip \
      rsync \
    #   openjdk-11-jdk \
      build-essential \
      software-properties-common \
      ssh 
    #   && \
    # apt-get clean && \
    # rm -rf /var/lib/apt/lists/*do


# RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
# WORKDIR ${SPARK_HOME}

# RUN curl https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz -o spark-${SPARK_VERSION}-bin-hadoop3.tgz \
#  && tar xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz --directory /opt/bitnami/spark --strip-components 1 \
#  && rm -rf spark-${SPARK_VERSION}-bin-hadoop3.tgz


# Install python deps
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV PATH="/opt/bitnami/spark/sbin:/opt/bitnami/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/bitnami/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

# COPY spark-defaults.conf "$SPARK_HOME/conf"

RUN chmod u+x /opt/bitnami/spark/sbin/* && \
    chmod u+x /opt/bitnami/spark/bin/*

ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

COPY entrypoint.sh .
RUN chmod u+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]