#! /usr/bin/env python
# -*- coding=utf-8 -*-
  
import re
  
text = 'pythontab'
m = re.match(r"\w+", text)
if m: 
    print(m.group(0))
else:
    print('not match')


#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
  
import re
  
text = '@pythontab'
m = re.match(r"\w+", text)
if m: 
    print(m.group(0))
else:
    print('not match')

#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
  
import re
  
text = 'pythontab'
m = re.search(r"\w+", text)
if m: 
    print(m.group(0))
else:
    print('not match')

text = '@pythontab'
m = re.search(r"\w+", text)
if m: 
    print(m.group(0))
else:
    print('not match')
