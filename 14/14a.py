recipe_list = [3,7]
positions = [0,1]
puzzle_input = 509671
recipes_to_get = 10

while len(recipe_list) < puzzle_input + recipes_to_get:
    position_sum = recipe_list[positions[0]] + recipe_list[positions[1]]
    recipe_list.extend([int(char) for char in str(position_sum)])
    positions = [(positions[0]+(1+recipe_list[positions[0]]))%len(recipe_list), (positions[1]+(1+recipe_list[positions[1]]))%len(recipe_list)]

print(''.join([str(num) for num in recipe_list[-recipes_to_get:]]))