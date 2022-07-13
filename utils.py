

def perform_query(cmd, val, file):
    if cmd == "filter":
        res = filter(lambda x: val in x, file)
        return list(res)

    if cmd == "map":
        val = int(val)
        return [x.split(" \"")[val] for x in file]

    if cmd == "unique":
        return list(set(file))

    if cmd == "sort":
        if val == "asc":
            return sorted(file)
        elif val == "desc":
            return sorted(file, reverse=True)

    if cmd == "limit":
        val = int(val)
        return list(file)[0:val]
