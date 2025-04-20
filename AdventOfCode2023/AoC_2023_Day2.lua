--file = io.open("my_own/input.txt", "r")
--local lines = {}

local result = 0
local red = 12 
local green = 13 
local blue = 14

local function checkDraw(line)
  --local good = true
  for l in string.gmatch(line, ".-,") do
    if string.find(l, "red") then
      --good = good and tonumber(string.match(l, "%d+")) <= red
      red = math.max(red, tonumber(string.match(l, "%d+")))
    elseif string.find(l, "green") then
      --good = good and tonumber(string.match(l, "%d+")) <= green
      green = math.max(green, tonumber(string.match(l, "%d+")))
    elseif string.find(l, "blue") then
      --good = good and tonumber(string.match(l, "%d+")) <= blue
      blue = math.max(blue, tonumber(string.match(l, "%d+")))
    end
  end
  --return good
end

for line in io.lines("my_own/input.txt") do 
  --lines[#lines + 1] = line
  red = 0
  green = 0
  blue = 0
  
  local gameId = string.sub(string.match(line, "Game.*:"), 6, -2)
  local _, pos = string.find(line, ":")
  local myLine = string.sub(line, pos + 2) .. ";"
  --local good = true
  for i in string.gmatch(myLine, ".-;") do
    i, _ = string.gsub(i, ";", ",")
    --good = good and checkDraw(i)
    checkDraw(i)
    
  end
  --if good then result = result + gameId end
  result = result + red * green * blue
end

print(result)

