#!/bin/sh 

echo "Downloading Postgres Release from Caltech data..."
DOWNLOAD_LINK=https://data.caltech.edu/records/hjfx4-a8r81/files/public_release_20230228.tar.gz?download=1
wget  $DOWNLOAD_LINK \
 -O ./data/releases/postgres/public_release.tar.gz

echo "Downloading Neo4j release from S3..."
PROFILE=${PROFILE:-default}
DOWNLOAD_LINK=https://data.caltech.edu/records/h88fq-dk449/files/public-release-neo4j-20230228.dump?download=1
wget  $DOWNLOAD_LINK \
 -O ./data/releases/neo4j/neo4j.dump