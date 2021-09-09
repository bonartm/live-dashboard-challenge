# Building a live dashboard

In this challenge you build an almost real-time data pipeline that regularily extracts data from a public API and stores it in a database.

### Task 1: Inspect the file `pegel.py`

1. Fill in a valid database `uri` that points to your AWS database.
2. Test the script locally with `python pegel.py`.
3. Find out what the script is doing!
4. Check that some data was stored in your remote database!

### Task 2: Copy the script to the server

1. From your local machine, use the `scp` command to copy the project from your local machine to the server:
   ```
   scp -r -i ~/.ssh/aws_key.pem ../live-dashboard-challenge/ ubuntu@<hostname/ip>:/home/ubuntu/
   ```
2. Connect to your remote machine with `ssh` and check if the folder is in the home directory of your server:
   ```
   cd live-dashboard-challenge
   ```

### Task 4: Install the libraries on the server

1. Check if python is installed by typing in `which python3`. This should show you the path `/usr/bin/python3`
2. Install `pip3` with `sudo apt install python3-pip`
3. Use `pip3` to install the required python packages that are listed in the `requirements.txt`:
   ```
   pip3 install -r requirements.txt
   ```
4. install a german locale, type in: `sudo locale-gen "de_DE.UTF-8"`
5. Test the script on the remote machine
   ```
   python3 pegel.py
   ```

### Task 5: Setup a Cronjob (https://crontab.guru/)

1. Type in `crontab -e`. This will open the `nano` text editor and allows you to edit your cron jobs.
2. Add a line to the crontab:
   ```
   * * * * * /usr/bin/python3 ~/live-dashboard-challenge/pegel.py >> ~/live-dashboard-challenge/pegel.log 2>&1
   ```
3. Save and exit the `nano` text editor.
4. Check that the log output is written to a file `pegel.log` in the server's home directory.
