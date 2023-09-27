# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'echo "server {
      listen 80;
      root   /etc/nginx/html;
      index  index.html;
      location /redirect_me {
        return 301 www.linkedin.com/in/iheb-timoumi-576a311b0;
      }
}" > /etc/nginx/sites-available/default',
}
