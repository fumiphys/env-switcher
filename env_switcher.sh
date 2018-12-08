#!/bin/bash

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
esac
}

swenv() {
  case "$1" in
    "context" ) context_func ${@:2} ;;
esac
}
