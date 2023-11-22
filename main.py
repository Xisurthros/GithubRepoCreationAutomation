import sys
from local.classes.helpers import Helpers

if __name__ == '__main__':
    helpers = Helpers()

    runnable_functions = {
        "help": helpers.help,
        "make_repo": helpers.make_repo,
        "get_repos": helpers.get_repos
    }

    try:
        function_name = sys.argv[1] if len(sys.argv) > 1 else None
        if function_name in runnable_functions:
            args = sys.argv[2:]
            print(runnable_functions[function_name](*args))
        else:
            print("Invalid function name" if function_name else "No arguments provided. Please specify a function name.")
            helpers.help()
    except IndexError:
        print("Error: Insufficient arguments provided.")
