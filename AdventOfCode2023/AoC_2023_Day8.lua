--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = 0
local instructions = {}


for line in io.lines("my_own/input.txt") do 
  lines[#lines + 1]= line
end

local commands = lines[1]
local curr = {}

for i=3,#lines do
  instructions[string.sub(lines[i], 1, 3)] = { string.sub(lines[i], 8, 10), string.sub(lines[i], 13, 15) }
  if string.sub(lines[i], 3, 3) == "A" then curr[#curr+1] = string.sub(lines[i], 1, 3) end
end

local minReach = {}

for p=1,#curr do
  result = 0
  while string.sub(curr[p], 3, 3) ~= "Z" do 
    for i=1,string.len(commands) do
      if string.sub(commands,i,i) == "L" then curr[p] = instructions[curr[p]][1] else curr[p] = instructions[curr[p]][2] end
      result = result + 1
    end
  end
  minReach[#minReach+1] = result/string.len(commands)
end
result = 1
--All were prime number so I don't have to do lowest common multiple
for i=1,#minReach do result = result * minReach[i] end
print(result*string.len(commands))
