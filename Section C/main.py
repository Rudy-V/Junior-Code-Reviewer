import unittest

def ISBN(isbn_number):
    '''This function takes a string of numbers and  returns "Valid" or "Invalid".'''
    
    def verify10(number):
        '''This function verifies the ISBN10 number and returns an ISBN13 number'''
        # Creating sum variables
        isbn_sum = 0

        # Reversed number for assistance in verification - ISBN10
        num_reversed = number[::-1].lower()

        # Replaces the x with 10
        if num_reversed.find("x") != -1:
            num_reversed = num_reversed.replace("x","10")

        # Adding all the values together
        if (len(num_reversed) == 10):
            for i in range(len(num_reversed)):
                isbn_sum += (int(num_reversed[i]))*((i+1))
        else:
            isbn_sum += 100
            for i in range(2,len(num_reversed)):
                isbn_sum += (int(num_reversed[i]))*((i+1))

        # verifying that the number is valid and converting to ISBN13
        if isbn_sum % 11 == 0:
            return convertTo13(num_reversed)
        else:
            return "Invalid"
    
    def verify13(number):
        '''This function verifies is a number is a valid ISBN13 number'''
        # Creating sum variables
        first_sum = 0
        second_sum = 0

        # Multiplying each element with either 1 or 3
        for i in range(0,len(number),2):
            first_sum += int((number[i]))*1
        for i in range(1,len(number),2):
            second_sum += int((number[i]))*3
        total_sum = first_sum + second_sum

        # Verifying if the number is valid
        if total_sum%10 == 0:
            return "Valid"
        else:
            return "Invalid"

    def convertTo13(num_reversed):
        '''This function converst the ISBN10 number to an ISBN13 number'''
        new_number = num_reversed[1:]
        new_number = new_number + "879"
        new_number = new_number[::-1]
        # Creating sum variables
        first_sum = 0
        second_sum = 0

        # Multiplying each element with either 1 or 3
        for i in range(0,len(new_number),2):
            first_sum += int((new_number[i]))*1
        for i in range(1,len(new_number),2):
            second_sum += int((new_number[i]))*3
        total_sum = first_sum + second_sum

        # Calculating last digit
        mod = total_sum%10
        last_digit = 10 - mod

        return new_number + str(last_digit)

    if len(isbn_number) == 10:
        return verify10(isbn_number)
    elif len(isbn_number) == 13:
        return verify13(isbn_number)
    else:
        return "Invalid number"

class SimpleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ISBN("0330301824"),"Invalid")
    def test_2(self):
        self.assertEqual(ISBN("9780316066525"),"Valid")
    def test_3(self):
        self.assertEqual(ISBN("0316066524"),"9780316066525")

if __name__ == '__main__':
    unittest.main()