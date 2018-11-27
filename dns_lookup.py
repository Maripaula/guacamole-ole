# -*- coding: utf-8 -*-

#################################################################################
# File Name:    dns_lookup.py
# Version:      1.0
# Created:      2018-08-15
# Contributors: MariPaula
# Modified:
# Modified By:
# Synopsis:     Used for finding specific hostnames by regex, given a list of IPs
# Changelog:
#################################################################################

import socket
import re

# Input and output file paths
file_path = ''
out_file = ''

# Attempt to get hostnames for each IP
with open(file_path, 'r') as in_file:
    for line in in_file:
        # Regex for domain name you are searching for
        reg_1 = '.[company].com'
        reg_2 = '.[site].com'
        
        ip = line.strip('\n')
        try:
            response = socket.gethostbyaddr(ip)
            hostname = response[0]
            
            # Attempt to sort company and site names from given list
            if re.search(reg_1, hostname) or re.search(reg_2, hostname):
                company_ips.append(ip)

            else:
                other_ips.append(ip)

        except Exception as e:
            print "Error finding hostname for IP {0}: {1}".format(ip,e.args[0])
            continue

# Write IPs out to file
out = open(out_file, "w")
out.write('Company IPs: ' + str(company_ips) + '\n' + 'Other IPs: ' + str(other_ips))
