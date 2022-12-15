#!/bin/sh 

DOWNLOAD_LINK=https://data.caltech.edu/records/4kk39-69x76/files/public_release_20221115.tar.gz?download=1
wget  $DOWNLOAD_LINK \
 -O ./data/releases/postgres/public_release.tar.gz