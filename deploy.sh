python3 -m venv env
source env/bin/activate
pip3 install poetry
poetry install
python3 manage.py migrate
python3 manage.py collectstatic --no-input
deactivate