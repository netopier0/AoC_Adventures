--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = 0
local galaxyColumn = {}
local expansionColumns = {}
local expansionRows = {}
local galaxies = {}

local function calcDistance(gal1, gal2)
  local expander = 0
  for i=1,#expansionRows do
    if (gal1[1] > expansionRows[i] and expansionRows[i] > gal2[1]) or (gal1[1] < expansionRows[i] and expansionRows[i] < gal2[1])
    then expander = expander + 1
    end
  end
  for i=1,#expansionColumns do
    if (gal1[2] > expansionColumns[i] and expansionColumns[i] > gal2[2]) or (gal1[2] < expansionColumns[i] and expansionColumns[i] < gal2[2])
    then expander = expander + 1
    end
  end
  return math.abs(gal1[1] - gal2[1]) + math.abs(gal1[2] - gal2[2]) + expander * 999999 --Part1 expander * 1
end

for line in io.lines("my_own/input.txt") do 
  lines[#lines+1] = line
  if not string.find(line, "#") then expansionRows[#expansionRows+1] = #lines
  else local initial = 0 while string.find(line, "#", initial+1) do initial = string.find(line, "#", initial+1) galaxyColumn[initial] = true end
  end
end

for i=1,string.len(lines[1]) do
  if not galaxyColumn[i] then
    expansionColumns[#expansionColumns+1] = i
  end
end

for i=1,#lines do
  local initial = 0
  while string.find(lines[i], "#", initial+1) do initial = string.find(lines[i], "#", initial+1) galaxies[#galaxies+1] = {i, initial} end
end

for i=1,#galaxies do 
  for j=i+1, #galaxies do
    result = result + calcDistance(galaxies[i], galaxies[j])
  end
end
print(result)