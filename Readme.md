# Vaccination Information System - VIC - cli

The aim of this tool is to update daily the statistics of the first vaccinations by county in Catalonia


## Requirements
- [Docker Engine](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
# Usage
Clone this repository, then start the service locally using docker compose:
```bash
docker-compose up -d
docker exec -it vic_cli vic -h # show cli help information
docker exec -it vic_cli vic
```

## TODO / Future work
- Create a tests
- Include args to update by county or a date range
- Improve db schemas in order to get better statistics 
- Add more provinces

