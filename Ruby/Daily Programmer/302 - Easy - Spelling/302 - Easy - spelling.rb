elements = {}

def is_num(str)
  !!Integer(str)
rescue ArgumentError, TypeError
  false
end

File.open("elements.csv").each do |line|
  splittedLine = line.split(",")
  elements[splittedLine[1].slice(1, splittedLine[1].length-2)] = splittedLine[2].slice(1, splittedLine[2].length-2)
end


def spellWithChem(input, elements)
  output = ""
  elementOutput = ""
  puts input
  while input!="" do
    if(elements.has_key?(input[0..2].capitalize))
      output += input[0..2].capitalize
      elementOutput += elements[input[0..2].capitalize] + ", "
      input.slice!(0, 3)
    elsif(elements.has_key?(input[0..1].capitalize))
      output += input[0..1].capitalize
      elementOutput += elements[input[0..1].capitalize] + ", "
      input.slice!(0, 2)
    elsif(elements.has_key?(input[0].capitalize))
      output += input[0].capitalize
      elementOutput += elements[input[0].capitalize] + ", "
      input.slice!(0)
    else
      puts "can't be done missing: #{input[0].capitalize}"
      return
      break
    end
  end

  puts "#{output} (#{elementOutput})"
end




spellWithChem("functions", elements)
spellWithChem("bacon", elements)
spellWithChem("poison", elements)
spellWithChem("sickness", elements)
spellWithChem("ticklish", elements)
