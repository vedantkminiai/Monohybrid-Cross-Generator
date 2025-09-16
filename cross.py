import random
import time


#going to be used to put dots or space between each section to make it legible
def spacer(yN=0, sec = 2):
  if yN == 0:
    for i in range(4):
      print(".", end="", flush=True)
      time.sleep(0.5)
  else:
    time.sleep(sec)
    print("\n\n")


#checks if trait input is valid
def verify(thing):
  while thing != "1" and thing != "2" and thing != "3":
    spacer(1)
    print("Invalid Input")
    thing = input("Trait: ")
  return thing


#checks if dad trait input is within given selection of options
def dadTraitVerify(possibleTraitsList, dad, name):
  while not (dad in possibleTraitsList):
    spacer(1)
    print("Invalid Input")
    dad = input("Enter Dad " + name + ": ").lower()
  return dad


#checks if mom trait input is within given selection of options
def momTraitVerify(possibleTraitsList, mom, name):
  while not (mom in possibleTraitsList):
    spacer(1)
    print("Invalid")
    mom = input("Enter Mom " + name + ": ").lower()
    spacer(1)
  return mom


#asks user for mom trait and dad trait, then checks if they are valid
def trait(trait):
  spacer(1, 1)
  if trait == "1":
    #option for eye colour
    name = "Eye Colour"
    print("Pick from eye colour: brown, blue, green, hazel")
    spacer(1, 1)
    dad = input("Enter Dad Eye Color: ").lower()
    dad = dadTraitVerify(possibleEyeColor, dad, name)
    spacer(1, 1)
    mom = input("Enter Mom Eye Color: ").lower()
    mom = momTraitVerify(possibleEyeColor, mom, name)
  elif trait == "2":
    #option for hair colour
    name = "Hair Colour"
    print("Pick from hair color: Black, brown, blonde, ginger")
    spacer(1, 1)
    dad = input("Enter Dad Hair Color: ").lower()
    dad = dadTraitVerify(possibleHairColor, dad, name)
    spacer(1, 1)
    mom = input("Enter Mom Hair Color: ").lower()
    mom = momTraitVerify(possibleHairColor, mom, name)
  elif trait == "3":
    #option for hair type
    name = "Hair Texture"
    print("Pick from hair texture: curly, straight, wavy")
    spacer(1, 1)
    dad = input("Enter Dad Hair Texture: ").lower()
    dad = dadTraitVerify(possibleHairTexture, dad, name)
    spacer(1, 1)
    mom = input("Enter Mom Hair Texture: ").lower()
    mom = momTraitVerify(possibleHairTexture, mom, name)
  #creates and returns list of mom and dad's characteristics for each trait
  parents = [dad, mom]
  return parents


#turns mom and dad's eye colour characteristics into alleles
def eyeToAllele(mom, dad):
  momAllele = ""
  dadAllele = ""
  if mom == "brown":
    momAllele = "EE"
  elif mom == "hazel" or mom == "green":
    momAllele = "Ee"
  elif mom == "blue":
    momAllele = "ee"
  if dad == "brown":
    dadAllele = "EE"
  elif dad == "hazel" or dad == "green":
    dadAllele = "Ee"
  elif dad == "blue":
    dadAllele = "ee"
  return dadAllele, momAllele

#function that turns hair colour to alleles
def hairColorToAllele(mom, dad):
  momAllele = ""
  dadAllele = ""
  if mom == "black":
    momAllele = "BB"
  elif mom == "brown" or mom == "ginger":
    momAllele = "Bb"
  elif mom == "blonde":
    momAllele = "bb"
  if dad == "black":
    dadAllele = "BB"
  elif dad == "brown" or dad == "ginger":
    dadAllele = "Bb"
  elif dad == "blonde":
    dadAllele = "bb"
  return dadAllele, momAllele

#function that turns hair texture to alleles
def hairTextureToAllele(mom, dad):
  mom = mom.lower()
  dad = dad.lower()
  momAllele = ""
  dadAllele = ""
  if mom == "curly":
    momAllele = "CC"
  elif mom == "wavy":
    momAllele = "Cs"
  elif mom == "straight":
    momAllele = "ss"
  if dad == "curly":
    dadAllele = "CC"
  elif dad == "wavy":
    dadAllele = "Cs"
  elif dad == "straight":
    dadAllele = "ss"

  return dadAllele, momAllele

