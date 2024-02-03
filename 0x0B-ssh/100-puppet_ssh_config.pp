# same as task 1 but with puppet
exec { 'ssh_ident':
  provider => shell,
  command => 'sed "s|IdentityFile *|IdentityFile ~/.ssh/school|" -i /root/.ssh/config',
}

exec { 'ssh_ident':
  provider => shell,
  command => 'sed "s|PasswordAuthentication *|PasswordAuthentication no|" -i /root/.ssh/config',
}
