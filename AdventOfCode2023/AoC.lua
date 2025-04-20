--file = io.open("my_own/input.txt", "r")
--local lines = {}
local result = 0
--Part 1
--[[
local function checkControl(line, control)
  line = table.concat(line)
  local curr = 1
  for i in string.gmatch(line, "#+") do
    if control[curr] ~= string.len(i) then return false else curr = curr + 1 end
  end
  return true
end

local function getCombinations(pos, spring, usable, changable, control)
  if changable < usable then return end
  if usable == 0 or #spring+1 == pos then if checkControl(spring, control) then result = result + 1 end return end
  if spring[pos] == "?" then
    spring[pos] = "#"
    getCombinations(pos+1, spring, usable-1, changable-1, control)
    spring[pos] = "?"
    getCombinations(pos+1, spring, usable, changable-1, control)
  else getCombinations(pos+1, spring, usable, changable, control)
  end
end

local function loadToTable(line)
  local res = {}
  local countH = 0
  local countQ = 0
  for i=1,string.len(line) do
    res[#res+1] = string.sub(line, i, i)
    if res[#res] == "#" then countH = countH + 1 end
    if res[#res] == "?" then countQ = countQ + 1 end
  end
  return res, countH, countQ
end

local function loadNumbers(line)
  local res = {}
  local total = 0
  for i in string.gmatch(line, "%d+") do
    res[#res+1] = tonumber(i)
    total = total + res[#res]
  end
  return res, total
end
--]]

--Part 2
--Masive help form reddit

local vypis = {}

local function solve(springs, posS, numbers, posN, left, total)
  if #numbers+1 == posN then result = result + 1 return end
  if #springs+1 == posS then return end
  if left > total then return end
  
  local lenN = numbers[posN]
  local lenS = string.len(springs[posS])
  
  if lenS == lenN then
    vypis[posN] = springs[posS]
    solve(springs, posS+1, numbers, posN+1, left-lenN, total-lenS)
  elseif lenS > lenN then
    for i=0,lenS-lenN do
      if not string.find(string.sub(springs[posS], 1, i), "#") and (lenN+i+1 > lenS or string.sub(springs[posS], i+lenN+1, i+lenN+1) ~= "#") then
        local tmp = springs[posS]
        vypis[posN] = string.sub(springs[posS], i, i+lenN)
        springs[posS] = string.sub(springs[posS], i+1+lenN+1)
        solve(springs, posS, numbers, posN+1, left-lenN, total-(lenN+i))
        springs[posS] = tmp
      elseif string.find(string.sub(springs[posS], 1, i), "#") then break
      end
    end
  end
  solve(springs, posS+1, numbers, posN, left, total-lenS)
end


local function loadNumbers2(line)
  local res = {}
  local left = 0
  for i in string.gmatch(line, "%d+") do
    res[#res+1] = tonumber(i)
    left = left + tonumber(i)
  end
  return res, left
end

local function loadSpring(line)
  local res = {}
  local total = 0
  for i in string.gmatch(line, "[#?]+") do
    res[#res+1] = i
    total = total + string.len(i)
  end
  return res, total
end

local function suma(line,st)
  local left = 0
  for x=st,#line do
    left = left + tonumber(line[x])
  end
  
  return left
end

-- Rewritten from python
local function recurse(lava, springs, springPos)
  local res = 0
  if #springs-springPos+1 == 0 then if not string.find(lava, "#") then return 1 end end
  local curr = springs[springPos]
  for i=1, string.len(lava) - suma(springs, springPos+1) - (#springs-springPos) - curr + 1 do
    if string.find(string.sub(lava, 1, i-1), "#") then break end
    local nx = i + curr - 1
    if nx <= string.len(lava) and not string.find(string.sub(lava, i, nx), '%.') and not string.find(string.sub(lava, nx+1, nx+1), '#') then
      res = res + recurse(string.sub(lava, nx+2), springs, springPos+1)
    end
  end
  return res
end


for line in io.lines("my_own/input.txt") do 
  --lines[#lines+1] = line
  local x, _ = string.find(line, " ")
  --Part 1
  --[[
  local springs, used, available = loadToTable(string.sub(line, 1, x-1))
  local numbers, total = loadNumbers(string.sub(line, x+1))
  getCombinations(0, springs, total-used, available, numbers)
  --]]
  
  --Part 2
  print(line)
  local springIslands, total = loadSpring(string.sub(string.rep(string.sub(line, 1, x-1) .. "?", 5), 1, -2))
  local numbers, left = loadNumbers2(string.rep(string.sub(line, x+1) .. ",", 5))
  --for x=1,#numbers do print(numbers[i]) end
  local h = recurse(string.sub(string.rep(string.sub(line, 1, x-1) .. "?", 5), 1, -2), numbers, 1)
  result = result + h
  --[[
  local numbers, left = loadNumbers2(string.rep(string.sub(line, x+1) .. ",", 5))

  solve(springIslands, 1, numbers, 1, left, total)
  print(line, "SubResult: "..result)
  --]]
end

print("Result: " .. result)