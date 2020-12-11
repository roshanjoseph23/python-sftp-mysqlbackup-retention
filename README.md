It's a simple python script to delete the oldest MySQL backup in the EC2

## Prerequisites

 - EC2 ip
 - key pair for EC2 access
 - EC2 sftp user
 - EC2 sftp port

## BACKUP

MySQL backup is taken in the following format under directory `~/mysql/backup/`

    wordpress-$(date +%Y-%m-%d-%H.%M.%S).sql

## USAGE

Script is used with arguments

    oldbackup.py <ip> <user> <port>/(default=22)

## Sample Output

    oldest backup is :  /home/ec2-user/mysql/backup/wordpress-2020-12-11-15.18.33.sql
    Removed the oldest backup... wordpress-2020-12-11-15.18.33.sql
