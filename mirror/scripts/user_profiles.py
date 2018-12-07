# stored user profiles


def get_user():
    names = ['User 1', 'User 2', 'User 3']
    bios = ['Bio 1', 'Bio 2', 'Bio 3']
    user_data = dict()
    user_data["names"] = names
    user_data["bio"] = bios
    result = list()
    for name, bio in zip(user_data["names"], user_data["bio"]):
        user = dict()
        user["name"] = name
        user["bio"] = bio
        result.append(user)
    return result
