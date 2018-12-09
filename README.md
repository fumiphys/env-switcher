# env-switcher
Context manager for environmental variables.

# usage
```
# enable command
source env_switcher.sh

# initialize context
swenv context init [context_name]

# edit context info
swenv context edit [context_name] [info_name] [info_value]

# add env field to context
swenv context update [context_name] [field_name] [field_value]

# copy context
swenv context cp [from_context_name] [to_context_name]

# get list of contexts
swenv context list
```
