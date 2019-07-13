#!/usr/bin/python36
import subprocess as sp
import cgi

print("content-type: text/html \n")

form=cgi.FieldStorage()
i=(form.getvalue("a"))
i1=(form.getvalue("b"))
b=(form.getvalue("c"))

print(i)
print(i1)
print(b)

fp=open('/root/Desktop/hosts','w')
fp2=open('/var/www/cgi-bin/master.yml','w')
fp3=open('/etc/ansible/hosts','a')
fp.write("127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n\n\n")
fp.write(i+"  "+i1)
fp.write("\n")
fp2.write("x: "+i+"\n")
fp3.write("[master]\n"+i+"[slaves]\n")
fp2.close()
slaveip=[]
slavename=[]
i=0
b=int(b)
while b>0:
	ip1=""
	name=""
	fp.write(ip1+"  "+name+"\n")
	fp3.write(ip1)
	i+=1
	b-=1
fp.close()
fp3.close()
sp.getoutput("sudo ansible-playbook hadoop.yml")