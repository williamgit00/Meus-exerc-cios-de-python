def create_character(name, stat1, stat2, stat3):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
       return "The character should have a name"  
    if len(name) > 10:
       return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    for stat in (stat1, stat2, stat3):
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers"
    for stat in (stat1, stat2, stat3):
        if stat < 1:
            return "All stats should be no less than 1"   
    for stat in (stat1, stat2, stat3):
        if stat > 4:
            return "All stats should be no more than 4"     
    if (stat1 + stat2 + stat3) != 7:
        return "The character should start with 7 points"       

    return (
    f"{name}\n"
    f"STR {'●' * stat1}{'○' * (10 - stat1)}\n"
    f"INT {'●' * stat2}{'○' * (10 - stat2)}\n"
    f"CHA {'●' * stat3}{'○' * (10 - stat3)}"
