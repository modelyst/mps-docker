# mps-docker
A Docker based deployment for the Materials Provenance Store (MPS) Database


## Download File
The neo4j dump file must be downloaded before the database can be instantiated. The most recent upload can be found at the s3 location below
```
s3://modelyst.rw/neo4j_dumps/public-release-neo4j-Dec-1-2022-09-01-23.dump
```
To download this file locally please use the AWS CLI tool with the correct credentials configured for the following command:
```Bash
aws s3 --profile PROFILE cp s3://modelyst.rw/neo4j_dumps/public-release-neo4j-Dec-1-2022-09-01-23.dump ./data/releases/public_release.dump
```
## Load the database
Once the file has successfully been downloaded it can be loaded into the neo4j docker container volume with the following command:
```
docker-compose run --rm loader
```
If the name of the release dump file is different than `public_release.dump.` it can be configured by setting the `DUMP_FILE` environmental variable prior to loading
```Bash
BACKUP_FILE=foo.dump dc run --rm loader
```
## Start the servers
Once the database has succesfully been loaded the jupyter and neo4j servers can be turned on with a simple docker-compose up command
```
docker-compose up -d
```
`-d` is appended here to start the servers in detached mode to run the servers in the background. 
## Connecting to the servers
Once the servers are succesfully instantiated you can navigate to http://localhost:7777 to access the jupyter server.

Similarly, the neo4j database can be accessed through its web portal at http://localhost:7474 or directly from `cypher-shell` at http://localhost:7687. The neo4j desktop application can also be configured to connect to the server by creating a remote connection to http://localhost:7687 and providing the credential information of User: neo4j and any password (authentication is disabled in the docker containers).

