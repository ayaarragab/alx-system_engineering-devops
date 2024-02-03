# Replace IdentityFile in /root/.ssh/config
exec { 'ssh_config':
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
