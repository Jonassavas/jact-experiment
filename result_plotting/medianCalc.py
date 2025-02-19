def calculate_median(arr):
    if len(arr) != 30:
        print("INCORRECT ARRAY SIZE")
        return 0
    
    # Sort the array
    arr_sorted = sorted(arr)
    
    # Find the number of elements
    n = len(arr_sorted)
    
    # Determine if the number of elements is odd or even
    if n % 2 == 1:
        # If odd, return the middle element
        median = arr_sorted[n // 2]
    else:
        # If even, return the average of the two middle elements
        middle1 = arr_sorted[n // 2 - 1]
        middle2 = arr_sorted[n // 2]
        median = (middle1 + middle2) / 2
    
    # Return the median rounded to one decimal place
    return round(median, 1)

def calculate_sum(arr):
    return sum(arr)

# Example usage
LoCArr = [302852, 51463, 30133, 16781, 571930, 
          35539, 66119, 19506, 2809, 42920, 
          16448, 89227, 7534, 33514, 15558, 
          18869, 53165, 21769, 64011, 76397, 
          101743, 7195, 20882, 31201, 2405, 
          5769, 508, 32388, 105046, 60400]
print(f"LoC Median: {calculate_median(LoCArr)}")
numberOfTestsArr = [3887, 1291, 168, 576, 1459,
                     855, 2460, 979, 30, 669, 37,
                     210, 500, 83, 5893, 122,
                    2600, 614, 1790, 35, 624,
                     151, 125, 274, 64, 82,
                       9, 305, 725, 868]
print(f"Project Coverage Median: {calculate_median(numberOfTestsArr)}")

# 6, 9, 20, 23, 24, 

directDepArr = [7,14,2,4,21,
                7,11,4,12,5,
                2,5,3,17,5,
                14,24,4,7,5,
                4,3,5,31,1,
                5,3,2,4,4]
print(f"Direct Dependency Median: {calculate_median(directDepArr)}")
print(f"Direct Dependency Sum: {calculate_sum(directDepArr)}")
indirectDepArr = [14,20,0,0,10,
                  12,9,6,27,0,
                  0,4,1,18,4,
                  8,20,2,1,31,
                  1,0,31,25,1,
                  3,6,0,2,1]
print(f"Indirect Dependency Median: {calculate_median(indirectDepArr)}")
print(f"Indirect Dependency Sum: {calculate_sum(indirectDepArr)}")
projectCovArr = [45.3, 49.2, 59.4, 85.9, 19.2, 
                 53.5, 80.4, 91.8, 76.7, 50.6, 
                 60.4, 32.6, 97.5, 44.5, 91.3, 
                 31.7, 42.4, 84.6, 86.8, 40.7, 
                 56.9, 73.2, 79.9, 34.8, 93.9, 
                 45.3, 75.4, 6.7, 61.9, 67.7]
print(f"Project Coverage Median: {calculate_median(projectCovArr)}")

dependenciesCovArr = [5.0, 7.4, 27.2, 6.2, 2.2, 
                      5.4, 8.4, 10.3, 13.9, 12.7, 
                      34.3, 0.8, 10.8, 5.0, 3.3, 
                      1.5, 4.4, 17.4, 16.1, 1.4, 
                      6.0, 5.7, 6.9, 14.4, 1.7, 
                      5.8, 7.3, 1.0, 15.9, 21.8]
print(f"Dependency Coverage Median: {calculate_median(dependenciesCovArr)}")

directDepCovArr = [6.8, 8.1, 27.2, 6.2, 1.6, 
                   11.6, 12.4, 10.5, 21.5, 12.7, 
                   34.3, 1.0, 8.8, 5.3, 3.3, 
                   1.2, 4.5, 18.2, 14.1, 1.9, 
                   6.1, 5.7, 9.5, 18.0, 1.7, 
                   5.7, 9.2, 1.0, 17.1, 22.9]
print(f"Direct Dependency Coverage Median: {calculate_median(directDepCovArr)}")

indirectDepCovArr = [0.9, 6.0, 0.0, 0.0, 4.9, 
                     1.0, 2.5, 0.0, 10.6, 0.0, 
                     0.0, 0.0, 23.5, 4.1, 2.7, 
                     2.1, 3.8, 1.4, 36.0, 0.6, 
                     5.2, 0.0, 6.6, 4.4, 0.0, 
                     6.0, 5.7, 0.0, 0.0, 0.0]
print(f"Indirect Dependency Coverage Median: {calculate_median(indirectDepCovArr)}")

projectAndDepCovArr = [10.0, 9.7, 54.7, 19.7, 9.2, 
                       6.4, 15.6, 22.9, 14.4, 23.2, 
                       35.9, 6.7, 18.4, 7.6, 5.2, 
                       2.6, 8.1, 21.7, 27.7, 4.4, 
                       12.7, 21.9, 7.7, 15.3, 2.9, 
                       6.7, 7.5, 4.5, 50.1, 41.3]
print(f"Project + Dependency Coverage Median: {calculate_median(projectAndDepCovArr)}")
