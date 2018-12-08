#!/bin/bash

# args:
#   list: list all context
#   init: initialize context
#   edit: update context value
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
      python3 context.py edit "$2" "$3" "$4"
esac
}

# args:
#   context
swenv() {
  case "$1" in
    "context" ) context_func ${@:2} ;;
esac
}
