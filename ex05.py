#ex05.py

my_name = "Zed A. Shaw"
my_age = 35 #Not a lie
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usualy %s depending on the coffee" % my_teeth

#This line is tricky, try to get it exactluy right

print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight
	)


# OJO FALTAN LOS Study Drills

#Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
#Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
#Search online for all of the Python format characters.
#Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
