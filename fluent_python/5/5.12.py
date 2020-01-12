def clip(text: str, max_len=80):
    """
    在max_len前面或者后面的第一个空格处截断文本
    :param text:
    :param max_len:
    :return:
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
        if space_after >= 0:
            end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__,clip.__code__.co_varnames)