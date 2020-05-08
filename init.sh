#!/bin/bash

# create shortcuts for all interface commands
alias sign_in=". ./sign_in.sh"
alias sign_out=". ./sign_out.sh"
alias create_profile=". ./create_profile.sh"
alias grab="python ./grab.py"
alias query="python ./query.py"
alias browse=". ./browse.sh"
alias cart="python ./cart.py"

# initially sign_out (= sign_in as Guest with no clearance level)
sign_out
# initialize values in JSON files
echo {} > ./session_data/profiles.json
echo "[\"No Clearance\", \"Guest\"]" > ./session_data/surfer.json