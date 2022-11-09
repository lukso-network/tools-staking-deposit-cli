#!/usr/bin/env bash
sed -i.bak -e "s#^DEPOSIT_CLI_VERSION\s*=\s*'\([^']*\)'\(.*\)\$#DEPOSIT_CLI_VERSION = '$1'\2#" staking_deposit/settings.py
rm -f staking_deposit/settings.py.bak
echo "$1" > .DEPOSIT_CLI_VERSION

