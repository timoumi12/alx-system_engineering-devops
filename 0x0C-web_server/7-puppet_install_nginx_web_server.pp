# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" > /var/www/html/index.html' ; echo "server {\n\tlisten 80;\n\troot\t/etc/nginx/html;\n\tindex  index.html;\n\tlocation /redirect_me {\n\t\treturn 301 www.linkedin.com/in/iheb-timoumi-576a311b0;\n\t}\n}" > /etc/nginx/sites-available/default ;sudo service nginx start',
}
