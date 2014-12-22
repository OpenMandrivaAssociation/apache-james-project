#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: ./create-tarball VERSION"
    exit 1
fi

VERSION=${1}
NAME="james-project"

wget http://repo1.maven.org/maven2/org/apache/james/${NAME}/${VERSION}/${NAME}-${VERSION}-source-release.zip
unzip ${NAME}-${VERSION}-source-release.zip
rm ${NAME}-${VERSION}-source-release.zip
# remove site - it contains bundled javascript project galleria (MIT license not included)
rm -Rf ./${NAME}-${VERSION}/src/*
tar czvf ${NAME}-${VERSION}-clean.tar.gz ./${NAME}-${VERSION}

