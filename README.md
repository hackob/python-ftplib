# python-ftplib
Usage and examples of python ftplib

# Login and welcome messge 
`ftp_login.py`

## Ouput
```
$ python3 ftplib/ftp_login.py
*resp* "220 Welcome to FTP service, python's ftplib is working!!!."
*welcome* "220 Welcome to FTP service, python's ftplib is working!!!."

220 Welcome to FTP service, python's ftplib is working!!!.

*cmd* 'USER anonymous'
*resp* '331 Please specify the password.'
*cmd* 'PASS **********'
*resp* '230 Login successful.'
*cmd* 'QUIT'
*resp* '221 Goodbye.'
```