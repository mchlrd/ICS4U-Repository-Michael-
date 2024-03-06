#Gigi likes to play with squares. She has a collection of equal-sized square tiles. Gigi wants to arrange some or all of her tiles on a table to form a solid square. What is the side length of the largest possible square that Gigi can build?

#For example, when Gigi has 9 tiles she can use them all to build a square whose side length is 3. But when she has only 8 tiles, the largest square that she can build has side length 2.

#Write a program that inputs the number of tiles and then prints out the maximum side length. You may assume that the number of tiles is less than ten thousand.
import math
def largest_square(num_tiles, maximum_num):
    num_tiles = int(input("Enter the number: "))

    maximum_num = math.sqrt(num_tiles)
    maximum_num = math.floor(maximum_num)

    finalm = f"The largest square has side length of {maximum_num}"

    print(finalm)

largest_square(num_tiles=int, maximum_num=int)