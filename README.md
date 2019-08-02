# JupyterHub tokenauthenticator - A JWT Token Authenticator for JupyterHub

Authenticate to Jupyterhub using a query parameter for the JSONWebToken, or by an authenticating proxy that can set the Authorization header with the content of a JSONWebToken.

This is a fork from [the github repo](https://github.com/mogthesprog/jwtauthenticator) with some changes.
Admin status is now derived from the user's roles defined in the token - specifically the 'katana-admin' role.

## Installation

clone this repository and run:

```bash
cd jwtauthenticator
pip install -e .
```

## Configuration

A jupyterhub config file `jupyterhub_config.py` which sets the necessary values can be found in this fork - for more details on the different attributes and options look at the original repo's [ReadMe](https://github.com/mogthesprog/jwtauthenticator/blob/master/README.md).

JupyerHub can be run locally using this file by calling

```bash
jupyterhub -f path/to/repo/jupyterhub_config.py 
```
