def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split(' ')
    return [int(a) for a in data]

class Branch():
    def __init__(self, instructions):
        self.child_count = instructions[0]
        self.metadata_count = instructions[1]
        self.instructions_to_give = instructions[2:]
        self.children, self.metadata, self.remaining_instructions = self.create_children()

    def create_children(self):
        if self.child_count == 0:
            return [], self.instructions_to_give[:self.metadata_count], self.instructions_to_give[self.metadata_count:]
        else:
            child_list = []
            instructions = self.instructions_to_give
            for i in range(self.child_count):
                child = Branch(instructions)
                instructions = child.remaining_instructions
                child_list.append(child)
            return child_list, child_list[-1].remaining_instructions[:self.metadata_count], child_list[-1].remaining_instructions[self.metadata_count:]
    
    def calculate_value(self):
        return_sum = 0
        if self.child_count == 0:
            return_sum = sum(self.metadata)
        else:
            for ix in self.metadata:
                if ix <= self.child_count:
                    return_sum += self.children[ix-1].calculate_value()
        return return_sum

def sum_tree(branch):
    branch_sum = 0
    for child in branch.children:
        branch_sum += sum_tree(child)
    return branch_sum + sum(branch.metadata)


instruction_list = get_input()
root = Branch(instruction_list)

print(root.calculate_value())
    