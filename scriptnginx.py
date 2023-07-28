import os

dns = input('Введіть ваш DNS:')
try:
	os.system('systemctl stop apache2')
except (Exception):
	pass

os.chdir('/etc/nginx/sites-available/')

with open('{0}.conf'.format(dns.split('.')[0]), 'w') as f:
	f.write("server {\n")
	f.write("	listen 80;\n")
	f.write("	listen [::]:80;\n")
	f.write("	root /var/www/{0};\n".format(dns.split('.')[0]))
	f.write("	index index.html index.htm index.nginx-debian.html;\n")
	f.write("	server_name {0};\n".format(dns))
	f.write("	location / {\n")
	f.write("		try_files $uri $uri/ =404;\n")
	f.write("	}\n")
	f.write("}\n")

if not os.path.exists('/var/www/{0}'.format(dns.split('.')[0])):
	os.mkdir('/var/www/{0}'.format(dns.split('.')[0]))
	with open('/var/www/{0}/index.html'.format(dns.split('.')[0]), 'w') as f:
		f.write('{0}'.format(dns.split('.')[0]))

os.system('ln -n {0}.conf /etc/nginx/sites-enabled/{0}.conf'.format(dns.split('.')[0]))
os.system('systemctl restart nginx')

print('Nginx налаштовано!!')

