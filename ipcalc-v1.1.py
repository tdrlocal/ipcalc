##!/usr/bin/env python
 
import ipcalc
from ipcalc import *
from netaddr import *
import sys
 
def how_to():
	print '\nIPCalc V1.1 - tdr.local[@]gmail.com '
	print '-----------------------------------------'
	print 'Usage: ipcalc [-s|-v] <ADDRESS>/<NETMASK>\n -s \t Summary of ipcalc output \n -v \t Verbose ipcalc output with IP addresses'
	print '\nExamples:\nipcalc -s 192.168.0.1/24\nipcalc -v 192.168.0.1/29\nipcalc -s 192.168.0.1/255.255.255.248\nipcalc -v 192.168.0.1/255.255.255.240'
 
if len(sys.argv) <= 1:
	how_to()
	sys.exit(1)
 
def main():
	try:
		input = sys.argv[2]
		opt = sys.argv[1]
		global ips
		global ip
		ips = Network(input)
		ip = IPNetwork(input)
		if opt == '-s':
			oper()
		elif opt == '-v':
			print '\nVerbose output:'
			oper()
			for x in ipcalc.Network(input):
				print str(x)
		else:
			how_to()
	except ValueError as err:
		print '\n'+str(err)
		how_to()
	except IndexError as err:
		print '\n'+str(err)
		how_to()
	except NameError as err:
		print '\n'+str(err)
		how_to()
	except TypeError as err:
		print '\n'+str(err)
		how_to()
	except:
		print 'Invalid input!'
 
def oper():
	print '\nAddress: '+str(ips)
	print 'Netmask: '+str(ips.netmask())
	print 'Network: '+str(ip.cidr)
	print 'Broadcast: '+str(ips.broadcast())
	print 'HostMin: '+str(ips.host_first())
	print 'HostMax: '+str(ips.host_last())
	print 'Hosts/Net: '+str(ips.size())
	print 'IP is private: '+str(IPAddress(ip.ip).is_private())+'\n'
	#print 'IP Version '+str(ip.version)
 
if __name__ == '__main__':
  main()