import pysftp
import posixpath
import sys
import ipaddress

usage = 'oldbackup.py <ip> <user> <port>/(default=22)'
sqlist = []

if len(sys.argv) == 4:
    sftp_host = sys.argv[1]
    sftp_user = sys.argv[2]
    sftp_port = sys.argv[3]
elif len(sys.argv) == 3:
    sftp_host = sys.argv[1]
    sftp_user = sys.argv[2]
    sftp_port = 22
else:
    print(usage)

sftp_keyfile = 'project.pem'
if ipaddress.ip_address(sftp_host) and str(sftp_port).isdigit():
    sftp = pysftp.Connection(host=sftp_host,port=sftp_port,username=sftp_user,private_key=sftp_keyfile)
    sftp.chdir('mysql/backup')
    wplist = sftp.listdir()
    if wplist:
        for sql in wplist:
            if sql.endswith('.sql'):
                sqlist.append(sql)
        else:
            print('No SQL backups found..!!!')
            exit()
        def time(wp):
            return wp.split('-',1)
            
        oldest = sorted(sqlist,key=time)[0]
        print('oldest backup is : ',posixpath.join(sftp.pwd,oldest))
            
        sftp.remove(oldest)
        print('Removed the oldest backup...', oldest)
    else:
        print('Directory is empty...!!!')
else:
    print('Connection Error...!!!\n',usage)
