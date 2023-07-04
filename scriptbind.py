import os

nsstr = input("Введіть ваш домен:")
nsarr = nsstr.split(".")
ipaddr = input("Введіть ваш IP:")
iparr = ipaddr.split(".")
os.chdir("/etc/bind/")
with open("named.conf.local", "w") as f:
	f.write("zone {0} {{\n".format(nsstr))
	f.write("	type master;\n")
	f.write("	file \"/etc/bind/forvard_{0}\";\n".format(nsarr[0]))
	f.write("};\n")
	f.write("\n")
	f.write("zone \"{2}.{1}.{0}.in-addr.arpa\" {{\n".format(iparr[0],iparr[1],iparr[2]))
	f.write("	type master;\n")
	f.write("	file \"/etc/bind/reverse_{0}\";\n".format(nsarr[0]))
	f.write("};\n")

with open("forvard_{0}".format(nsarr[0]), "w") as f:
	f.write("$TTL    86400\n")
	f.write("@       IN      SOA     ns.{0}. root.{0}. (\n".format(nsstr))
	f.write("                              1         ; Serial\n")
	f.write("                         604800         ; Refresh\n")
	f.write("                          86400         ; Retry\n")
	f.write("                        2419200         ; Expire\n")
	f.write("                          86400 )       ; Negative Cache TTL\n")
	f.write(";\n")
	f.write("@       IN      NS      ns.{0}.\n".format(nsstr))
	f.write("ns.{0}. IN      A       {1}\n".format(nsstr,ipaddr))
	f.write("{0}.    IN      A       {1}\n".format(nsstr,ipaddr))
	f.write("site1   IN      A       {0}\n".format(ipaddr))
	f.write("site2   IN      A       {0}\n".format(ipaddr))

with open("reverse_{0}".format(nsarr[0]), "w") as f:
	f.write("$TTL    86400\n")
	f.write("@       IN      SOA     ns.{0}. root.{0}. (\n".format(nsstr))
	f.write("                              1         ; Serial\n")
	f.write("                         604800         ; Refresh\n")
	f.write("                          86400         ; Retry\n")
	f.write("                        2419200         ; Expire\n")
	f.write("                          86400 )       ; Negative Cache TTL\n")
	f.write(";\n")
	f.write("@       IN      NS      ns.{0}.\n".format(nsstr))
	f.write("{0}      IN      PTR     {1}.".format(iparr[3],nsstr))
	f.write("{0}      IN      PTR     site1.{1}.\n".format(iparr[3],nsstr))
	f.write("{0}      IN      PTR     site2.{1}.\n".format(iparr[3],nsstr))

with open("/etc/resolv.conf", "w") as f:
	f.write("nameserver {0}\n".format(ipaddr))



os.system("systemctl start named")
os.system("systemctl enable named")
os.system("systemctl restart named")

os.system("echo DNS налаштовано!!")
