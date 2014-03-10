# This FontLab Studio 5 script takes a set of designed denominator glyphs with names ending 
# in ".dnom" and creates new shifted glyphs referencing the originals as
# composites, with names ending ".numr", ".subs" and ".sups"

# NOTES:
# 1) Requires RoboFab to be installed.
# 2) Script uses constants for vertical offsets of numerator, denominator 
#    and subscript glyphs; you will have to adjust these for your values.
# 3) Script will use the italic angle in the font to decide on the horizontal 
#    shift required for any given vertical shift.

import math
# we need the Python math module to calculate the correct 
# horizontal shifts for vertically-moved components in italic fonts.

from robofab.world import CurrentFont
#import string

f = CurrentFont()
fontAngle=fl.font.italic_angle
startCount = len(fl.font.glyphs)

def splitName():
	glyph.name.split('.')

class Mode: # make a class for categories of glyphs being added, with different suffixes and shifts
	def __init__(self, glyphkind, y, x): # when initializing, get kind label and contents
		self.kind = glyphkind
		self.yShift = y
		self.xShift = x

modes=[0,1,2]
modes[0]=Mode("numr",280,math.cos(fl.font.italic_angle) * 280 * -1)
modes[1]=Mode("sups",400,math.cos(fl.font.italic_angle) * 400 * -1)
modes[2]=Mode("subs",-140,math.cos(fl.font.italic_angle) * -140 * -1)

dnomGlyphs = []
	
for glyph in fl.font.glyphs:
	splitName = glyph.name.split('.')
	if len(splitName)>1 and splitName[1]=="dnom":
			dnomGlyphs.append(glyph)

print "\nWelcome to FontLab Studio 5.\n"
print "Fonts  open: ", len(fl)

for x in range (0, len(modes)):
	print "Adding", modes[x].kind, "glyphs"
	for sGlyph in dnomGlyphs:
		newGlyph = Glyph() ;
		comp = Component(sGlyph.index) ;
		newGlyphName = sGlyph.name.split('.')[0]+"."+modes[x].kind ;
		newGlyph.width = sGlyph.width ;
		f.newGlyph(newGlyphName) ;
		f[newGlyphName].width = sGlyph.width ;
		f[newGlyphName].appendComponent(sGlyph.name, (modes[x].xShift,modes[x].yShift)) ;
		f.update() ;

endCount = len(f.glyphs)

print "Starting glyph count was ", startCount
print "Final glyph count is ", endCount
print "Added ", (endCount - startCount), "glyphs"
