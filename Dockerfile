FROM python:3.10

ARG UID=1000
ARG GID=1000

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | \
    POETRY_HOME=/opt/poetry python - --version 1.2.2 && \
    chmod a+x /opt/poetry/bin/poetry && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin

RUN addgroup python-user --gid $GID
RUN adduser python-user --gid $GID --uid $UID
RUN mkdir /application && chown python-user:python-user /application
USER python-user

WORKDIR /application
ENV WORKDIR=/application
ENV PYTHONPATH=$WORKDIR

CMD [".venv/bin/python", "-u", "src/server.py"]

