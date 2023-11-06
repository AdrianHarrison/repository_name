import argparse # Grant access to resorces from the argparse standard library (https://docs.python.org/3/library/argparse.html)

########################################
## HOW TO READ A (SIMPLE) PYTHON FILE ##
########################################

# 1. Code execution is top down, 
# 2. Control structures (if, elif, else, for, while), functions, and classes use whitespace indentation 
# 3. Organization:
#       a. Imports (files containing python code, the python standard library, or pip modules installed from pypi.org)
#       a. Class definitions (not used here)
#       a. Variable definitions
#       b. Function definitions
#       c. Entrypoint (only used by `__main__` files)

# disclaimer: I am not pulling out any big tools for this and trying to keep
# it as barebones as possible. if someone tells you that you can do this better
# in numpy/pandas/scipy they're absolutely right

# define constants first
GEAR_RATIO  = 4.41
WHEEL_DIA   = 0.4572
PEAK_KW     = 72
PEAK_NM     = 120
CONT_NM     = 80
MAX_RPM     = 6000
MASS_KG     = 277

ACCUM_EFFI  = 0.95
CONT_EFFI   = 0.95
MOTOR_EFFI  = 0.92

FRONT_M2    = 1.0
AIR_KGM2    = 1.18
DRAG_COEFF  = 0.3
RR_COEFF    = 0 # fill this in when you know it

# functions are how you isolate your code into managable chunks and are defined by the `def` keyword
# for this problem all you need to do is basically work out the order of operations and return the result

# stub method for rolling resistance, your calculations go here, 
# assign the final value to the `result` variable
def calculate_rolling_resistance(fr:float, cr:float, fn:float) -> float:
    result = 0

    print ("Calling Rolling Resistance Function:")
    print(f"""Current values:
             fn = {fn}
             cr = {cr}
             fn = {fn}""")

    
    return result

# stub method for drag_force, your calculations go here
# assign the final value to the `result` variable
def calculate_drag_force(fp, p, a, ca, v) -> float:
    result = 0
    print ("Calling Drag Force Function:")
    print(f"""Current values:
             fp = {fp}
             p  = {p}
             a  = {a}
             ca = {ca}
             v  = {v}""")
    
    
    return result

# The main loop / routing function
def main(args:argparse.Namespace) -> None:
    # BASIC HUNT & PRINT DEBUGGING:
    # if something isn't working, check your variables by passing them to a print() function
    print(args)

    # get the function name
    func = args.function

    if func == "roll":
        
        # grab the variables we want
        fr = args.roll_force
        cr = args.roll_resist
        fn = args.norm_force

        # and pass them into the rolling resist function
        result = calculate_rolling_resistance(fr, cr, fn)
        print(f"Roll Resist = {result}")
    elif func == "drag":
        
        # grab the variables we want
        p = args.fluid_density
        v = args.velocity
        fp = args.drag_force

        # inline ternary operator, basically an if / else statement in one line
        # a `None` is a null or unassigned variable, so if we don't provide it the
        # default const is used
        ca = args.drag_force if args.drag_force else DRAG_COEFF
        # same approach to frontal area
        a = args.frontal_view if args.frontal_view else FRONT_M2

        # pass everything to the drag force function
        result = calculate_drag_force(fp, p, a, ca,v)
        print(f"Drag Force = {result}")
    else:
        print("INVALID FUNCTION")

# optional standalone module setup
# if the module is called via `python ./single_file_cli_utility.py`
# it will adopt the behavior below as it is specified as the "__main__" program
if __name__ == "__main__":

    # Instantiate and configure the parser object
    parser = argparse.ArgumentParser(
        prog="SingleFileCliUtility",
        description="Takes a function name / parameter set and calls a matching function.",
    )

    # Assign CLI flags to the parser so we can cearly label input values.
    # in a more thurough design you'd include each potential function as a subparser
    # allowing function-specific flags so you don't have to dump all your variables into
    # one big list

    # what function to call
    parser.add_argument("-f", "--function", help="Function to run.", choices=['roll', 'drag'])

    # parameters for rolling resistance
    parser.add_argument("-fr", "--roll_force", help="Force due to rolling resistance.")
    parser.add_argument("-cr", "--roll_resist", help="Rolling resistance coefficient.")
    parser.add_argument("-fn", "--norm_force", help="Normal force.")

    # parameters for drag force
    parser.add_argument("-fp", "--drag_force", help="Force due to drag.")
    parser.add_argument("-p", "--fluid_density", help="Desnity of the fluid.")
    parser.add_argument("-v", "--velocity", help="Velocity of the fluid moving past the vehicle.")

    # i left this one in in case you wanted to override DRAG_COEFF or FRONT_M2
    parser.add_argument("-ca", "--coeff_drag", help="Coefficient drag of the vehicle.")
    parser.add_argument("-a", "--frontal_view", help="Frontal view area of the vehicle.")

    # fetch all the provided args
    args = parser.parse_args()

    # start the main loop with all the provided args
    main(args)