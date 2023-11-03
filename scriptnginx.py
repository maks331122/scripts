import os
import sys

ip = sys.argv[1]

os.chdir('/etc/nginx/sites-available/')

instance = sys.argv[2]

with open('site.conf', 'w') as f:
	f.write("server {\n")
	f.write("	listen 8080;\n")
	f.write("	listen [::]:8080;\n")
	f.write("	root /var/www/site/index.html;\n")
	f.write("	index index.html;\n")
	f.write("	server_name {0};\n".format(ip))
	f.write("	location / {\n")
	f.write("		try_files $uri $uri/ =404;\n")
	f.write("	}\n")
	f.write("}\n")

if not os.path.exists('/var/www/site'):
	os.mkdir('/var/www/site')
	with open('/var/www/site/index.html', 'w') as f:
		f.write('site{0}'.format(instance))

os.system('ln -n site.conf /etc/nginx/sites-enabled/site.conf')
os.system('systemctl restart nginx')

print('Nginx налаштовано!!')

