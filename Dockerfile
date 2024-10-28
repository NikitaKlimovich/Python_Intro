FROM mysql:latest
EXPOSE 3306
RUN mkdir /python_intro
COPY . /python_intro/
WORKDIR /python_intro
ARG r
ENV room=$r
ARG s
ENV stud=$s
ARG f
ENV format=$f
RUN chmod +x /usr/bin/apt-get
RUN apt-get update && \
    apt-get install -y python3-pip
RUN apt install python3.10-venv
RUN python3 -m venv python_intro_env
RUN source python_intro_env/bin/activate
RUN pip install -r requirements.txt
RUN chmod +x python3 main.py -r $room -r $stud -r $format
ENTRYPOINT [ "python3", "main.py" ]
