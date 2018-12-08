#!/bin/bash

context_func() {
  if [ "$1" = "list" ]; then
    python3 context.py context list
  fi
}

swenv() {
  if [ "$1" = "context" ]; then
    context_func "$2"
  fi
}
