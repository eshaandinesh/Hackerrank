
class TestDataEmptyArray:
    def get_array():
        return []

class TestDataUniqueValues():
    def get_array():
        return [1,2,3,4,5]
    
    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums():
    def get_array():
        return [1,2,1]
    
    def get_expected_result():
        return 0

