def same_by(characteristic, objects):
    if not objects:
        return True
    return len(set(map(characteristic, objects)))    == 1
