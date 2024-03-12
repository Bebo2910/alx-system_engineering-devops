class nginx_setup {
  package { 'nginx':
    ensure => installed, # Ensure Nginx is installed
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('nginx/nginx.conf.erb'), # Use an ERB template to populate the configuration
    require => Package['nginx'], # This configuration requires that the Nginx package is installed
    notify  => Service['nginx'], # Notify the Nginx service if the file changes
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => File['/etc/nginx/nginx.conf'], # This service requires the Nginx configuration file
  }
}

# Example content of nginx/nginx.conf.erb (you need to create this template file)
# worker_processes auto;
# worker_connections 1024;
# ... Add other configurations as needed ...

# To apply the manifest:
# puppet apply 0-the_sky_is_the_limit_not.pp

