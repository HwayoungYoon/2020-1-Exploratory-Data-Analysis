Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Join
>>> string2 = "Your,deliverable,is,due,in,June"
>>> string2_list = string2.split(',')
>>> print("Output #25: {0}".format(','.join(string2_list)))
Output #25: Your,deliverable,is,due,in,June
>>> #Replace
>>> string5 = "Let's replace the spaces in this sentence with other characters."
>>> string5_replace = string5.replace(" ","!@!")
>>> print("Output #32 (with !@!): {0:s}".format(string5_replace))
Output #32 (with !@!): Let's!@!replace!@!the!@!spaces!@!in!@!this!@!sentence!@!with!@!other!@!characters.
>>> string5_replace = string5.replace(" ",",")
>>> print("Output #33 (with commas): {0:s}".format(string5_replace))
Output #33 (with commas): Let's,replace,the,spaces,in,this,sentence,with,other,characters.
>>> #Lower
>>> string6 = "Here's WHAT Happens WHEN You Use lower."
>>> print("Output #34: {0:s}".format(string6.lower()))
Output #34: here's what happens when you use lower.
>>> #Upper
>>> string7 = "Here's what Happens when You Use UPPER."
>>> print("Output #35: {0:s}".format(string7.upper()))
Output #35: HERE'S WHAT HAPPENS WHEN YOU USE UPPER.
>>> #Capitalize
>>> string8 = "here's WHAT Happens WHEN you use Capitalize."
>>> print("Output #36: {0:s}".format(string8.capitalize()))
Output #36: Here's what happens when you use capitalize.
>>> string8_list = string8.split()
>>> print("Output #37 (on each word):")
Output #37 (on each word):
>>> for word in string8_list:
	print("{0:s}".format(word.capitalize()))

	
Here's
What
Happens
When
You
Use
Capitalize.
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print("Mac address: {0}".format(mac))
Mac address: 150075731951663
>>> 