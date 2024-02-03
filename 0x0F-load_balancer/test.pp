exec { 'apt_update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->

exec { 'echo_hello_world':
  command => "sudo sh -c 'echo \"Hello World!\" > /var/www/html/index.html'",
  path    => '/usr/bin/sudo:/bin:/usr/bin:/usr/sbin',
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /var/www/html;
     index       index.html index.htm;
  }",
} ->

exec { 'echo_custom_404':
  command => "sudo echo 'Ceci n'est pas une page' > /usr/share/nginx/html/custom_404.html",
  path    => '/usr/bin/sudo:/usr/bin/echo',
} ->

exec { 'sed_update_default':
  command => "sudo sed -i 's/server_name _;/server_name _;\\n\\trewrite ^\\/redirect_me https:\\/\\/github.com\\/Tolulope05 permanent;\\n\\n\\terror_page 404 \\/custom_404.html;\\n\\tlocation = \\/custom_404.html {\\n\\t\\troot \\/usr\\/share\\/nginx\\/html;\\n\\t\\tinternal;\\n\\t}/' /etc/nginx/sites-available/default",
  path    => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

exec { 'sed_update_nginx_conf':
  command => "sudo sed -i 's/include \\/etc\\/nginx\\/sites-enabled\\/\\*;/include \\/etc\\/nginx\\/sites-enabled\\/\\*;\\n\\tadd_header X-Served-By \"$HOSTNAME\";/' /etc/nginx/nginx.conf",
  path    => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

exec { 'sed_update_nginx_conf_header':
  command => "sudo sed -i 's/http{/http{\\n add_header X-Served-By $hostname;/' /etc/nginx/nginx.conf",
  path    => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Exec['apt_update'], Package['nginx'], File['/etc/nginx/sites-available/default']],
}