#function that generates and displays monohybrid cross 
def diHybridCross(parents, b=0):
  dadAlleleOne = parents[1][1]
  dadAlleleTwo = parents[1][0]
  momAlleleOne = parents[0][1]
  momAlleleTwo = parents[0][0]
  if dadAlleleOne.isupper():
    possibleAllele1 = dadAlleleOne + momAlleleOne
    possibleAllele3 = dadAlleleOne + momAlleleTwo
  else:
    possibleAllele1 = momAlleleOne + dadAlleleOne
    possibleAllele3 = momAlleleTwo + dadAlleleOne

  if dadAlleleTwo.isupper():
    possibleAllele2 = dadAlleleTwo + momAlleleOne
    possibleAllele4 = dadAlleleTwo + momAlleleTwo
  else:
    possibleAllele2 = momAlleleOne + dadAlleleTwo
    possibleAllele4 = momAlleleTwo + dadAlleleTwo
  if b == 0:
    spacer(1, int(1/2))
    print("Generating Dihybrid Cross")
    spacer()
    print("\n")
    print(
        f"{dadAlleleOne:<8}{dadAlleleTwo:>5}\n{momAlleleOne:<10}{possibleAllele1:<5}{possibleAllele2:>5}\n\n{momAlleleTwo:<10}{possibleAllele3:<5}{possibleAllele4:>5}"
    )
    spacer()
    print("\nThe Monohybrid Cross is a method of creating children from two parents. It finds all possible combinations of the parent's alleles which can occur in the children.")
  allelePossibility = [
      possibleAllele1, possibleAllele2, possibleAllele3, possibleAllele4
  ]
  return allelePossibility

#function that determines the probability of each kid having a certain trait 
def possibilityChecker(allelePossibilityList, printYN = 0):
  dominant_number = 0
  recessive_number = 0
  mix_number = 0
  dominantPercent = 0
  recessivePercent = 0
  mixedPercent = 0
  for i in allelePossibilityList:
    if i[0].isupper() and i[1].isupper():
      dominant_number += 1
    elif i[0].isupper() and i[1].islower():
      mix_number += 1
    elif i[0].islower() and i[1].islower():
      recessive_number += 1
  spacer(1, 3)
  if printYN == 1:
    if dominant_number == 4:
      print(f"You have 100% chance to get {dominant}")
      dominantPercent = 1
    elif dominant_number == 2:
      if recessive_number == 2:
        print(
            f"You have a 50% chance to get {dominant} and a 50% chance to get {recessive}"
        )
        dominantPercent = 0.5
        recessivePercent = 0.5
      elif mix_number == 2:
        print(
            f"You have a 50% chance to get {dominant} and a 50% chance to get {mixed}"
        )
        dominantPercent = 0.5
        mixedPercent = 0.5
    elif dominant_number == 1:
      if mix_number == 2:
        print(
            f"You have a 25% chance to get {dominant}, a 25% chance to get {recessive}, and a 50% chance to get {mixed}"
        )
        dominantPercent = 0.25
        recessivePercent = 0.25
        mixedPercent = 0.5
    elif dominant_number == 0:
      if recessive_number == 4:
        print(f"You have a 100% chance to get {recessive}")
        recessivePercent = 1
      elif mix_number == 4:
        print(f"You have a 100% chance to get {mixed}")
        mixedPercent = 1
      elif recessive_number == 2:
        print(
            f"You have a 50% chance to get {recessive} and a 50% chance to get {mixed}"
        )
        recessivePercent = 0.5
        mixedPercent = 0.5
  else:
    if dominant_number == 4:
      dominantPercent = 1
    elif dominant_number == 2:
      if recessive_number == 2:
        dominantPercent = 0.5
        recessivePercent = 0.5
      elif mix_number == 2:
        dominantPercent = 0.5
        mixedPercent = 0.5
    elif dominant_number == 1:
      if mix_number == 2:
        dominantPercent = 0.25
        recessivePercent = 0.25
        mixedPercent = 0.5
    elif dominant_number == 0:
      if recessive_number == 4:
        recessivePercent = 1
      elif mix_number == 4:
        mixedPercent = 1
      elif recessive_number == 2:
        recessivePercent = 0.5
        mixedPercent = 0.5
  

  return dominantPercent, recessivePercent, mixedPercent, dominant, recessive, mixed


