# Open the file in read mode
s = open('/Users/admin/Documents/new/praticework/demo.txt', mode='a')

# write content
content = s.write('this is first file')

# Close the file
s.close()
# Open the file in read mode
s = open('/Users/admin/Documents/new/praticework/demo.txt', mode='r')

# write content
content = s.read()

# Print to terminal
print(content)

# Close the file
s.close()
s = open('/Users/admin/Documents/new/praticework/demo.txt', mode='w')

# write content
content = s.write('this is a book')

# Close the file
s.close()

s = open('/Users/admin/Documents/new/praticework/demo.txt', mode='r+')
print(s.read)
# write content
content = s.write('r+ mode')

# Close the file
s.close()

s = open('/Users/admin/Documents/new/praticework/demo.txt', mode='w+')
# write content
content = s.write('w+ mode')
print(s.read())

# Close the file
s.close()