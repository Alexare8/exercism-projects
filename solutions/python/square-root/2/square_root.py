def square_root(number):
    if number == 1: return 1   # 1 breaks, everything else is fine
    estimate = number / 2      # Make *any* initial estimate

    # Refine the estimate, Heron's method
    prev_est = number
    while prev_est - estimate >= 1:
        prev_est = estimate
        estimate = (number/estimate + estimate) / 2
    return round(estimate)