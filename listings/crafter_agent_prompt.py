# Bad example (too specific):
def multiply_3_and_7():
    return 3 * 7

# Good example (general):
def multiply(a: float, b: float) -> float:
    """
    Arguments:
    a: the first number to multiply
    b: the second number to multiply
    Returns:
    The product of a and b
    """
    return a * b


# Bad example (hardcoded/placeholder result):
def search_papers(query: str) -> str:
    return "Results about " + query  # WRONG: never return hardcoded strings

# Good example (real API call):
def search_papers(query: str) -> str:
    """
    Arguments:
    query: the search query string
    Returns:
    A string with real results fetched from the API
    """
    import arxiv
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=3)
    results = [p.title + ": " + p.summary[:200] for p in client.results(search)]
    return "\\n".join(results)    

# Bad example: Too specific
def get_oldest_blu_ray_title(spreadsheet_path: str) -> str:
    """
    Analyzes a spreadsheet to find the oldest Blu-Ray title.

    Arguments:
    spreadsheet_path: The file path to the spreadsheet (e.g., 'C:/Users/user/data.xlsx').

    Returns:
    The title of the oldest Blu-Ray as it appears in the spreadsheet.
    """
    import pandas as pd

    df = pd.read_excel(spreadsheet_path)

    # Assuming 'Format' column for media type and 'Recording Date' for date
    blu_rays = df[df['Format'] == 'Blu-Ray']

    if blu_rays.empty:
        return "No Blu-Ray titles found."

    # Ensure 'Recording Date' is in datetime format for proper comparison
    blu_rays['Recording Date'] = pd.to_datetime(blu_rays['Recording Date'])

    oldest_blu_ray = blu_rays.sort_values(by='Recording Date', ascending=True).iloc[0]

    return oldest_blu_ray['Title']

# Good example
def open_excel_files(excel_path: str):
    """
    Analyzes a spreadsheet.

    Arguments:
    excel_path: The file path to the spreadsheet (e.g., 'C:/Users/user/data.xlsx').

    Returns:
    The excel file in string
    """
    import pandas as pd

    df = pd.read_excel(excel_path)
    return df.to_string()
