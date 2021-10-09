# Specify base image 

FROM python:alpine

# Install dependenies for application
WORKDIR ./django-polls/dist

COPY ./ ./


#RUN python -m pip install Django
#RUN python -m pip install Pillow
RUN python -m pip install --user ./mysite/django-polls/dist/django-polls-0.1.tar.gz
#RUN  pip install psycopg
# Run Default Command.
EXPOSE 80
CMD ["python" ,"./mysite/manage.py","runserver","0:8090"]
