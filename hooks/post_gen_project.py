import os

if "{{ cookiecutter.use_docker }}" == "False":
    os.remove(os.path.join(os.getcwd(), "Dockerfile"))