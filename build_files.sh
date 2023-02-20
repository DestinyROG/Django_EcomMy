
echo "BUILD START"
python3.11.1 -m pip install -r requirments.txt
python3.11.1 manage.py collectstatic --noinput --clear
echo "BUID END"