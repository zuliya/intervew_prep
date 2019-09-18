take_out = [1, 3, 5]
dine_in = [2, 4, 6]
served = [1, 2, 3, 5, 4, 6]


def cake_ordering(t_o,d_i,served):
    take_out_current_index = 0
    dine_in_current_index = 0
    served_in_current_index = 0
    # Go through served orders array
    while served_in_current_index < len(served):
        # If matches take out array increment index
        if take_out_current_index < len(t_o) and served[served_in_current_index] == t_o[take_out_current_index]:
            take_out_current_index += 1
        # If matches dine in array increment index
        elif dine_in_current_index < len(d_i) and served[served_in_current_index] == d_i[dine_in_current_index]:
            dine_in_current_index += 1
        # If does not match any of the latest orders means not FIFO
        else:
            return "Not FIFO"

        served_in_current_index += 1

    return "Is FIFO"


print(cake_ordering(take_out,dine_in,served))
