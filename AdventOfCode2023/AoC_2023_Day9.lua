--file = io.open("my_own/input.txt", "r")
--local lines = {}
local result = 0

local function extrapolate(values)
  local subs = {}
  local zeroes = true
  for i=2,#values do
    subs[#subs+1] = values[i] - values[i-1]
    zeroes = zeroes and subs[#subs] == 0
  end
  if not zeroes then
    subs = extrapolate(subs)
  else 
    subs[0] = 0
  end
  --Part 1
  --values[#values+1] = values[#values] + subs[#subs]
  values[0] = values[1] - subs[0]
  return values
end

for line in io.lines("my_own/input.txt") do 
  -- lines[#lines + 1]= line
  local readings = {}
  for i in string.gmatch(line, "-?%d+") do
    readings[#readings+1] = tonumber(i)
  end
  readings = extrapolate(readings)
  --Part 1
  --result = result + readings[#readings]
  result = result + readings[0]
end

print(result)
