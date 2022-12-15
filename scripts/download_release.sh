#!/bin/sh 

echo "Downloading Postgres Release from Caltech data..."
DOWNLOAD_LINK=https://data.caltech.edu/records/4kk39-69x76/files/public_release_20221115.tar.gz?download=1
wget  $DOWNLOAD_LINK \
 -O ./data/releases/postgres/public_release.tar.gz

echo "Downloading Neo4j release from S3..."
PROFILE=${PROFILE:-default}
aws s3 --profile $PROFILE cp s3://modelyst.rw/neo4j_dumps/public-release-neo4j-Dec-1-2022-09-01-23.dump ./data/releases/public-release.dump