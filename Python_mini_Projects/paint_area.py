def paint_calc(height, width, cover):
    number_of_cans = 0
    number_of_cans = (height * width) / 5
    print(round(number_of_cans))

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
