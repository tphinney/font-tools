# TWP: Generate OpenType feature substitution code for selected glyphs
# works with simple ligatures and alternates.
# Does not attempt to decode multiple-feature glyphs such as "f_f_i.alt"
# as there is no single clear right input set for that

f = fl.font
if f == None:
  exit

def printCode(g, index):
  if g == None:
    return
  dropDot = glyphs[index].name.split(".")[0]
  inputNames = dropDot.replace("_"," ")
  if len(glyphs[index].name.split(".")) == 1:
  	return
  print "  sub", inputNames, "by", glyphs[index].name , ";"

font = fl.font
glyphs = font.glyphs
for index in range(len(glyphs)):
  if fl.Selected(index):
    printCode(glyphs[index], index)
