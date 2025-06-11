def expand_string(input_str: str) -> str:
    stack: list[tuple[int, list[str]]] = []
    current_list: list[str] = []
    cur_ind: int = 0

    while cur_ind < len(input_str):
        if input_str[cur_ind].isdigit():
            num: int = 0
            while cur_ind < len(input_str) and input_str[cur_ind].isdigit():
                num = num * 10 + int(input_str[cur_ind])
                cur_ind += 1
            if cur_ind < len(input_str) and input_str[cur_ind] == '[':
                stack.append((num, current_list))
                current_list = []
                cur_ind += 1
            else:
                current_list.append(str(num))
        elif input_str[cur_ind] == ']':
            if stack:
                multiplier, previous_list = stack.pop()
                current_list = previous_list + (current_list * multiplier)
            else:
                raise ValueError("Unmatched closing bracket ']'")
            cur_ind += 1
        else:
            if input_str[cur_ind] == '[':
                raise ValueError("Opening bracket '[' without preceding number")
            else:
                current_list.append(input_str[cur_ind])
            cur_ind += 1

    if stack:
        raise ValueError("Unmatched opening bracket '['")

    return ''.join(current_list)
