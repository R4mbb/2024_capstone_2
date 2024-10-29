FROM amazon/aws-lambda-python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

RUN yum install git -y

RUN git clone https://github.com/jinsu9758/lambda_docker_test.git

RUN pip install -r lambda_docker_test/requirements.txt

WORKDIR lambda_docker_test/

CMD ["lambda_function.handler"]
