import pysftp
import posixpath
import sys
import ipaddress

usage = 'oldbackup.py <ip> <user> <port>/(default=22)'

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
try:
    if ipaddress.ip_address(sftp_host) and str(sftp_port).isdigit():
        sftp = pysftp.Connection(host=sftp_host,port=sftp_port,username=sftp_user,private_key=sftp_keyfile)
        sftp.chdir('mysql/backup')
        wplist = sftp.listdir()
        def time(wp):
            return wp.split('-',1)
        
        oldest = sorted(wplist,key=time)[0]
        print('oldest backup is : ',posixpath.join(sftp.pwd,oldest))
            
        sftp.remove(oldest)
        print('Removed the oldest backup...', oldest)
except:
    print(usage)
