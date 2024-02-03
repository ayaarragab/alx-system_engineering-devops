# Replace IdentityFile in /root/.ssh/config
exec { 'ssh_ident':
  command => 'sed "s|IdentityFile *|IdentityFile ~/.ssh/school|" -i /root/.ssh/config',
}

# Disable PasswordAuthentication in /root/.ssh/config
exec { 'ssh_password_auth':
  command => 'sed "s|PasswordAuthentication *|PasswordAuthentication no|" -i /root/.ssh/config',
}
