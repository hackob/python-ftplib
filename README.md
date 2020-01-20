# python-ftplib
Usage and examples of python ftplib

# Login and welcome message 
`ftp_login.py`

## Output
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