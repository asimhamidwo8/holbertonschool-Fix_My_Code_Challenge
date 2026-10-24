#!/usr/bin/env ruby

numbers = ARGV.select { |arg| arg.match?(/\A-?\d+\z/) }.map(&:to_i)

puts numbers.sort

