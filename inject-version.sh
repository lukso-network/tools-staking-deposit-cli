#!/usr/bin/env bash
if [ -n "$1" ]
then
    sed -i.bak -e "s#^DEPOSIT_CLI_VERSION\s*=\s*'\([^']*\)'\(.*\)\$#DEPOSIT_CLI_VERSION = '$1'\2#" staking_deposit/settings.py
    sed -i.bak -e "s#version='\([^']*\)',#version='$1',#" ./setup.py

    rm -f ./setup.py.bak staking_deposit/settings.py.bak
    VERSION=$1
else
    VERSION=$2
fi

if [ -n "$GITHUB_OUTPUT" ]
then
    echo "VERSION=$VERSION" >> $GITHUB_OUTPUT
fi
