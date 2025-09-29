'''
Small fastAPI application to listen to anonymous telemetry for MaPS and to write
it to a CSV file for later analysis.
'''
from os import path
from typing import Annotated
from fastapi import FastAPI, Form

if not path.isfile("stats.log"):
    with open("stats.log", 'w', encoding='ascii') as initfile:
        initfile.write("reponame, repourl, runtime\n")

app = FastAPI()

@app.post("/ping")
def get_ping(
        reponame: Annotated[str, Form()],
        repourl: Annotated[str, Form()],
        runtime: Annotated[str, Form()]
    ):
    """
    Get reponame, repourl, and runtime as an `application/x-www-form-urlencoded`
    and write to file (also return, for some reason?).
    """
    with open('stats.log', 'a', encoding='ascii') as statsfile:
        statsfile.write(f"{reponame}, {repourl}, {runtime}\n")
    return {'reponame': reponame, 'repourl': repourl, 'runtime': runtime}
