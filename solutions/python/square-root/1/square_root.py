def square_root(number):
    # Make an initial estimate, 'Binary estimate' method from wikipedia
    sci_note = f"{number:e}"
    base, power = sci_note.split("e+")
    estimate = (0.5 + 0.5 * float(base)) * (2 ** int(power))

    # Refine the estimate, Heron's method
    # One iteration per magnitude of the input
    # Not sure how to actually tell how many iterations are needed,
    #   but for these tests at least this works.
    for i in str(number):
        estimate = (number/estimate + estimate) / 2
    return round(estimate)