# Building a live dashboard

In this challenge you build an almost real-time data pipeline that regularily extracts data from a public API and stores it in a database.


### Task 1: Inspect the file `store_info.py`

1. Bring the statements into the correct order.
2. Find out what the script is doing!
3. Fill in the `????`


### Task 2: Test the script locally

1. Fill in a valid database `uri`.
2. Test the script locally.
3. Is the data stored in the database?


### Task 3: Setup a python environment on the server

1. Connect to your remote machine with `ssh`.
2. On the remote machine, download the miniconda installer:
   ```
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```
3.  Install miniconda:
   ```
   bash Miniconda3-latest-Linux-x86_64.sh
   ```
   Follow the prompts on the installer screens. If you are unsure about any setting, accept the defaults. You can change them later.
   
4. Restart the terminal and connect to the server. 
5. Check if the installation was successful by typing in `which python`. This should show you the path `/home/ubuntu/miniconda3/bin/python`
6. Using `pip`, install the required packages `beautifulsoup4`, `pandas`, `sqlalchemy` and `requests`


### Task 4: Copy the script to the server and test it

1. With the `scp` command, copy `store_info.py` from your local machine to the server:
   ```
   scp -i ~/.ssh/mykey.key store_info.py ubuntu@hostname:/home/ubuntu/store_info.py
   ```
2. Connect to your remote machine with `ssh` and check if the script is also running on your server!


### Task 5: Setup a Cronjob (https://crontab.guru/)

1. Type in `crontab -e`. This will open the `nano` text editor and allows you to edit your cron jobs.
2. Add a line to the crontab:
   ```
   */5 * * * * /home/ubuntu/miniconda3/bin/python ~/store_info.py > ~/log.log  2>&1
   ```
3. Save and exit the `nano` text editor. 
4. Check that the log output is written to a file `log.log` in the server's home directory. 

