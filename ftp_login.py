import ftplib

with ftplib.FTP() as ftp:

    # Set the debugging level.
    # The required argument level means:
    #     0: no debugging output (default)
    #     1: print commands and responses but not body text etc.
    #     2: also print raw lines read and sent before stripping CR/LF
    ftp.set_debuglevel(1)

    # - host: hostname to connect to (string, default previous host)  
    # - port: port to connect to (integer, default previous port)  
    # - timeout: the timeout to set against the ftp socket(s)  
    # - source_address: a 2-tuple (host, port) for the socket to bind  
    #   to as its source address before connecting.
    ftp.connect(host='10.211.55.29', port=21)

    # Get the welcome message from the server. (this is read and squirreled away by connect())
    welcome_message = ftp.getwelcome()
    print(f"\n{welcome_message}\n")

    # Login, default anonymous.
    # ftp.login(user='anonymous', passwd='myemail@email.com')

    # as anonymous login is the default you can change line 24 with this:
    ftp.login()