from utils.encoding import encode_base64


class Registers:
    def __init__(self):
        self.registers = [0] * 16

    def add(self, val, dest_reg, src_reg):
        self.registers[dest_reg] = self.registers[src_reg] + val

    def mov(self, src_reg, dest_reg):
        self.registers[dest_reg] = self.registers[src_reg]

    def store(self, val, dest_reg):
        self.registers[dest_reg] = val


def sum_registers(registers):
    return sum(registers)


def execute_program(instructions: list[str]):
    registers = Registers()

    for instruction in instructions:
        instruction = instruction.replace("\"", "")
        parts = instruction.split()

        if parts[0] == "ADD":
            val = int(parts[1])
            dest = int(parts[3][1:])
            src = int(parts[2][1:])
            registers.add(val, dest, src)
        elif parts[0] == "MOV":
            src = int(parts[1][1:])
            dest = int(parts[2][1:])
            registers.mov(src, dest)
        elif parts[0] == "STORE":
            val = int(parts[1])
            dest = int(parts[2][1:])
            registers.store(val, dest)

    return encode_base64(sum_registers(registers.registers))
