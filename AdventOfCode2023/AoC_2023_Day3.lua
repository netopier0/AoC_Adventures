--file = io.open("my_own/input.txt", "r")
local lines = {}
result = 0

--[[
--Part 1
local function checkAround(number, line, start, finish)
  local isAround = false
  if line > 1 then
    isAround = isAround or string.find(string.sub(lines[line-1], start-1, finish+1), "[*#+=%%-&$/@]")
  end
  if start > 1 then
    isAround = isAround or string.find(string.sub(lines[line], start-1, start-1), "[*#+=%%-&$/@]")
  end
  if finish < #lines[line] then
    isAround = isAround or string.find(string.sub(lines[line], finish+1, finish+1), "[*#+=%%-&$/@]")
  end
  if line < #lines then
    isAround = isAround or string.find(string.sub(lines[line+1], start-1, finish+1), "[*#+=%%-&$/@]")
  end
  return isAround
end
--]]

local function checkAroundStar(number, line, start, finish)
  local posx, posy
  if line > 1 then
    if string.find(string.sub(lines[line-1], start-1, finish+1), "[*]") then
      posx = start-2 + string.find(string.sub(lines[line-1], start-1, finish+1), "[*]")
      posy = line-1
    end
  end
  if start > 1 then
    if string.find(string.sub(lines[line], start-1, start-1), "[*]") then
      posx = start-2 + string.find(string.sub(lines[line], start-1, start-1), "[*]")
      posy = line
    end
  end
  if finish < #lines[line] then
    if string.find(string.sub(lines[line], finish+1, finish+1), "[*]") then
      posx =  finish + string.find(string.sub(lines[line], finish+1, finish+1), "[*]")
      posy = line
    end
  end
  if line < #lines then
    if string.find(string.sub(lines[line+1], start-1, finish+1), "[*]") then
      posx = start-2 + string.find(string.sub(lines[line+1], start-1, finish+1), "[*]")
      if start == 1 then posx = posx + 1 end
      posy = line+1
    end
  end
  return posx, posy
end

for line in io.lines("my_own/input.txt") do 
  lines[#lines + 1] = line
end

--[[
--Part 1
for i=1,#lines do
  print(lines[i])
  local first = 0
  local last = 0
  while true do
    first, last = string.find(lines[i], "%d+", last+1)
    if not last then break end
    if checkAround(tonumber(string.sub(lines[i],first, last)), i, first, last) then
      result = result + tonumber(string.sub(lines[i],first, last))
    end
  end
end
--]]

cogs = {}
cogs_num = {}
nums = {}

for i=1,#lines do
  local first = 0
  local last = 0
  while true do
    local posx, posy
    first, last = string.find(lines[i], "%d+", last+1)
    if not last then break end
    posx, posy = checkAroundStar(tonumber(string.sub(lines[i],first, last)), i, first, last)
    if posx then
      if not cogs_num[1000*posy + posx] then
        nums[#nums+1] = 1000*posy + posx
        cogs_num[1000*posy + posx] = 1
        cogs[1000*posy + posx] = tonumber(string.sub(lines[i],first, last))
      else
        cogs_num[1000*posy + posx] = cogs_num[1000*posy + posx] + 1
        cogs[1000*posy + posx] = cogs[1000*posy + posx] * tonumber(string.sub(lines[i],first, last))
      end
    end
  end
end

for _, v in ipairs(nums) do
  print(v)
  if cogs_num[v] == 2 then
    result  = result + cogs[v]
  end
end
print(result)

