#!/bin/bash

python -c 'import secrets; print(secrets.token_hex())' | tee MEGA_SECRET_HYPER_PASSWORD
