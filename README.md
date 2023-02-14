# Cookiecutter Streamlit

> Cookiecutter template for Streamlit app

![](https://github.com/wonyoungseo/cookiecutter-streamlit/blob/main/images/example_app_screenshot.png)

## 0. Prerequisite

1. Python must be installed on your OS
2. Cookiecutter must be installed

[Reference guide on installation](https://cookiecutter.readthedocs.io/en/2.1.1/installation.html#)

## 1. Project template structure

```text
.
├── README.md
├── .streamlit
├── app.py
├── sub_pages  # <-- your development starting point 
│   ├── __init__.py
│   ├── _page_base.py
│   ├── page_main.py
│   ├── page_1.py
│   └── page_2.py
├── utils
│   ├── __init__.py
│   └── utils.py
├── requirements.txt
├── Dockerfile
└── .gitignore
```

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
