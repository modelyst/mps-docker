# Migration


## Restore backups
To restore a specific backup run the following command 

```Bash
POSTGRES_BACKUP_FILE=public_release_20230228_eigth.tar.gz docker-compose --profile postgres up
```

This will first start the postgres docker container then start a loading service that takes the backup file and loads it into the database.

## Dump the postgres database
The neo4j database is created from a set of CSV files generated from the Postgresql database. These csv files can be generated through the `scripts/migration/migrate.sh` script. Run the command:

```
scripts/migration/migrate.sh dump
```

This will generate csv files in the `data/pg4j_output` directory.

## load the dump into neo4j

```Bash
docker-compose up pg4j
```

## Start neo4j
```Bash
docker-compose up neo4j
```
