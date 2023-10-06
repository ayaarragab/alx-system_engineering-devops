#!/usr/bin/env ruby
# [SENDER],[RECEIVER],[FLAGS]
# values within () are the only captured (yeah)!
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(\+?\d{11})\] \[flags:(\S+)\]/).join(",")
