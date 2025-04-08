FROM python:slim

# upgrade pip
RUN pip install --upgrade pip

# create non-root user
RUN adduser --disabled-password --comment "" flask

# create working directory
RUN mkdir -p /home/app/data && chown -R flask:flask /home/app

WORKDIR /home/app
USER flask

# copy files
COPY --chown=flask:flask . .

# virtual environment
ENV VIRTUAL_ENV=/home/app/venv
RUN python -m venv $VIRTUAL_ENV --system-site-packages
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000
ENV PYTHONUNBUFFERED=1

# declare volume (optional)
VOLUME ["/home/app/data"]

# launch
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]