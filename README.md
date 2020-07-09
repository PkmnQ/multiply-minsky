# multiply-minsky

There's a single register.

The code is made of instructions separated by spaces.

The instructions are made of 3 numbers separated by spaces.

The instructions in the format `a b c` do this:

1. Multiply the register by `a`

2. If the register is divisible by `b`, proceed to step 3, otherwise, move to the next instruction.

3. Divide the register by `b`.

4. Goto instruction `c`.
