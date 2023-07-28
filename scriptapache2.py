import os

dns = input('Введіть ваш DNS:')
try:
	os.system('systemctl stop nginx')
except (Exception):
	pass

os.chdir('/etc/apache2/sites-available/')

with open('{0}.conf'.format(dns.split('.')[0]), 'w') as f:
	f.write('<VirtualHost *:80>\n')
	f.write('ServerName {0}\n'.format(dns))
	f.write('DocumentRoot /var/www/{0}\n'.format(dns.split('.')[0]))
	f.write('</VirtualHost>\n')

if not os.path.exists('/var/www/{0}'.format(dns.split('.')[0])):
	os.mkdir('/var/www/{0}'.format(dns.split('.')[0]))
	with open('/var/www/{0}/index.html'.format(dns.split('.')[0]), 'w') as f:
		f.write('{0}'.format(dns.split('.')[0]))

os.system('a2ensite {0}.conf'.format(dns.split('.')[0]))
os.system('systemctl restart apache2')

print('Apache 2 налаштовано!!')

