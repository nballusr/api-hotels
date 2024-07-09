# API-Hotels

This repository contains a simple API service to manage hotels' information.

## Local setup

### Prerequisites

In order to bootstrap local development environment, you need the following:

- Unix like OS
- Docker
- Docker Compose

### Installation

To set up the local environment for the first time, execute the following command:

```
make install
```

This process will build all required docker images and start them as services.

### Development

Once installed, the project can be managed executing the following commands:

```
# start local environment
make start

# stop local environment
make stop

# clean, stop and start local environment
make restart
```

The available services will be displayed as the command output.

### Services

After starting the project, you will have the following services locally available.

#### API

The API is available at http://localhost:8080

#### API Doc

The API documentation is available at http://localhost:8080/docs

### Migrations

❗️ All models need to be imported and added to `migrations/models.py` in order to be detected by Alembic.

Run `make shell` to enter the application container. Then:

- To apply migrations: `alembic upgrade head`.
- To generate a migration automatically: `alembic revision --autogenerate -m "Some message"`.
- To generate an empty migration file: `alembic revision -m "Some message"`.

Once the migration file is generated, you should review it at `migrations/revisions/` and tweak it as needed.

### Adding a dependency

To install new dependencies, you can use `poetry` inside the python container:

```
# Enter the python container
make shell

poetry add pandas scikit-learn

## Use --group dev for dev dependencies
poetry add --group dev pandas scikit-learn
```

## Tests

To execute all tests, run:

```
make tests
```

To just execute unit and integration tests, run:

```
make pytest
```

To just execute acceptance tests, run:

```
make acceptance
```
