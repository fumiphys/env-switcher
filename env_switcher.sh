#!/bin/bash

# args:
#   list: list all context
#   init: initialize context
#   edit: update context value
#   update: update context fields
#   cp: copy context
context_func() {
  case "$1" in
    "list" )
      if [ $# -ne 1 ]; then
        echo "invalid argument: ${@:2}"
        return 1
      fi
      python3 context.py list
      ;;
    "init" )
      if [ $# -ne 2 ]; then
        echo "context init requires exactly one argument."
        return 1
      fi
      python3 context.py init "$2"
      ;;
    "edit" )
      if [ $# -ne 4 ]; then
        echo "context edit requires exactly three argument."
        return 1
      fi
      python3 context.py edit "${@:2}"
      ;;
    "update" )
      if [ $# -lt 4 -o $# -gt 5 ]; then
        echo "context update requires three or four argument"
        return 1
      fi
      python3 context.py update "${@:2}"
      ;;
    "cp" )
      if [ $# -ne 3 ]; then
        echo "context cp requires exactly two arguments"
        return 1
      fi
      python3 context.py cp "${@:2}"
      ;;
esac
}

# args:
#   context
swenv() {
  case "$1" in
    "context" ) context_func ${@:2} ;;
esac
}
