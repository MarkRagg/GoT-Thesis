

def symbolic_integration(expression: str, variable: str) -> str:
    """
    Performs symbolic integration of a given mathematical expression with respect to a specified variable.

    Arguments:
    expression: The mathematical expression to integrate (e.g., "x**2 * exp(x**2)").
    variable: The variable with respect to which to integrate (e.g., "x").

    Returns:
    A string representation of the indefinite integral of the expression.
    """
    from sympy import integrate, sympify, Symbol, exp

    try:
        # Define the symbol
        x = Symbol(variable)
        
        # Sympy's integrate function can handle expressions with exp
        integrated_expr = integrate(sympify(expression), x)
        return str(integrated_expr)
    except Exception as e:
        return f"Error during integration: {e}"