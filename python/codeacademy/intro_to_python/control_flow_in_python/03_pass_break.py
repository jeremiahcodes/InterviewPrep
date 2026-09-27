# #pass
# names = ["Jude", "Amy", "Michael", "Oprah", "Kelly"]

# for name in names:
#     if 'k' in name.lower():
#         pass
#     else:
#         print(name)



# #break
# names = ["Jake", "Amy", "Bruce", "Mary", "Clark"]

# for name in names:
#     if 'm' in name.lower():
#         break #exit the loop when a name containing the letter 'm' is found
#     else:
#         print(name)

#continue
names = ["Jake", "Amy", "Bruce", "Mary", "Clark"]

for name in names:
    if 'm' in name.lower():
        print("Skipped " + name)
        continue #skip the current iteration when a name containing the letter 'm' is found
    else:
        print(name)
