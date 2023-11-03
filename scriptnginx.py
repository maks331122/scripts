import os
import sys

ip = sys.argv[1]

os.chdir('/etc/nginx/sites-available/')

instance = sys.argv[2]

with open('site.conf', 'w') as f:
	f.write("server {\n")
	f.write("	listen 8080;\n")
	f.write("	listen [::]:8080;\n")
	f.write("	root /var/www/html/libro/public;\n")
	f.write("	index index.html;\n")
	f.write("	server_name %s;\n" % ip)
	f.write("	location / {\n")
	f.write("		try_files $uri $uri/ =404;\n")
	f.write("	}\n")
	f.write("}\n")

with open('/var/www/html/index.html', 'w') as f:
	f.write('site{0}'.format(instance))

os.system('ln -n site.conf /etc/nginx/sites-enabled/site.conf')
os.system('systemctl restart nginx')

print('Nginx налаштовано!!')

