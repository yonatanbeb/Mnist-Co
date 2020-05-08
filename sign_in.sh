#!/bin/bash

python sign_in.py $1 $2
# update command line prompt
PS1="$(</home/yonatan/PycharmProjects/Mnist\&Co/session_data/prompt)"