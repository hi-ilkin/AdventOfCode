import sys
import day_1.solution as d1
# import day_2.solution as d2
# import day_3.solution as d3
# import day_4.solution as d4
# import day_5.solution as d5
import day_6.solution as d6
import day_7.solution as d7
import day_8.solution as d8
import day_9.solution as d9
import day_10.solution as d10
import day_11.solution as d11
import day_12.solution as d12
import day_13.solution as d13
import day_14.solution as d14
import day_15.solution as d15


def parse_arguments():
    args = sys.argv

    if len(args) < 2:
        raise Exception("Not enough arguments. Please provide iteration count and days.")

    iterations = int(sys.argv[1])
    days_ = sys.argv[2:]
    return iterations, days_


solutions = {
    '1': d1.main,
    # '5': d5.main,
    # '6': d6.main,
    # '7': d7.main,
    # '8': d8.main,
    # '9': d9.main,
    # '10': d10.main,
    # '11': d11.main,
    '12': d12.main,
    '13': d13.main,
    '14': d14.main,
    '15': d15.main,
}

if __name__ == '__main__':
    itr, days = parse_arguments()
    for _ in range(itr):
        print('Solving...')

        for day in days:
            run = solutions.get(day, None)
            if run is None:
                print(f'Day {day} is not available')
            else:
                run()
