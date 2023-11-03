import os
import sys

os.chdir('/etc/haproxy/')

ip_addresses = sys.argv[1:]

with open('haproxy.cfg', 'a') as f:
    f.write('\n')
    f.write('frontend http_ngfront\n')
    f.write('    bind *:80\n')
    f.write('    stats uri /haproxy?stats\n')
    f.write('    default_backend http_ngback\n')
    f.write('\n')
    f.write('backend http_ngback\n')
    f.write('    balance roundrobin\n')
    for ip in ip_addresses:
        f.write('    server nginx-{0} {1}:80 check\n'.format(ip_addresses.index(ip), ip))

os.system('systemctl restart haproxy')

print('Haproxy configured and restarted.')
