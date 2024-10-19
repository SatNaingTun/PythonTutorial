x="live and  let \t \tlive"
y=x.split();
print(y)
print(x)
y=x.replace(" let \t \tlive","enjoy life")
print(y)

import re #regular expression
regexpr=re.compile(r"[\t]+")
print(regexpr.sub("",x))
