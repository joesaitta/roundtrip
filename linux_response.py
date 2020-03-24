"""
Template Linux process to execute via windows
"""
import argparse

def handle_windows_request(infile, outfile):
    # Crack open the infile, grab the date, and dump to a new file
    with open(infile, 'r') as f:
        lines = f.readlines()
    data = lines[0].split(' ')
    windows_host = data[3]
    write_date = data[5]

    with open(outfile, 'w') as f:
        f.write('Hooray, this file was created from a Windows ')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-win_cmd', type=str, help='Windows command')
    parser.add_argument('-outfile', type=str)

    args = parser.parse_args()
    # -win_cmd C:\Users\jsaitta\Documents\windows_process.bat
    # -outfile C:\Users\jsaitta\Documents\tempfile.txt
    execute_windows_process(args.win_cmd, args.outfile)
