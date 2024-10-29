FROM public.ecr.aws/lambda/python:3.12

RUN /var/lang/bin/python3.12 -m pip install --upgrade pip

RUN yum install git -y

RUN git clone https://github.com/jinsu9758/lambda_docker_test.git

RUN pip install -r lambda_docker_test/requirements.txt

WORKDIR lambda_docker_test/

CMD ["lambda_function.handler"]
