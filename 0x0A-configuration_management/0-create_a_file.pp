# this file makes a new file with some desired features
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
