compdef _swenv_zsh swenv

function _swenv_zsh {
  local -a cmds
  _arguments \
    '1: :->first' \
    '*: :->args'

  case $state in
    args )
      case "$words[2]" in
        config )
          _values "" "get" "set"
          ;;
        context )
          _values "" "list" "init" "edit" "update" "cp" "activate" "print"
          ;;
        * )
          _files
          ;;
      esac
      ;;
    first )
      _values "" "config" "context"
      ;;
    * )
      _files
      ;;
  esac
}
