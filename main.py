def main():

    N = int(input('Enter the number N: '))
    result = []
    i = 0
    j = 1

    while i <= N:
        result.append(j)
        j = j * 2
        i += 1
    print(result)


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
