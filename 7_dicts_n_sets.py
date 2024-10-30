# Dictionaries
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items
print(band['vocals'])
print(band.get('guitar'))

# List all keys
print(band.keys())

# Print all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# Verify a key exists
print('guitar' in band)
print('triangle' in band)

# Change values / add key/value
band['vocals'] = 'Coverdale'
band.update({'guitar': 'Ross', 'bass': 'JPJ'})

print(band)

# Remove items
# Removes specific item, returns the value of the item removed
print(band.pop('bass'))
print(band)

band['drums'] = 'Bonham'
print(band)

print(band.popitem())   # Removes last item added, returns a key/value tuple
print(band)

# Delete and clear
del band['guitar']  # Removes specific item

band2.clear()   # Removes all items

print(band)
print(band2)

del band2   # Deletes the dictionary from the app

# Copy dictionaries
band1 = band    # WARNING: This creates a reference; All changes to 'band1' will affect 'band' too!

band2 = band.copy()  # This creates an actual copy

band3 = dict(band)

# Nested dictionaries
member1 = {'name': 'Plant', 'instrument': 'vocals'}
member2 = {'name': 'Page', 'instrument': 'guitar'}

band = {
    'member1': member1,
    'member2': member2
}

print(band)

# Acessing nested dictionaries
print(band['member1']['name'])

# Sets
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

nums = {1, 2, 3, 4}

nums2 = set((3, 4, 5, 6))

print(nums)
print(nums2)

print(type(nums))
print(len(nums))

# No duplicates allowed
nums3 = {6, 7, 7, 8, 9}
print(nums3)  # {6, 7, 8, 9}

# True is a dupe of 1, False is a dupe of 0
nums4 = {True, 0, 1, 2, 3, False}
print(nums4)  # {0, True, 2, 3} it uses the first item read

# Check if value is in a set
print(2 in nums4)  # True

# You cannot refer to an element in a set with an index or a key

# Add elements to a set
nums.add(5)
print(nums)

# Add elements from one set to another
nums.update(nums2)
print(nums)  # {1, 2, 3, 4, 5, 6}

# You can use .update with lists, tuples and dictionaries too

# Merge two sets to create one set
mergednums = nums.union(nums3)
print(mergednums)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)  # {2, 3}

# Keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)  # {1, 4}
