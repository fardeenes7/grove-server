#build_files.sh

pip install -r requirements.txt
./manage.py collectstatic --noinput
