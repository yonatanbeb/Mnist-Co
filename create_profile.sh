#!/bin/bash

python create_profile.py $1 $2 $3
# sign_in with created profile
sign_in $1 $2