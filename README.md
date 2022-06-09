# doc-summary

REST APIs for storing and getting a summary of a large text.

## APIs Summary

1. [POST /documents/]

TBA

2.[GET /documents/{id}/]

TBA

3.[GET /documents/{id}/summary/]

TBA

4.[GET /documents/]

## Local development

- Clone the repo and ```cd``` into the directory.
- Create .env using .env.sample as a reference.

- To run the API server:

    ```sh
    make start-dev
    ```

- To run the server after making code changes(rebuilds the docker image and restarts the container):

    ```sh
    make refresh-dev
    ```

- To stop the server:

    ```sh
    make stop-dev
    ```

- To run the tests in docker environment:
  
    ```sh
    make test
    ```

## Running the unit and integration tests

- Create .env_test using .env_test.sample as a reference.

    Make sure POSTGRES_SERVER is set to the correct value.

- Set the environment variables with the following terminal command

    ```sh
    set -a && source .env_test && set +a
    ```

- To run the tests on local environment:

    ```sh
    make test-local
    ```

## Limitations

- Works only with English text.
- Currently supports only plain text documents
