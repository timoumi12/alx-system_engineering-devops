# fix Apache 500 error

exec { 'fix':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
