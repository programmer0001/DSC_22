def count_full_probability(coins1, tr):
    probabilities = [0.48]

    for i in range(len(tr)):
        p = len(list(filter(lambda x: x == 1, tr[:i+1]))) / len(tr[:i+1])

        for j in range(len(coins1) - 1):
            if coins1[j] <= p <= coins1[j+1]:
                a = coins1[j+1]
                break
            else:
                a = coins1[-1]
        prob = (probabilities[i] + a) / 2
        probabilities.append(round(prob, 2))

    print("Probabilities = ", probabilities)


if __name__ == '__main__':
    coins = [0.1, 0.2, 0.4, 0.8, 0.9]
    tests_res = [1, 1, 1, 0, 1, 0, 1, 1]
    count_full_probability(coins, tests_res)
