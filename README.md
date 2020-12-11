It's a simple python script to delete the oldest MySQL backup in the EC2

## BACKUP

MySQL backup is taken in the following format under directory `~/mysql/backup/`

    wordpress-$(date +%Y-%m-%d-%H.%M.%S).sql

## USAGE

Script is used with arguments

    oldbackup.py <ip> <user> <port>/(default=22)
