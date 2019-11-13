#CONFIG
host = 'test.rebex.net'
port = 22
username = 'demo'
password = 'password'
source_path='pub/example'
target_path='./'

import os
import paramiko
from stat import S_ISDIR

#paramiko.util.log_to_file('/tmp/paramiko.log')
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
def sftp_walk(remotepath):
    path=remotepath
    files=[]
    folders=[]
    for f in sftp.listdir_attr(remotepath):
        if S_ISDIR(f.st_mode):
            folders.append(f.filename)
        else:
            files.append(f.filename)
    if files:
        yield path, files
    for folder in folders:
        new_path=os.path.join(remotepath,folder)
        for x in sftp_walk(new_path):
            yield x


for path,files  in sftp_walk(source_path):
    for file in files:
        #sftp.get(remote, local) line for dowloading.
        sftp.get(os.path.join(os.path.join(path,file)), taget_path+file)
        