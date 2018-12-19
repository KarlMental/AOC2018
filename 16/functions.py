def addr(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] + registers[instruction[1]]
    return registers

def addi(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] + instruction[1]
    return registers

def mulr(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] * registers[instruction[1]]
    return registers

def muli(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] * instruction[1]
    return registers

def banr(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] & registers[instruction[1]]
    return registers

def bani(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] & instruction[1]
    return registers

def borr(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] | registers[instruction[1]]
    return registers

def bori(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]] | instruction[1]
    return registers

def setr(instruction, registers):
    registers[instruction[2]] = registers[instruction[0]]
    return registers

def seti(instruction, registers):
    registers[instruction[2]] = instruction[0]
    return registers

def gtir(instruction, registers):
    registers[instruction[2]] = 1 if instruction[0] > registers[instruction[1]] else 0
    return registers

def gtri(instruction, registers):
    registers[instruction[2]] = 1 if registers[instruction[0]] > instruction[1] else 0
    return registers

def gtrr(instruction, registers):
    registers[instruction[2]] = 1 if registers[instruction[0]] > registers[instruction[1]] else 0
    return registers

def eqir(instruction, registers):
    registers[instruction[2]] = 1 if instruction[0] == registers[instruction[1]] else 0
    return registers

def eqri(instruction, registers):
    registers[instruction[2]] = 1 if registers[instruction[0]] == instruction[1] else 0
    return registers

def eqrr(instruction, registers):
    registers[instruction[2]] = 1 if registers[instruction[0]] == registers[instruction[1]] else 0
    return registers