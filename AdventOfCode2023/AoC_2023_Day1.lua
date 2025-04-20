--file = io.open("my_own/input.txt", "r")
--local lines = {}

local result = 0
local numbers = {"one","two","three","four","five","six","seven","eight","nine"}

local function findNum(line, rev)
  if rev then line = string.reverse(line) end
  local n = #line + 1
  local res
  for i=1, #numbers do
    local pos
    if rev then
      pos = string.find(line, string.reverse(numbers[i]))
    else
      pos = string.find(line, numbers[i])
    end
    if pos ~= nil and n > pos then n = pos res = i end
  end
  if n > string.find(line, "[1-9]") then res = string.match(line, "[1-9]") end
  return res
end


for line in io.lines("my_own/input.txt") do 
  --lines[#lines + 1] = line
  local a = findNum(line, false)
  local b = findNum(line, true)
  result = result + (a .. b)
end

print(result)
