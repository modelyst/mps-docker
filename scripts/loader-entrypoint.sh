#!/usr/bin/env bash
neo4j-admin \
    load \
    --database=neo4j \
    --from=/releases/${BACKUP_FILE:-public-release.dump} \
    --force