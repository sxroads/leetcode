class Solution(object):
    def romanToInt(self, s):
        
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Go through the string from left to right
        for char in s:
            current_value = roman_to_int[char]
            
            # If the previous value is less than the current value, subtract the previous value
            if prev_value < current_value:
                total -= 2 * prev_value  # Subtract the previous value and then subtract it again for correct calculation
            
            # Add the current value to the total
            total += current_value
            # Update the previous value
            prev_value = current_value
        
        return total
    

#	*s6xroad*