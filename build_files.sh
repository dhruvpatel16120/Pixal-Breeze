# build_files.sh
echo "BUILD IS START NOW !...."
pip install -r requirements.txt
python3.9 manage.py collectstatic

echo "Python Migration is Start"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput


echo "BUILD IS SUCCESSFUL !!"