def SuffixArray(text):
  suffixArray = []
  for i in range(0, len(text)):
    suffixArray.append(text[i:])
  suffixArray=sorted(suffixArray)
  return suffixArray

def BinarySearch(suffixarray, pattern):
  start = 0
  end = len(suffixarray) - 1
  while start <= end:
    middle = (start + end)//2
    middlepoint = suffixarray[middle]
    if middlepoint > pattern:
      end = middle - 1
    elif middlepoint < pattern:
      start = middle + 1
    else:
      #return middlepoint
      return suffixarray.index(middlepoint)


texto = SuffixArray("Biologia$")
print(BinarySearch(texto, "$"))