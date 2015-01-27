__author__ = 'ysahn'

def segment_text(text, maxchars = 100):
    text_list = []

    if len(text) < maxchars:
        text_list.append(text)
        return text_list

    next_start_pos = 0;
    last_blank_pos = 0;

    cursor = 0;
    segment_char_cnt = 0;
    for char in text:

        if char in ' \t\n':
            last_blank_pos = cursor

        curr_len = cursor - next_start_pos + 1
        if curr_len == maxchars:
            # @todo handle error when a word is bigger than the maxchar
            text_segment = text[next_start_pos: last_blank_pos+1]
            text_list.append(text_segment)
            next_start_pos = last_blank_pos + 1

        cursor += 1

    if next_start_pos != cursor:
        text_segment = text[next_start_pos: cursor+1]
        text_list.append(text_segment)

    return text_list