import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

registered_functions = []
searched_for_functions = False

class FunctionSet():
    """
    This class holds a range of values (the domain) and a set of functions to be applied
    to each value (the range)
    """

    def __init__(self, num_set, functions):
        """
        set the domain and create a dict of all the
        :param num_set:
        :param functions:
        :return:
        """
        plt.title("Plotting fun")

        self.num_set = num_set

        self.function_set = {}
        for function in functions:
            self.add_function(function)

        # plt.ion()
        # plt.show()

    def add_function(self, function):
        self.function_set[function.name] = [function.function(x) for x in self.num_set]

    def plot_function(self, key, interactive):
        """
        :param key: the string name of the function in function_set to plot
        """

        function_values = self.function_set[key]
        plt.plot(self.num_set, function_values, label=key)
        plt.legend(loc=2)

        if interactive:
            plt.pause(2)
            plt.draw()


    def graph(self, interactive=False):
        """
        This method plots all functions in function_set onto one plot, with num_set as the x axis and
        the function values as the y axis
        """
        for function in self.function_set:
            """
            in this loop, 'function' is a string and also a key to the range values
            """
            self.plot_function(function, interactive)

        plt.show(not interactive)

    def graph_interactive(self):

        self.graph(interactive=True)
        while True:
            self.receive_input()


    def receive_input(self):
        func_name = input("Expression name: ")
        in_func = input("Enter expression: ")

        def user_function(x):
            return eval(in_func)

        func_rep = Function(func_name, user_function)
        registered_functions.append(func_rep)
        self.add_function(func_rep)

        self.plot_function(func_name, True)


class Function():
    """
    This should take in a callable function and wrap it to provide comparison functionality
    """

    def __init__(self, name, function):
        self.name = name
        self.function = function  # this should be a callable

    def __str__(self):
        return self.name

    def __gt__(self, other):
        if self.function(999999999) > other.function(999999999):
            return True

        return False

    def __lt__(self, other):
        if self.function(999999999) < other.function(999999999):
            return True

        return False

    # TODO Needs to come before the other conditionals and be given some delta % logic
    def __eq__(self, other):
        if self.function(999999999) == other.function(999999999):
            return True

        return False


def register_function(name):
    """
    To be used as a decorator to decorate a new function to be added to the globabl list
    :param func: a callable function
    """
    def decorator(fn):
        func_rep = Function(name, fn)
        registered_functions.append(func_rep)
        return fn
    return decorator


def get_functions():
    """
    Imports the functions in the functions file so that their decorators get ran and everything gets registered
    :return: the list of global functions
    """
    # this allows the function to be called more than once without trying to re-import all of the functions
    global searched_for_functions
    if not searched_for_functions:
        from . import functions
        searched_for_functions = True

    return registered_functions
