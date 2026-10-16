test_settings =  {'theme': 'light'}

def add_setting (settings, new_setting):
    key, val = new_setting
    key = key.lower()
    val = val.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = val
    return f"Setting '{key}' added with value '{val}' successfully!"

def update_setting (update, new_update):
    key, val = new_update
    key = key.lower()
    val = val.lower()  


    if key in update:
        update[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting (delete, key):
    key= key.lower()
    
    if key in delete:
        del delete[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"    

def view_settings(settings):
    if not settings:
        return "No settings available."

    else:
        result = "Current User Settings:"
        for key, val in settings.items():
            result+=f"\n{key.capitalize()}: {val}"
    return result +"\n"
print(view_settings(test_settings))
