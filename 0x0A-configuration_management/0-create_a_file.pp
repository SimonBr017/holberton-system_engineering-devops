# Create a file in /tmp using Puppet
  file { '/tmp/holberton': #the path of the new file
    ensure  => 'present',
    content => 'I love Puppet', #this text will be inside the file
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
  }
