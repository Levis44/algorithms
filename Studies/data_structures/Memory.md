[[Memory.excalidraw]]

- Your program will always store a variable in a memory slot or a series of memory slots that are free
- If your program needed more than one memory block to store information (variable), it would store it in back to back (sequence) memory slots
- There are limited memory slots in the computer, that's why space complexity is relevant
- Accessing memory slots is very quickly!
- Stored in base two format (binary)
- 1 memory slot = 8 bits (1 byte)

Memory = bits 
0 0 1 0 1

1 memory slot = 8 bits = 1 byte
base 2 system - base 2 format

1 = 0000 0001
2 = 0000 0010
3 = 0000 0011
4 = 0000 0100

$$
1 byte = 2ˆ8 = 256
$$
- In Java Int = 32 bits (4 bytes) and Long = 64 bits (8 bytes)
## Pointers
Memory address are Stored in binary (base 2 format)
You can store in a memory slot the address of other memory slot

Useful to refer data "far away", that has memory slots taken between the reference