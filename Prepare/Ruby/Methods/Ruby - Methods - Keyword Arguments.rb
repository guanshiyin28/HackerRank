# Your code here
def convert_temp(temperature, input_scale:, output_scale: :celsius)    
    {
        [:celsius, :fahrenheit] => ->(t) { (t * 9.0/5.0) + 32.0 },
        [:celsius, :kelvin] => ->(t) { t + 273.15 },
        [:fahrenheit, :celsius] => ->(t) { (t - 32.0) * 5.0/9.0 },
        [:fahrenheit, :kelvin] => ->(t) { ((t - 32.0) * 5.0/9.0) + 273.15 },
        [:kelvin, :celsius] => ->(t) { t - 273.15 },
        [:kelvin, :fahrenheit] => ->(t) { (t - 273.15) * 9.0/5.0 + 32.0 },
    }[[input_scale.to_sym, output_scale.to_sym]].call(temperature)
end
