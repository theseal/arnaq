FROM python:3.10.5-bullseye

COPY arnaq.py /arnaq.py
CMD ["/arnaq.py"]
