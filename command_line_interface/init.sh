#!/bin/bash

alias sign_in=". ./sign_in.sh"
alias sign_out=". ./sign_out.sh"
alias create_profile=". ./create_profile.sh"
alias grab="python ./grab.py"
alias query="python ./query.py"
alias browse=". ./browse.sh"

sign_out
echo {} > ./session_data/profiles.json
echo "[\"No Clearance\", \"Guest\"]" > ./session_data/surfer.json