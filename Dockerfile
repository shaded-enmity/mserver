FROM fedora:22
MAINTAINER Pavel Odvody <podvody@redhat.com>

RUN dnf install -y python-flask python-flask-sqlalchemy python-psycopg2

COPY app.py /usr/bin/

ENTRYPOINT ["app.py"]
