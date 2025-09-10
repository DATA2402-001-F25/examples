
amts = [100.00, 50.00, 'missing', 25.00, 75.00, None]

# write a loop that computes GST amounts for each of the values
# BUT where that's not possible, use the number 0.0 instead

for value in amts:
    try:
        gst = value * 0.05
    except TypeError:
        gst = 0.0

    print(gst)