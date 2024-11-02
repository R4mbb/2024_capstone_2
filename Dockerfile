FROM public.ecr.aws/lambda/python:3.12

RUN /var/lang/bin/python3.12 -m pip install --upgrade pip

RUN dnf install git -y

RUN git clone https://github.com/jinsu9758/lambda_docker_test.git

RUN pip install -r lambda_docker_test/requirements.txt

COPY lambda_docker_test/ /var/task

CMD ["lambda_function.handler"]
