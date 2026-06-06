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
        upper_half = []
        while True: #creation of one diamond by creating separate string for each new line
            diamonds = []
            final_diamond = []
            #initial diamond boundary
            initial_space = size * " "
            gap = 2 * " " * gap_ind
            diamonds.append(list(f"{initial_space}/{gap}\\"))
            if size == 0:
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
            text_curr = "".join(final_diamond)
            upper_half.append(text_curr)
            upper_half.append('\n')
            gap_ind += 1
            size -= 1
        upper_text = "".join(upper_half)
        print(upper_text, end='')

        mapping_lower = str.maketrans("/\\", "\\/")
        reversed_lower = upper_text.translate(mapping_lower)

        for line in reversed_lower.splitlines()[::-1]:
            print(line)





main()

