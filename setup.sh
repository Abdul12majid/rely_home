echo 'pick a directory name for set-up: '
read dir_name
mkdir $dir_name
cd $dir_name
git clone https://github.com/Abdul12majid/rely_home.git .
pip install /-r requirements.txt
echo "set-up done, kindly go into the folder and run the command - 'python main.py' to run the main code or 'python test.py' to test run."
echo "each code requires an active url to work, one for the job accept(main.py) and another to select day and time(test.py)"