--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = 0
local startRow
local startColumn
local mapa = {}
--[[
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
--]]

local function getNext(fromRow, fromColumn, currRow, currColumn)
  local currVal = string.sub(lines[currRow], currColumn, currColumn)
  if currVal == "|" then if fromRow == currRow-1 then return currRow+1, currColumn else return currRow-1, currColumn end
  elseif currVal == "-" then if fromColumn == currColumn-1 then return currRow, currColumn+1 else return currRow, currColumn-1 end
  elseif currVal == "L" then if currRow == fromRow then return currRow-1, currColumn else return currRow, currColumn+1 end
  elseif currVal == "J" then if currRow == fromRow then return currRow-1, currColumn else return currRow, currColumn-1 end
  elseif currVal == "7" then if currRow == fromRow then return currRow+1, currColumn else return currRow, currColumn-1 end
  elseif currVal == "F" then if currRow == fromRow then return currRow+1, currColumn else return currRow, currColumn+1 end
  else print("Ehm")
  end
end

for line in io.lines("my_own/input.txt") do 
  lines[#lines + 1]= line
  if string.find(line, "S") then startRow = #lines startColumn = string.find(line, "S") end
end

local dirRow1, dirColumn1 = startRow+1, startColumn
local dirRow2, dirColumn2 = startRow-1, startColumn

local pastDirRow1, pastDirColumn1 = startRow, startColumn
local pastDirRow2, pastDirColumn2 = startRow, startColumn

--Part 1
while true do
  result = result + 1
  mapa[dirRow1 + 1000*dirColumn1] = true
  mapa[dirRow2 + 1000*dirColumn2] = true
  if dirRow1 == dirRow2 and dirColumn1 == dirColumn2 then break end
  local dR1, dC1 = dirRow1, dirColumn1
  local dR2, dC2 = dirRow2, dirColumn2
  dirRow1, dirColumn1 = getNext(pastDirRow1, pastDirColumn1, dirRow1, dirColumn1)
  dirRow2, dirColumn2 = getNext(pastDirRow2, pastDirColumn2, dirRow2, dirColumn2)
  pastDirRow1, pastDirColumn1 = dR1, dC1
  pastDirRow2, pastDirColumn2 = dR2, dC2
end
print(result)
mapa[startRow + 1000*startColumn] = true
lines[startRow] = string.gsub(lines[startRow], "S", "|")


--Point in polygon algorithm Hint from reddit
--Part 2
result = 0
for i=1,#lines do
  local passed = 0
  for j=1,string.len(lines[i]) do
    if mapa[i + 1000*j] then 
      local val = string.sub(lines[i], j, j) 
      if val == "|" then passed = passed + 1
      elseif val == "J" or val == "F" then passed = passed + 0.5 
      elseif val == "L" or val == "7" then passed = passed - 0.5 
      end
    else
      --mapa[i + 1000*j] = passed%2
      if passed%2 == 1 then result = result + 1 end
    end
  end
end
print(result)

--[[
--Print
for i=1,#lines do
  local pr = ""
  for j=1,string.len(lines[i]) do
    if mapa[i + 1000*j] == 1 then pr = pr .. "Y"
    elseif mapa[i + 1000*j] == 0 then pr = pr .. "N"
    else pr = pr .. string.sub(lines[i], j, j) 
    end
  end
  print(pr)
end
--]]