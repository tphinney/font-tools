# FontLab script to generate OpenType feature substitution code for selected glyphs
# works with simple ligatures and alternates.
# Does not attempt to decode multiple-feature glyphs such as "f_f_i.alt"
# as there is no single clear right input set for that
#
# by Thomas Phinney, open source under Apache 2.0 license

f = fl.font
if f == None:
  exit

# function to call for each glyph...
# it takes two arguments
def printCode(g):
  if g == None:
    return
# take the part of the glyph name before the period:
  dropDot = g.name.split(".")[0]
# separate ligature components:
  ligSplit = dropDot.replace("_"," ")
# if neither of these substitutions did anything, exit function and don't print the replacement code
  if ligSplit == g.name :
  	return
# hey, let's print the glyph replacement code now!
  print "  sub", ligSplit, "by", g.name , ";"

# This is the actual program (using the function above)
font = fl.font
glyphs = font.glyphs
# for every glyph in the font
for index in range(len(glyphs)):
  if fl.Selected(index):
    printCode(glyphs[index])
