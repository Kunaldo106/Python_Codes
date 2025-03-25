#conversion of celcius to fehrenheit of water temperature

def TempConversion(C):
    return C*(9/5)+32
    
Water_BP= 100
Water_FP= 0

Water_BP_F= TempConversion(Water_BP)
Water_FP_F= TempConversion(Water_FP)

print(f"The Boiling point of water : {Water_BP_F} F")
print(f"The Freezing point of water : {Water_FP_F} F")
