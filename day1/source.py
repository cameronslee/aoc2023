# Day 1: Trebuchet?!

with open('input.txt') as f:
  lines = f.readlines()

total = 0
for l in lines:
  i = 0
  j = len(l)-1

  while not l[i].isdigit():
    i += 1

  while not l[j].isdigit():
    j -= 1

  total += (int)(l[i] + l[j])

print("Part 1", total)

total = 0
nums = {
  "one" : "1",
  "two" : "2",
  "three" : "3",
  "four" : "4",
  "five" : "5",
  "six" : "6",
  "seven" : "7",
  "eight" : "8",
  "nine" : "9"
}

for l in lines:
  print(l)
  i = 0
  j = len(l)-2

  while not l[i].isdigit() and l[i:i+3] not in nums and l[i:i+4] not in nums and l[i:i+5] not in nums:
    i += 1

  while not l[j].isdigit() and l[j-2:j+1] not in nums and l[j-3:j+1] not in nums and l[j-4:j+1] not in nums:
    j -= 1
  
  left = 0
  if l[i].isdigit():
    left = l[i]
  elif l[i:i+3] in nums:
    left = nums[l[i:i+3]]
  elif l[i:i+4] in nums:
    left = nums[l[i:i+4]]
  elif l[i:i+5] in nums:
    left = nums[l[i:i+5]]

  right = 0
  if l[j].isdigit():
    right = l[j]
  elif l[j-2:j+1] in nums:
    right = nums[l[j-2:j+1]]
  elif l[j-3:j+1] in nums:
    right = nums[l[j-3:j+1]]
  elif l[j-4:j+1] in nums:
    right = nums[l[j-4:j+1]]

  total += (int)(left + right)

print("Part 2", total)
