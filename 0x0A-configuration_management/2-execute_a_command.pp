# file to excute an command
exec {'pkill killmenow':
  command => 'pkill killmenow'
  path => '/usr/bin/'
}
