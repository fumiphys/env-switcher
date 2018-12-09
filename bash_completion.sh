#!/bin/bash

# completion for bash
_swenv_bash() {
  local opts cur prev
  opts="context config"
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"

  case "${prev}" in
    "config" )
      COMPREPLY=( $(compgen -W "get set" ${cur}) )
      return 0
      ;;
    "context" )
      COMPREPLY=( $(compgen -W "list init edit update cp activate print" ${cur}) )
      return 0
      ;;
  esac
    
  COMPREPLY=( $( \
    compgen -W "${opts}" \
    ${cur} \
    ) )
}

complete -F _swenv_bash swenv
