def fizzbuz a, b, n
  (1..n).collect do |i|
    fizz = (i % a).zero?
    buzz = (i % b).zero?
    fizz & buzz ? 'FB' : fizz ? 'F' : buzz ? 'B' : i
  end
end

ARGF.each_line do |line|
  puts (fizzbuz *line.split.map(&:to_i)).join ' '
end
