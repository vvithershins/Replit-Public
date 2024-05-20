#A combination of split and rsplit
def super_split(text,sep,max):
  if max < 0:
    if abs(max) > text.count(sep):
      max = -text.count(sep)
    reversedword = reversed(text)
    reversedword = "".join(reversedword)
    new = reversedword.split(sep,abs(max))
    new = " ".join(new)#uses non breaking space alt numpad 254
    forward = reversed(new)
    how = "".join(forward)
    final = how.split(" ")#uses non breaking space alt numpad 254
    
  elif max > 0:
    if max > text.count(sep):
      max = text.count(sep)
    final = text.split(sep,max)
    
  else:
    final = "There was an error, Cannot split 0 times"
  return final

  

#Example
text = "abc.def.ghi.jkl.mno"

print(super_split(text,".",-2))
