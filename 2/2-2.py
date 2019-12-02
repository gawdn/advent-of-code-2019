from copy import deepcopy


def get_instructions(program, n=4):
    """
    Retrieves the next instruction in the program
    Yields: <opcode> <arg1> <arg2> <result_index>
    Returns: if the instruction has an opcode of 99
    """
    program_counter = 0
    while program_counter < len(program):
        instruction = program[program_counter:program_counter + n]

        if instruction[0] == 99:
            return
        else:
            yield instruction

        program_counter += 4


def execute_program(program):
    """
    Executes program given a list of intcodes
    """
    new_program = deepcopy(program)

    for instruction in get_instructions(new_program):
        opcode, arg1, arg2, result_index = instruction

        if opcode == 1:
            new_program[result_index] = new_program[arg1] + new_program[arg2]
        elif opcode == 2:
            new_program[result_index] = new_program[arg1] * new_program[arg2]
        else:
            print(f"Unknown opcode given {opcode}")

    return new_program[0]


if __name__ == "__main__":
    with open("2.1202.in", "r") as codes_fp:
        codes = codes_fp.readline().strip().split(',')
        codes = list(map(int, codes))

    for noun in range(0, 100):
        for verb in range(0, 100):
            codes[1], codes[2] = noun, verb
            result = execute_program(codes)
            if result == 19690720:
                print(100 * noun + verb)
