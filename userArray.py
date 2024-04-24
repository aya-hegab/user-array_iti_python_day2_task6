def userInputs():
  lengthUse = input("enter length of array ")
  while not lengthUse.isdigit():
    lengthUse = input("enter length of array ")
  arrLength = lengthUse

  startUse = input("enter start of array ")
  while not startUse.isdigit():
    startUse = input("enter start of array ")
  arrStart = startUse
  return arrLength, arrStart

def createUserArray(arrLength, arrStart):
  userArray = []
  for i in range(int(arrLength)):
    userArray.append(int(arrStart) + i)
  return userArray

arrLength, arrStart = userInputs()
print(createUserArray(arrLength, arrStart))