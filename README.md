# Red Dragon FastAPI Assignment

### Run Docker
```bash
docker-compose up
```

### Send text to be converted into speech.
```bash
curl --location 'http://127.0.0.1:4000/query' \
--header 'Content-Type: application/json' \
--data '{
    "content": "The quick brown fox jumps over the lazy dog."
}' \
--output-dir <output file location> \
--output '<output file name>.wav'
```