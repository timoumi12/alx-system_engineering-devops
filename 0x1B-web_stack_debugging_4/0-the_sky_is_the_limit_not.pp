# fix limit file
exec { 'Correct file and restart':
  provider => "shell",
  command  => 'sudo sed -i \'s/15/30000/\' /etc/default/nginx && sudo service nginx restart'
}
