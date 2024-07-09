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

## Project Architecture and Design Patterns

### Dependency Injection

This project leverages the dependency-injector package to manage dependencies in a clean and modular way. Dependency
Injection (DI) allows for greater flexibility and testability by decoupling the creation and management of dependencies
from the business logic.

### Command Query Responsibility Segregation (CQRS)

The project employs the Command Query Responsibility Segregation (CQRS) pattern along with middlewares to handle
business logic in a clear and concise manner.

### Hexagonal Architecture

The project is organized following the principles of Hexagonal Architecture. This architectural style helps in creating
a system that is easier to maintain, test, and adapt to future requirements.

### Summary

Combining dependency injection, CQRS with middlewares, and Hexagonal Architecture results in a highly decoupled,
maintainable, and scalable codebase. This architectural approach ensures that the core business logic remains clean and testable while facilitating easy integration with various external systems and services.
