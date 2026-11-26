# base image

FROM python:3.13-slim

# 2: working directory

WORKDIR /myapp

# 3: copy project files to the working directory

COPY . /myapp

#  4: run, install alll the requirements in the image

RUN pip install -r requirements.txt

# 5: expose ports, usuallly 5000 port is used for flask

EXPOSE 5000

# 6: command

CMD ["python", "./app.py"]