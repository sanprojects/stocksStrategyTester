#!/usr/bin/env bash

#set -o errexit
set -o pipefail
set -o nounset
# set -x # show running commands

usage() {
    echo "Usage: $0 COMMAND" >&2
    echo "Commands:"
    declare -F | sed "s/declare -f/ /g"
}

install() {
    pip3 install --upgrade -r requirements.txt
}

updateRequirements() {
  pip3 freeze > requirements.txt && cat  requirements.txt
}

run() {
  python3 run.py bots/buyFallen.py start=2020-01-01 end=2020-09-30 ticker=AAPL
}

tests() {
  pytest
}


${1:-usage} || usage