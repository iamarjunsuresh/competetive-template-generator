import os
line=raw_input('enter template:')

for word in line.split(' '):
    print prevtoken
    if word=="{":
		output+=forloop % (prevtoken[-3],prevtoken[-2],prevtoken[-3],prevtoken[-1],prevtoken[-3])
		prevtoken.clear()
    elif word=="}":
        output+="""
        }
        """
	elif word=="in":
		for token in prevtoken:
			output+="cin>>" + token+";"
		prevtoken.clear()
    elif word=="":
        pass
    else:
        prevtoken.append(word)
output+="""

return 0;
}
"""

print output











