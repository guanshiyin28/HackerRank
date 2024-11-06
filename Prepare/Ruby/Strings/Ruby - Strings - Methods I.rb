def process_text(text_array)
  text_array.map(&:strip).join(" ")
end
