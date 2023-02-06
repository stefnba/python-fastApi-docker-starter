# python-fastApi-docker-starter
Starter template for Python 🐍 and FastAPI with Docker.


# Get Started

Run the following commands to create a virtual environment called `env`, activate it and install packages listed in `requirements.txt`.

```console
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -U black
pip install -r requirements.txt
```

Start server
```console
uvicorn src/main:app --reload
```



# Save packages

```console
pip freeze > requirements.txt
```