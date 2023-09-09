# build_files.sh
echo "BUILD IS START NOW !...."
pip install -r requirements.txt
python3.11 manage.py collectstatic

echo "Python Migration is Start"
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput


echo "BUILD IS SUCCESSFUL !!"