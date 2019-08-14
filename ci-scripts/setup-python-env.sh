#!/usr/bin/env bash

mkdir -p $HOME

cat > $HOME/.pypirc <<EOF
    [distutils]
    index-servers=pypi

    [pypi]
    repository = https://nexus3.usu-research.ml/repository/pypi-internal/
    username = deployment
    password = ${NEXUS_DEPLOYMENT_PASSWORD}
EOF
