# Migration


## Restore backups
To restore a specific backup, move the backup file to ./data/releases/postgres/public_release.tar.tz, and run the following command 

```Bash
docker-compose --profile postgres up
```

This will first start the postgres docker container then start a loading service that takes the backup file and loads it into the database.

## Dump the postgres database
The neo4j database is created from a set of CSV files generated from the Postgresql database. These csv files can be generated through the `scripts/migration/migrate.sh` script. Run the command:

```
scripts/migration/migrate.sh dump
```

This will generate csv files in the `data/pg4j_output` directory. This command may take some time to complete, depending on the size of the database being dumped. If it is working correctly, .csv files should start to appear in `data/pg4j_output`.

## Load the dump into neo4j

```Bash
docker-compose up pg4j
```

When this is completed, the message `mps-docker_pg4j_1 exited with code 0` should appear.

## Stop the Postgres container as it is no longer needed

```Bash
docker-compose down
```

## Start neo4j
```Bash
docker-compose up neo4j
```