#function that uses probability to generate 4 children with traits 
def kidCreator():
  playAgain = True
  gen = 0
  spacer(1, int(1/2))
  while playAgain:
    spacer()
    gen += 1
    dominantChance, recessiveChance, mixedChance, dominant, recessive, mixed = possibilityChecker(
        diHybridCross(parents, 1))
    kidChance = []
    if dominantChance == 1:
      kidChance.append("x")
      kidChance.append("x")
      kidChance.append("x")
      kidChance.append("x")
    elif dominantChance == 0.5:
      kidChance.append("x")
      kidChance.append("x")
    elif dominantChance == 0.25:
      kidChance.append("x")
    if recessiveChance == 1:
      kidChance.append("y")
      kidChance.append("y")
      kidChance.append("y")
      kidChance.append("y")
    elif recessiveChance == 0.5:
      kidChance.append("y")
      kidChance.append("y")
    elif recessiveChance == 0.25:
      kidChance.append("y")
    if mixedChance == 1:
      kidChance.append("z")
      kidChance.append("z")
      kidChance.append("z")
      kidChance.append("z")
    elif mixedChance == 0.5:
      kidChance.append("z")
      kidChance.append("z")
    elif mixedChance == 0.25:
      kidChance.append("z")

    kidPhenotype = ["", "", "", ""]
    for i in range(0, 4, 1):
      kidPhenotype[i] = random.choice(kidChance)
    #selects gender
    kidGender = [
        random.randint(1, 2),
        random.randint(1, 2),
        random.randint(1, 2),
        random.randint(1, 2)
    ]

    #function that translates x, y, z, 1, and 2 into genders and dominant/recessive/mixed 
    def chanceTranslator(item):
      if item == "x":
        return dominant
      elif item == "y":
        return recessive
      elif item == "z":
        return mixed
      elif item == 1:
        return "male"
      elif item == 2:
        return "female"

    kidChance = map(chanceTranslator, kidPhenotype)
    kidGender = map(chanceTranslator, kidGender)
    kidChance = list(kidChance)
    kidGender = list(kidGender)
    print(f"Generation {gen}")
    for i in range(0, 4, 1):
      print(f"Kid {i+1} has {kidChance[i]} and is {kidGender[i]}")
    playAgain = input(
        "\n\nDo you want to generate another set of kids? (Press any button to retry or 0 to stop): "
    )
    if playAgain == 0 or playAgain == "0":
      playAgain = False

#function that asks user whether they want to generate 4 children or not
def genKidsYN():
  spacer(1)
  genKids = input("With this information would you like to generate a set of 4 potential kids? (y/n): ").lower()
  if genKids == "y":
    spacer(1)
    print(
        "Loading Kid Generation Program, kids genes will be based of the mom and dad genes inserted above",
        end="")
    spacer()
    kidCreator()
  elif genKids == "n":
    spacer(1, int(1/4))
    print("\nOkay, no kids generated")
  else:
    print("Invalid Input")
    genKidsYN()
  spacer()
  print("\n\nThank you for visiting the program!")

#main
#title


#user trait input and trait options
try_again = True
while try_again:
  print("Children Creator")
  spacer()
  spacer(1, int(1/2))
  print("Traits List: \nEye Colour = 1\nHair Colour = 2\nHair Texture = 3")
  dominant = ""
  recessive = ""
  mixed = ""
  userTrait = verify(input("Trait: "))
  possibleEyeColor = ["brown", "blue", "green", "hazel"]
  possibleHairColor = ["black", "brown", "blonde", "ginger"]
  possibleHairTexture = ["curly", "straight", "wavy"]
  parents = trait(verify(userTrait))
  if userTrait == "1":
    parents[1], parents[0] = eyeToAllele(parents[1], parents[0])
    dominant = "brown eyes"
    mixed = "blue or green eyes"
    recessive = "hazel eyes"
  elif userTrait == "2":
    parents[1], parents[0] = hairColorToAllele(parents[1], parents[0])
    dominant = "black hair"
    mixed = "brown or ginger hair"
    recessive = "blonde hair"
  elif userTrait == "3":
    dominant = "curly hair"
    mixed = "wavy hair"
    recessive = "straight hair"
    parents[1], parents[0] = hairTextureToAllele(parents[1], parents[0])
  possibilityChecker(diHybridCross(parents, 0), 1)
  genKidsYN()
  try_again = input("Play again? (y/n): ")
  def validation(try_again):
    if try_again == "y":
      try_again = True
    elif try_again == "n":
      try_again = False
    else:
      validation(input("Invalid Input, try again: "))
    return try_again
  validation(try_again)
