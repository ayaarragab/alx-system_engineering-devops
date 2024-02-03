# everything in task 0 but in puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
 ensure   => 'present',
 provider => 'apt',
 require  => Exec['update'],
}

exec { "sudo sh -c 'echo 'Hello World!'' > /var/www/html/index.html":
  path => '/usr/bin/sudo:/bin:/usr/bin:/usr/sbin',
}

exec { 'echo_command':
  command => 'sudo echo "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /var/www/html;
     index       index.html index.htm;
  }" > /etc/nginx/sites-available/default',
  path   => '/usr/bin/sudo:/usr/bin/echo',
}

exec { "sudo echo 'Ceci n'est pas une page' > /usr/share/nginx/html/custom_404.html":
  path => '/usr/bin/sudo:/usr/bin/echo',
}

exec {'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Tolulope05 permanent;\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default':
  path => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} 

exec {'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf':
  path => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec {'sudo sed -i "s/http{/http{\n add_header X-Served-By $hostname;/g" /etc/nginx/nginx.conf':
  path => '/usr/bin/sudo:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'nginx restart':
  path    => '/etc/init.d/',
  require => [Exec['update'], Package['nginx'], File['/etc/nginx/sites-available/default']],
}
