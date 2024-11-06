def skip_animals(animals, skip)
  # Your code here
    animals.enum_for(:each_with_index).select { |v, i| i >= skip }.map { |v, i| "#{i}:#{v}"}
end
