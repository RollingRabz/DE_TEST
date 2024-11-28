def word_mesh(words: list[str]):
    def get_mesh(a, b):
        # Find mesh point
        for i in range(1, min(len(a), len(b)) + 1):    # get the max character we can check which is min of two words selected
            if a[-i:] == b[:i]:                        # If found mesh point return the mesh word
                return a[-i:]
        return ""                                      # If mesh point not found return empty string

    ans = ""                                           # created empty string for store output
    for i in range(len(words) - 1):                    # Loop through all words in list
        mesh = get_mesh(words[i], words[i + 1])        # take input into above function
        if not mesh:                                   # If mesh point not found return failed to mesh
            return "failed to mesh"
        ans += mesh                                    # Merge the mesh word together
    return ans


# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"