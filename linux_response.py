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
        f.write('Hooray, this file was created using Windows inputs\n')
        f.write('From {}\n'.format(windows_host))
        f.write(write_date)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-infile', type=str,)
    parser.add_argument('-outfile', default='/home/jsaitta/PycharmProjects'
                                            '/linux_to_windows/final_file.txt',
                        type=str)

    args = parser.parse_args()
    handle_windows_request(args.infile, args.outfile)