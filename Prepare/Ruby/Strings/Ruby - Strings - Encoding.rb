# Enter your code here.
def transcode(encoded_input_string)
    encoded_input_string.force_encoding(Encoding::UTF_8)
end

def transcode_to_ISO_8859_1(encoded_input_string)
    encoded_input_string.force_encoding(Encoding::ISO_8859_1)
end
transcode(transcode_to_ISO_8859_1("Bhavana"))
