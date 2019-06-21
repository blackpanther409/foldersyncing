import ftplib
import os
from os import scandir
site_address = '127.0.0.1'          #master device ip address

# site_address = input('Enter the website:')

with ftplib.FTP(site_address) as ftp:
    print(ftp.getwelcome())
    print('33333333')
    ftp.login('admin','password')   #enter master device or site username and password
    #ftp.retrlines('LIST')
    print(f'current directory:{ftp.pwd()}')
    #ftp.dir()
    
    master_dir=input('masterdir:')   #enter master directory address
    ftp.cwd(master_dir)
    print('current directory:',ftp.pwd())
    ftp.dir()
    
    #master system's info
    files_master=ftp.nlst()
    print(files_master)

    #local system's info
    basepath=input('Enter path of backup file:')    #backup directory address

    files_backup=[]
    dir_entries = scandir(basepath)
    for entry in dir_entries:
        if entry.is_file():
            files_backup.append(entry.name)
    
    print(f'files in backup:{files_backup}')
    print(f'files in master:{files_master}')

    missing=[]   
    #comparing master and backup files
    for i in files_master:
      if i not in files_backup:
        missing.append(i)
    print(f'missing:{missing}')

    #getting missing files from master to backup
    for filename in missing:
      local_filename = basepath+'\\'+filename
      #print(filename)
      lf = open(local_filename, "wb")
      ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
      lf.close()
    
