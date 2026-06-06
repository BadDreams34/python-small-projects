"""Diamonds
Generates ASCII art of Diamonds of various sizes."""

import time
print("Diamonds")
print("This program generates ASCII art of Diamonds of various sizes.")


def main():
    i = 0
    num = 6
    while i<num:
        diamond_generator(i,"up")
      #  diamond_generator(i, "down") #im on this line step out should take me out of the current scope but,,,
        print(flush=True)
        print(flush=True)
        i+=1
    time.sleep(4)



def diamond_generator(siz,orientation):
    if orientation == 'up':
        size = siz
        gap_ind = 0



        # firstly reduce the gap and like create a diamond and another one but this time

        while True: #creation of one diamond by creating separate string for each new line
            diamonds = []
            final_diamond = []
            #initial diamond boundary
            initial_space = size * " "
            gap = 2 * " " * gap_ind
            diamonds.append(list(f"{initial_space}/{gap}\\"))
            # if all the lines are being stored
            if size == 0:
                print(f"{initial_space}/{gap}\\")
                break

            #check for additional diamonds with gap
            if len(gap) != 0 and len(gap) % 2 == 0:
                dis = 1
                gap_reduced = len(gap) - 2
                for i in range(len(gap) // 2):
                    distance = " " * dis
                    dis +=1
                    diamonds.append(list(f"{distance + initial_space}/{gap_reduced * " "}\\{distance}"))
                    gap_reduced -= 2

            # print the final diamond
            for items in zip(*diamonds):
                for element in items:
                    element_added = False
                    if element != " ":
                        element_added = True
                        final_diamond.append(element)
                        break
                if not element_added:
                    final_diamond.append(" ")
            print("".join(final_diamond))
            gap_ind += 1
            size -= 1



    # elif orientation == 'down':
    #     size = 0
    #     i = siz
    #     dis = 0
    #     distance = " " * dis
    #     while True:
    #         initial_space = distance + size * " "
    #         gap = 2 * " " * i
    #         print(f"{initial_space}\\{gap}/",flush=True)
    #         if size == siz or i == 0:
    #             break
    #         size += 1
    #         i -= 1


main()

