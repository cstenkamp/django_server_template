# Django Server

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI/CD - Master](https://github.com/OWNER/REPO/actions/workflows/test_docker_publish.yml/badge.svg?branch=master)](https://github.com/OWNER/REPO/actions/workflows/test_docker_publish.yml)


This repository contains the code for a backend server with Django.

## How to use this template

* For all `*.md`-files, replace `OWNER` with the owner of the repo you're using this template as, `REPO` with the name of the repo, and `ENV_NAME` with the name of the conda-env you want to run this in.
* For the `docker`-directory and in `howto_docker.md`, replace `PROJECT_NAME` with the name of your project
* In `docker/docker-compose.yml`, as well as `src/settings/settings_base.py` add your values for `POSTGRES_DB`, `POSTGRES_USER` and `POSTGRES_PASSWORD` (where there's `<your_value_here>`)
* If you want to run a tf-serving instance, you can un-comment the `tf_serving` section in `docker/docker-compose.yml` and the line that creates the directory in `docker/docker_run_linux.sh`. You'll also  need to replace `PROJECT_NAME` in `src/apps/backend/util/tf_model_server.py` with the name of your Project and `<your_tfserving_modelname>` with the name of the model in all places it occurs. Then you can use the stuff in `src/apps/backend/sample_tfserving.py`, `src/test/test_base_tfserving.py` and `src/apps/backend/util/tf_model_server.py`. If you don't, just remove all that.

## Installing

There are two ways of installing this project: Either using Docker-Compose, or manually. The former means that you don't have to install all components on your local system, but can instead simply install `docker` and `docker-compose`, and then set up the container inside docker. If you are not already deep into the technology stack of this project, this is the recommended way. Note that if you want to contribute to this project, you should still install a few requirements for static-code-checking upon commits.

The second possibility is to install everything (including `conda` and `postgresql`) manually on your computer. This way takes longer and is more error-prone than the first way, but allows for more customization and easier debugging.

Next to the distinction of installing using Docker or not, another distinction is if you want to install *productively* or *for development*. If you want to set this up on a productive server, the settings and the way this Django-Project is invoked differ. In this project, different `docker-compose.yml`-files allow for setting this project up correctly both for developers and for productive serving, such that setting up this project on a fresh VM can be done using only a single command.

**For the complete guide on how to install/set up this project, see [doc/install.md](https://github.com/OWNER/REPO/blob/master/doc/install.md)**


## Contributing

If you want to contribute, you can still run everything inside the docker-container. However, we are using `pre-commit` with linting hooks, such as `black` and `flake8`.

**Please read the file [doc/readme_developer.md](https://github.com/OWNER/REPO/blob/develop/doc/readme_developer.md) for instructions on how to set these up**.
