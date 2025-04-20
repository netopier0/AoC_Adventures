--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = 0

local time = {}
local dist = {}

local t
local d

for line in io.lines("my_own/input.txt") do 
  lines[#lines + 1], _ = string.gsub(line, " ", "")
end
--[[
--Part 1
result = 1
for i in string.gmatch(lines[1], "%d+") do
  time[#time+1] = tonumber(i)
end

for i in string.gmatch(lines[2], "%d+") do
  dist[#dist+1] = tonumber(i)
end

for race=1,#time do
  local count = 0
  for speed=1,time[race] do
    if speed * (time[race]-speed) > dist[race] then count = count + 1 end
  end
  result = result * count
end
--]]
--Part 2
t = tonumber(string.match(lines[1], "%d+"))
d = tonumber(string.match(lines[2], "%d+"))
local b = 0
local e = t 
local s = math.floor(t/2)
--Min win time
while not (s * (t-s)< d and (s+1)*(t-s-1)> d) do
  if s * (t-s)>= d then e = s else b = s end
  s = math.floor((b+e)/2)
end
local minWin = s + 1
b = 0
e = t 
s = math.floor(t/2)
--Max win time
while not (s * (t-s)> d and (s+1)*(t-s-1)< d) do
  if s * (t-s)<= d then e = s else b = s end
  s = math.floor((b+e)/2)
end
local maxWin = s
print(maxWin - minWin + 1)
--print(result)