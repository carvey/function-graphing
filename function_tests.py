from functions.tools import FunctionSet, get_functions, registered_functions


num_set = list(range(0, 1500))

functions = get_functions()
fc = FunctionSet(num_set, functions)
fc.graph()


for target_function in registered_functions:
    print("FUNCTION: %s" % target_function.name)

    for function in registered_functions:

        if function is target_function:
            continue

        if target_function < function:
            print("%s < %s" % (target_function, function))

        elif target_function > function:
            print("%s > %s" % (target_function, function))

        elif target_function == function:
            print("%s = %s" % (target_function, function))

    print("--------------------", "\n")

