def load_input(day, test_mode=False, sections=False):

    """Load Advent of Code input data from a text file.

    Args:
        day (str or int): Identifier for the input file. This typically matches the
            Advent of Code day number, but any string matching a file name is
            accepted.
        test_mode (bool, optional): If True, load from ``input/test/``.
            If False, load from ``input/actual/``. Defaults to False.
        sections (bool, optional): If True, split the input into sections separated
            by blank lines. Defaults to False.

    Returns:
        list[str] or list[list[str]]: The loaded input. When ``sections`` is False, a
            list of lines. When ``sections`` is True, a list of sections, where each
            section is a list of lines.
    """
    #Derrive input file name
    if test_mode:
        data_subdir = "test"
    else:
        data_subdir = "actual"

    dir_path = f"./input/{data_subdir}/{str(day)}.txt"

    #Open and read the file
    with open(dir_path) as f:
        lines = f.read().split('\n')

    #If the file only contains 1 section, then return as is.
    if not sections:
        return lines

    #Otherwise, split input into sections and then return
    else:
        section = 0
        input_var = [[]]
        for line in lines:
            if line == "":
                section += 1
                input_var.append([])
            else:
                input_var[section].append(line)

        return input_var
    
def line_to_arr(line, delimiter=",", convert_to_num=False):
    """Convert a string line containing multiple pieces of information into an 
    array of values.

    Args:
        line (str): String containing multiple pieces of information.
        delimiter (str): String of the delimiter seperating values in the line.
        convert_to_num (Boolean): When True, convert values to numeric integers.

    Returns:
        values (array): Array of values.
    """

    #Split using delimiter
    values_raw = line.split(delimiter)

    #Trim remaining line space
    values = [x.strip() for x in values_raw]
    values = [x for x in values if x != ""]

    #If needed, convert values to integers
    if convert_to_num:
        values = [int(x) for x in values]

    return values