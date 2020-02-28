import subprocess
import datetime
import re

import argparse

def write_result(filename, ping):
	with open(filename, "w") as f:
		f.write(f"Start time {datetime.datetime.now()}")
		for result in ping:
			f.write(result)
		f.write(f"End time {datetime.datetime.now()}")

def ping_subnet(subnet):
	for addr in range(1, 255):
		yield subprocess.Popen(["ping", f"{subnet}.{addr}", "-n", "1"], stdout=subprocess.PIPE) \
			.stdout.read()									\
			.decode()							

def main(subnet, filename):
	write_result(filename, ping_subnet(subnet))

def parse_arguments():
	parser = argparse.ArgumentParser(usage='%(prog)s [options] <subnet>',
					 description='ip checker', 
					 epilog = "python ipscanner.py 192.168.1 -f somefile.txt")
	parser.add_argument('subnet', type=str, help='the subnet you want to ping')
	parser.add_argument('-f', '--filename', type=str, help='The filename')
