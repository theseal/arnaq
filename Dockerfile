FROM python:3.11-bullseye

RUN python3 -m pip install poetry

COPY poetry.lock pyproject.toml /

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY arnaq.py /arnaq.py
CMD ["/arnaq.py"]
