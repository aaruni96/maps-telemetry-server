# MaPS Telemtry Server

This program listens for when an installation of MaPS reports in with details
of the runtime its about to download, and the remote its about to download from.

## Installation

In a python virtual environment, install all the requirements from
`requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Set up a reverse proxy which takes `/ping` and forwards it to the application on
`127.0.0.1:8080/ping`.

## Usage

Run the program with

```bash
fastapi run --host 127.0.01 --port 8080 --forwarded-allow-ips 127.0.0.1
```
