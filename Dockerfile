FROM mysql:latest
RUN -n mysql -e MYSQL_ROOT_PASSWORD=Nekito2001 -d mysql:latest
RUN -it --rm mysql mysql -h localhost -u root -p Nekito2001



FROM python:3.8
RUN mkdir /python_intro
COPY . /python_intro/
WORKDIR /python_intro
RUN chmod +x ./run.sh
ENTRYPOINT [ "/run.sh" ]
