# Building a live dashboard

In this challenge you build an almost real-time data pipeline that regularily extracts data from a public API and stores it in a database.


### Task 1: Inspect the file `store_info.py`

1. Bring the statements into the correct order.
2. Find out what the script is doing!
3. Fill in the `????`


### Task 2: Test the script locally

1. Fill in a valid database `uri`.
2. Test the script locally.
3. Check that the data stored in your database!


### Task 3: Setup a python environment on the server

1. Connect to your remote machine with `ssh`.
2. On the remote machine, download the miniconda installer:
   ```
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```
3.  Install miniconda by exectuting the installation script:
      ```
      bash Miniconda3-latest-Linux-x86_64.sh
      ```
      Follow the prompts on the installer screens. If you are unsure about any setting, accept the defaults. You can change them later.
      
4.  Type in `~/miniconda3/bin/conda init` to initialize conda.
   
5. Restart the terminal and connect to the server again. 
6. Check if the installation was successful by typing in `which python`. This should show you the path `/home/ubuntu/miniconda3/bin/python`
7. Using `pip`, install the required packages `beautifulsoup4`, `pandas`, `sqlalchemy`, `lxml`, `psycopg2-binary` and `requests` (you also find them in the `requirements.txt`).


### Task 4: Copy the script to the server and test it

1. From your local machine, use the `scp` command, copy `store_info.py` from your local machine to the server:
   ```
   scp -i ~/.ssh/mykey.pem ./store_info.py ubuntu@hostname:/home/ubuntu/store_info.py
   ```
2. Connect to your remote machine with `ssh` and check if the script is in the home directory of your server.
3. Check that the script also runs on the remote machine!
   - you might have to install a german locale, type in: `sudo locale-gen "de_DE.UTF-8"`


### Task 5: Setup a Cronjob (https://crontab.guru/)

1. Type in `crontab -e`. This will open the `nano` text editor and allows you to edit your cron jobs.
2. Add a line to the crontab:
   ```
   */5 * * * * /home/ubuntu/miniconda3/bin/python ~/store_info.py > ~/log.log  2>&1
   ```   
3. Save and exit the `nano` text editor. 
4. Check that the log output is written to a file `log.log` in the server's home directory. 


### Cronjobs

- What means the code `*/5 * * * *`?
- What is happening if you type in `/home/ubuntu/miniconda3/bin/python ~/store_info.py`
- What means the line `> ~/log.log  2>&1`?





