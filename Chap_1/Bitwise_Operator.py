# Bitwise Operator

a = 5  # 101
b = 3  # 001

# Bitwise AND (&): Performs a bitwise AND operation between the corresponding bits of two operands.
# The result is 1 only if both bits are 1.

c = a & b
print(f"Result of a & b is {c}")
# Output: 1 -> (001)

# Bitwise OR (|): Performs a bitwise OR operation between the corresponding bits of two operands.
# The result is 1 if at least one of the bits is 1.

c = a | b
print(f"Result of a | b is {c}")
# Output: 7 -> (111)

# Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation between the corresponding bits of two operands.
# The result is 1 if the bits are different.

c = a ^ b
print(f"Result of a ^ b is {c}")
# Output: 6 -> 110

# Bitwise NOT (~): Inverts all the bits of the operand.
# It is a unary operator (operates on a single operand).

c = ~a
print(f"Result of ~a is {c}")
# Output: -6 (~0101 = -(0110+1) = -6)

# Bitwise Left Shift (<<): Shifts the bits of the first operand to the left by the number of positions specified
# by the second operand.
# Zeros are shifted in from the right.

c = a << 2
print(f"Result of a << 2 is {c}")
# Output: 20 (5 << 2 = 0101 << 2 = 0001 0100)

# Bitwise Right Shift (>>): Shifts the bits of the first operand to the right by the number of positions
# specified by the second operand.
# Zeros are shifted in from the left.

c = a >> 1
print(f"Result of a >> 1 is {c}")
# Output: 2 (5 >> 1 = 0101 >> 1 = 0010)

