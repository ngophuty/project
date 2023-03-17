#!/usr/bin/env python3
import sys
import os
import shutil
from subprocess import call as subprocess_call

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IS_ROOT = os.getenv('root') is not None
ARGS = sys.argv[1:]
ENV_DOCKER = os.path.join(ROOT_PATH, "config/.docker")
PROJECT = os.path.basename(ROOT_PATH).lower()

APP = ARGS[0] if len(ARGS) > 0 else None
COMMAND = ARGS[1] if len(ARGS) > 1 else None
ARGS = ARGS[2:]

os.chdir(ROOT_PATH)

def call(*args, env=None):
    cmd = " ".join(map(lambda s : f'"{s}"' if " " in s else s, map(str, args)))
    print(cmd)
    environ = os.environ.copy()
    if env:
        environ.update(env)
    subprocess_call(cmd, shell=True, env=environ)

def docker_compose(*args, env=None):
    call("docker", "compose", "--env-file", ENV_DOCKER, "-p", PROJECT, *args, env=env)

def getuid():
    return 0 if IS_ROOT else os.getuid()

if APP not in ["yarn", "app", "node", "docker", "init"]:
    subprocess_call("cat _documents/help_content.md", shell=True)
    sys.exit(0)

if APP == "init":
    if not os.path.exists("config/.docker"):
        print("Docker environment file (config/.docker) not found. Generating...\n")
        shutil.copy("config/_docker", "config/.docker")
        print("'config/.docker' is added to your project. You may want to update this file manually.\n\n")

    if not os.path.exists("config/.env"):
        print("Environment file (config/.env) not found. Generating...\n")
        shutil.copy("config/_env", "config/.env")
        print("'config/.env' is added to your project. You may want to update this file manually.\n\n")

if APP == "app":
    if COMMAND == "install":
        COMMAND = "pip-install"

    if COMMAND in ["serve", "start", "stop", "restart", "status"]:
        if COMMAND in ["serve", "start", "stop", "restart", "status"]:
            IS_ROOT = True
        docker_compose("exec", "--user", getuid(), "app", "cmd", COMMAND, *ARGS)
    else:
        docker_compose("exec", "--user", getuid(), "app", COMMAND, *ARGS)

if APP in ["yarn", "node"]:
    docker_compose("exec", "--user", getuid(), "node", "yarn", COMMAND, env={"USER_ID" : str(os.getuid())})

if APP == "docker":
    if COMMAND == "up":
        if len(ARGS) == 0:
            ARGS.append('-d')
        if "--fg" in ARGS:
            ARGS.remove("--fg")

    if COMMAND == "logs":
        if len(ARGS) == 0:
            ARGS.append('app')
        if "-f" in ARGS:
            ARGS.remove("-f")
        ARGS.insert(0, '-f')

    if COMMAND in ["build", "rebuild"]:
        docker_compose(COMMAND, env={"USER_ID" : str(os.getuid())})
    else:
        docker_compose(COMMAND, *ARGS)