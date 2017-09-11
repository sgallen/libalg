FROM python:3.6

RUN mkdir /linalg

# We have to add the requirements because volume created by docker-compose isn't
# available yet.
# ADD requirements.txt /linalg

WORKDIR /linalg

# Install the python packages
# RUN pip3 install -r requirements.txt;

# Create user to run as by default it will be UID=1000 GID=1000.  This can be
# overriden by setting enviroment variables USER_UID/USER_GID before running 
# docker commands.
ARG USER_UID
ARG USER_GID

RUN set -x  \
    && mkdir /home/linalg \
    && groupadd linalg --gid=${USER_GID:-${USER_UID:-1000}} \
    && useradd -d /home/linalg -g linalg --uid=${USER_UID:-1000} linalg \
    && chown linalg:linalg /home/linalg \
    && chmod 755 /home/linalg

USER linalg
