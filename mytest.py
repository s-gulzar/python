def myfunction5(k):
    if k > 0:
        results = k + myfunction5(k - 1)
    else:
        results = 0

    print(results)
    return results


myfunction5(6)