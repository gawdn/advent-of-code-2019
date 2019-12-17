from datetime import datetime


def count_possible_password(min_num=108457, max_num=562041):
    """
    Counts password matching the criteria:

    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    possible_count = 0

    start = datetime.now()

    for i in range(min_num, max_num):
        possible_password = f"{i:0{len(str(max_num))}}"
        is_valid = True

        runs = []

        for i in range(len(possible_password)):
            try:
                if int(possible_password[i]) > int(possible_password[i + 1]):
                    is_valid = False
                    break
            except IndexError:
                pass

            if not runs or runs[-1][0] != possible_password[i]:
                runs.append([possible_password[i], 1])
            else:
                runs[-1][1] += 1

        has_repeat = any([True for x in runs if x[1] == 2])
        if has_repeat and is_valid:
            print(possible_password, runs)
            possible_count += 1

    print(f"\n\nTook {datetime.now() - start}")
    return possible_count
