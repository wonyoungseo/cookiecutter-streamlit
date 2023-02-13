# Cookiecutter Streamlit

> Cookiecutter template for Streamlit app

## 1. Prerequisite

1. Python must be installed on your OS
2. Cookiecutter must be installed

[Reference guide](https://cookiecutter.readthedocs.io/en/2.1.1/installation.html#)

## 2. Generate Streamlit project via `cookiecutter`

Command can be either one of the followings;

```bash
# With URL
$ cookiecutter https://github.com/wonyoungseo/cookiecutter-streamlit.git

# With Github user name and repository name
$ cookiecutter gh:wonyoungseo/cookiecutter-streamlit
```

## 3. Run Streamlit app

```bash
# With pip
$ pip install -r requirements.txt
$ streamlit run app.py
```

```bash
# With Docker
$ docker build -t streamlit_app .
$ docker run -rm  -p 8501:8501 streamlit_app
```
