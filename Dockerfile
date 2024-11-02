FROM public.ecr.aws/lambda/python:3.12

RUN /var/lang/bin/python3.12 -m pip install --upgrade pip

RUN dnf install git -y

RUN git clone https://github.com/jinsu9758/lambda_docker_test.git /var/task

RUN pip install -r /var/task/requirements.txt

WORKDIR /var/task

CMD ["lambda_function.handler"]
