# CONFIG
server='test.rebex.net'
port=22
user='demo'
pwd='password'

import sys
import logging
logging.basicConfig(level=logging.DEBUG)

if sys.argv[1]=='ftplib':
    from ftplib import FTP
    logging.info("Creo oggetto FTP...")
    f=FTP()
    logging.info("Oggetto FTP creato!")
    logging.info("Provo a connettermi...")
    f.connect(host=server, port=21)
    logging.info("Connessione riuscita!")
    logging.info("Provo a loggarmi...")
    f.login(user,pwd)
    logging.info("Sono dentro!")
    logging.info("Lista file e cartelle:")
    #f.cwd('pub/example')
    f.retrlines('LIST')
    #with open('ConsoleClient.png', 'wb') as fp:
    #    f.retrbinary('RETR ConsoleClient.png', fp.write)
    f.quit()
else:
    import paramiko
    
    logging.info("Provo a connettermi...")
    transport = paramiko.Transport((server, port))
    logging.info("Connessione riuscita!")
    logging.info("Provo a loggarmi...")
    transport.connect(username=user,password=pwd)
    logging.info("Sono dentro!")
    logging.info("Lista file e cartelle:")
    sftp = paramiko.SFTPClient.from_transport(transport)
    lista=sftp.listdir_attr()
    for item in lista:
        print(item)
    #sftp.get('pub/example/ConsoleClient.png', './CC.png')
    sftp.close()
    transport.close()