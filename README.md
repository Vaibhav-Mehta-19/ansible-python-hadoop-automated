# ansible-python-hadoop-automated
Automating the creation of a hadoop cluster using an ansible playbook, python-cgi and an html web page.

Copy the html file in the /var/www/html folder in Linux machine. Edit the file to give the ip of your system.
Copy the yml and python file in /var/www/cgi-bin folder in Linux machine. Make the changes required in the files like changing the ip to your system ip,etc.

Now open the browser and run the html file and give the values for launch suitable cluster. 

This file will setup both the server and the clients as given in the ansible-hosts file. 
