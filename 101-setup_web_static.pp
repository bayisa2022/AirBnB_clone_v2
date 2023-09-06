#!/usr/bin/python3
package {'nginx':
  ensure => installed,
}

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/'],
}

file { '/data/web_static/releases/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/'],
}

file { '/data/web_static/releases/test/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/'],
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Test page',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test/'],
}

file_line { 'nginx_config':
  path    => '/etc/nginx/sites-available/default',
  line    => 'root /data/web_static/current;',
  match   => 'root /var/www/html;',
  require => Package['nginx'],
}

file_line { 'nginx_alias':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/; }',
  after   => 'root /data/web_static/current;',
  require => File_line['nginx_config'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
