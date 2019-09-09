# Python 3

# Solves Todd Lammle's IP Subnet Practice Page problem - https://www.lammle.com/ip-subnet-practice-page
# Given an IP address and subnet mask in the form xxx.xxx.xxx.xxx/xx , find the
# 1.) Network IP
# 2.) First Host
# 3.) Last Host
# 4.) Broadcast

# User input is the IP address and subnet mask given in the above form
# No error handling; user input must be in the above form


# input is a list of length 32 representing the IP's binary bits
# returns ip address in human readable form
def displayIP(list_binary):
	ip_address = ''
	octet = ''
	count = 0
	
	for i in list_binary:
		count += 1
		octet += i 
		if count % 8 == 0:
			if count != 32:
				ip_address += ( str(int(octet, 2)) + '.' )
			else:
				ip_address += str(int(octet, 2))
			octet = '' 
		
	return ip_address
	
# input is ip address in decimal form 
# returns ip address as a list of length 32, representing the IP's binary bits
def decimalToListBinary(decimal):
	binary_form = bin(decimal)[2:].zfill(32)
	
	list_binary_form = []
	
	for i in binary_form:
		list_binary_form += i
	
	return list_binary_form 


# get ip address and subnet mask from user
ip_mask = input("What is the IP address in CIDR notation? (in the form: xxx.xxx.xxx.xxx/xx) ")
ip_mask_list = ip_mask.split('/')

# take ip address and put its 4 octets in to a list
ip = ip_mask_list[0]
ip_list = ip.split('.')

# convert each of the 4 octets of the ip address to an 8-digit binary number, padding zero's [0] in the front if necessary
ip_list_binary = []

for x in ip_list:
	ip_list_binary.append('{0:08b}'.format(int(x)))

# turn 'ip_list_binary' from list of four 8-digit binary numbers to list of thirty-two 1-digit binary numbers
ip_list_binary = ''.join(ip_list_binary)
ip_list_binary = list(ip_list_binary)

# convert subnet mask to 32-digit binary form
mask = ip_mask_list[1]
mask_list_binary = []
mask_num_zeros = 0 # used to calculate the number of hosts

# number of one's [1] in the subnet mask = number to the right of the forward slash [/] in CIDR notation
for i in range(int(mask)):
	mask_list_binary.append('1')

# number of zero's [0] in subnet mask = 32 - number of one's [1] in subnet mask
count = 32 - int(mask)
for i in range(count):
	mask_list_binary.append('0')
	mask_num_zeros += 1
	
# Solving for NETWORK (part 1 of solution)
# NETWORK = 'AND gate' between 'ip_list_binary' and 'mask_list_binary'

network_list_binary = [] 
for n, m in zip(ip_list_binary, mask_list_binary):
	if n == '1' and m == '1':
		network_list_binary.append('1')
	else:
		network_list_binary.append('0')

# Solving for 1ST HOST (part 2 of solution)
# 1ST HOST = NETWORK + 1

network_binary = ''.join(network_list_binary)

first_host_decimal = int(network_binary, 2) + 1
first_host_list_binary = decimalToListBinary(first_host_decimal)
	
# Solving for LAST HOST (part 3 of solution)
# LAST HOST = number of hosts + 1ST HOST - 1
# number of hosts = 2^(number of zero's [0] in the subnet mask) - 2

number_of_hosts = 2**mask_num_zeros - 2

last_host_decimal = number_of_hosts + first_host_decimal - 1
last_host_list_binary = decimalToListBinary(last_host_decimal)
	
# Solving for BROADCAST (part 4 of solution)
# BROADCAST = LAST HOST + 1

broadcast_decimal = last_host_decimal + 1
broadcast_host_list_binary = decimalToListBinary(broadcast_decimal)


print()
print('  ~~Solution~~')
print()
print('  Network:      ' + displayIP(network_list_binary))
print()
print('  First Host:   ' + displayIP(first_host_list_binary))
print()
print('  Last Host:    ' + displayIP(last_host_list_binary))
print()
print('  Broadcast:    ' + displayIP(broadcast_host_list_binary))
print()
			
 
