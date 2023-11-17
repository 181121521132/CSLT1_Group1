bits = input("Bits: ")

while bits != "":
  if bits.count("0") + bits.count("1") != 8 or len(bits) != 8:
    print("Error")
  else:
    ones = bits.count("1")

    if ones % 2 == 0:
      print("Bit 0")
    else:
      print("Bit 1")
  bits = input("Bits: ")