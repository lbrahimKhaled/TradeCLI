import re

# matches: variable = TransformationName{config_args}{series_args}
LINE_PATTERN = re.compile(r"(\w+)\s*=\s*(\w+)\{([^}]*)\}\{([^}]*)\}")

#if the transformation requires some arguments this will correctly ingest them and extract them
def parse_args(raw: str) -> list[str]:
    return [a.strip() for a in raw.split(",") if a.strip()]

def parse_script(script: str) -> list[tuple[str, str, list[str], list[str]]]:
    """"
    this will return the list of statements enetered by the user
    each statement is a tuple of the variable (e.g. price, fast, slow ...etc), the transformation used (e.g. EMA ...etc)
    the input config (e.g. the alpha for the EMA) and the input series (e.g. the price series in the EMA)
    """
    statements = []
    for line in script.splitlines():
        line = line.strip() # so that we getting the transformations is cleaner
        if not line: # no script (later do some error handling)
            continue
        match = LINE_PATTERN.match(line)
        if not match:
            continue
        variable, transformation, config_raw, series_raw = match.groups()
        statements.append((variable, transformation, parse_args(config_raw), parse_args(series_raw)))
    return statements
