recipe_list = [3,7]
positions = [0,1]
puzzle_input = [5,0,9,6,7,1]
recipes_to_get = len(puzzle_input)

while True:
    position_sum = recipe_list[positions[0]] + recipe_list[positions[1]]
    recipe_list.extend([int(char) for char in str(position_sum)])
    positions = [(positions[0]+(1+recipe_list[positions[0]]))%len(recipe_list), (positions[1]+(1+recipe_list[positions[1]]))%len(recipe_list)]
    if recipe_list[-recipes_to_get:] == puzzle_input:
        print(len(recipe_list)-len(puzzle_input))
        break
    elif recipe_list[-recipes_to_get-1:-1] == puzzle_input:
        print(len(recipe_list)-len(puzzle_input)-1)
        break
