#!/usr/bin/env python3
import os, sys
from subprocess import call as subprocess_call

ARGS = sys.argv[1:]
ARGS = [arg if len(arg.split()) == 1 else f'"{arg}"' for arg in ARGS]

COMMAND = ARGS[0] if len(ARGS) > 0 else None
ARGS = ARGS[1:]

if __name__ == "__main__":

    PYTHON = "/src/.cache/.virtualenv/bin/python3"
    if COMMAND == "serve":
        PORT = 8000
        if ARGS:
            PORT = ARGS[0]
        print(f'/src/.cache/.virtualenv/bin/uvicorn app:app --host "0.0.0.0" --port {PORT} --reload')
        subprocess_call(f'/src/.cache/.virtualenv/bin/uvicorn app:app --host "0.0.0.0" --port {PORT} --reload', shell=True, cwd="/src/backend/")
    elif COMMAND in ["status", "start", "stop", "restart"]:
        SERVICES = "all"
        if ARGS:
            SERVICES = " ".join(ARGS)
        subprocess_call(f"supervisorctl {COMMAND} {SERVICES}", shell=True)

    elif COMMAND == "db":
        COMMAND = ARGS[0]
        ARGS = ARGS[1:]

        os.chdir("/src/alembic/")
        if COMMAND in ["revision", "auto", "autorevision"]:
            command = "revision" if COMMAND in ["revision"] else "revision --autogenerate"
            subprocess_call(f"/src/.cache/.virtualenv/bin/alembic {command} {f'-m {ARGS[0]}' if ARGS else ''}", shell=True)

        if COMMAND in ["upgrade", "migrate", "downgrade"]:
            command = "upgrade" if COMMAND in ["upgrade", "migrate"] else "downgrade"
            subprocess_call(f"/src/.cache/.virtualenv/bin/alembic {command} {ARGS[0] if ARGS else ''}", shell=True)

        if COMMAND in ["list", "history"]:
            subprocess_call(f"/src/.cache/.virtualenv/bin/alembic history {ARGS[0] if ARGS else ''}", shell=True)