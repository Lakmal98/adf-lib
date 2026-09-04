# Atlassian validation samples

Generate JSON documents with Docker Compose:

```bash
docker compose run --rm samples
```

Copy files from `samples/generated/` into Atlassian's ADF validator or an Atlassian API request. The generated files are ignored by Git so they can be regenerated and edited locally.

Run the test suite with:

```bash
docker compose run --rm test
```