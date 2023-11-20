# fix Apache 500 error

exec {
  provider => 'shell',
  command  => 'sed -i "/s/phpp/php/g" /var/www/html/wp-settings.php'
}
