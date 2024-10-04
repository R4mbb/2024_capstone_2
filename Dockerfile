FROM amazon/aws-lambda-python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

RUN yum install git -y

RUN git clone https://github.com/kimcheolgi/Lambda_Docker.git

RUN pip install -r Lambda_Docker/requirements.txt

RUN cp Lambda_Docker/lambda_function.py /var/task/

CMD ["lambda_function.handler"]