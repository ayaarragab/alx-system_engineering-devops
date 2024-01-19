# i am forced to write a comment
exec { 'killmenow_cod':
    command => '/usr/bin/pkill killmenow',  # Adjust the path if needed
    path => '.',
}
