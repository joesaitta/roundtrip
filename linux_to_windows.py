"""
Template Linux process send an ssh command to Windows

Assumes that both client (Linux) and host (Windows) systems have ssh private
key authentication set up. This pulls the USERNAME and HOST name from
environment variables and executes a batch file on the Windows side.
"""
import datetime
import argparse
import subprocess
import os

FMT = '%Y-%m-%d %H:%M:%s'
# User credentials for the Windows machine, in the deployed version, we'll need
# a system key that can be grabbed in the environment
USERNAME = os.getenv('SSH_USER')
WINHOST = os.getenv('WINDOWS_HOST')
LINUXHOST = os.getenv('HOSTNAME')


def execute_windows_process(win_cmd, outfile):
    # Fill in the arguments for ssh and the command to execute on Windows
    kwargs = {'user': USERNAME,
              'host': WINHOST,
              'proc': win_cmd,
              'client': LINUXHOST,
              'outfile': outfile}
    cmd_str = 'ssh {user}@{host} "{proc} {client} {outfile}"'.format(**kwargs)
    print(cmd_str)
    return subprocess.check_call(cmd_str, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-win_cmd', type=str, help='Windows command')
    parser.add_argument('-outfile', type=str)

    args = parser.parse_args()
    # -win_cmd C:\Users\jsaitta\Documents\windows_process.bat
    # -outfile C:\Users\jsaitta\Documents\tempfile.txt

    execute_windows_process(args.win_cmd, args.outfile)