# doc-summary

REST APIs for storing and getting a summary of a large text.

## Interactive API Documentation

Interactive API documentation for the REST API can be accessed under

- [/docs] - for Swagger UI

    Eg. <http://localhost:8080/docs>

- [/redoc] - for Redoc

    Eg. <http://localhost:8080/redoc>

## API Endpoints

1. [POST /documents/]
     API to create a new document.

     Eg:

     ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello World"}' http://localhost:8080/documents/
    ```

2. [GET /documents/{id}/]

    API to retrieve a document.

    Eg:

    ```sh
    curl -X GET http://localhost:8080/documents/1/
    ```

3. [GET /documents/{id}/summary/]

    API to retrieve(generate) a summary of a document.

    Eg:

    ```sh
    curl -X GET http://localhost:8080/documents/1/summary/
    ```

4. [GET /documents/]

    API to retrieve all documents.

    Eg:

    ```sh
    curl -X GET http://localhost:8080/documents/
    ```

## Local development

- Clone the repo and ```cd``` into the root directory.

- Create `.env` file using `.env.sample` as a reference.

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

- To run the (unit and integration)tests in docker environment:
  
    ```sh
    make test
    ```

## Running the unit and integration tests locally(outside of docker container)

- Create .env_test using .env.sample as a reference.
- Update the value of POSTGRES_SERVER with correct postgres server value.
- Set the environment variables with the following terminal command

    ```sh
    set -a && source .env_test && set +a
    ```

- To run the tests on local environment:

    ```sh
    make test-local
    ```

## Steps involved in extracting the text summary

Python NLP library NLTK is used to extract the summary.

The steps involved (under `app/nlp.py`) in extracting the summary are:

- Preprocessing the text.
- Tokenization of the text into sentences.
- Generate term frequency(weighted) matrix.
- Generate sentence score matrix.
- Get top n sentences and generate the summary.

Deep learning libraries could be used to generate the summary to improve the performance of text summarization.

## Limitations

- Works only with English text.
- Currently supports only plain text documents
- Has not been tested on large documents.

## Future plans

To make the codebase production ready.

- [ ] Add support for other languages.
- [ ] Test the API with real data.
- [ ] Test the API with large text.
- [ ] Handle extraction of summary for very large text with background task.
- [ ] Incorporate Deep Learning based text summarization to improve the performance.
- [ ] Add support for other document types (e.g. PDF, Word, etc.)
- [ ] Add support for other document formats (e.g. JSON, XML, etc.)
- [ ] Add support for other document storage (e.g. S3, GCS, etc.)
- [ ] Provide simple GUI interface for uploading and getting the summary of the document.
- [ ] Add docker configuration for production (security, concurrency, db volume, application/web servers etc.)

## References

- [1] <https://www.nltk.org/>
- [2] <https://fastapi.tiangolo.com/tutorial/>
- [3] <https://github.com/Mathuv/PPSPM-TextMM>
