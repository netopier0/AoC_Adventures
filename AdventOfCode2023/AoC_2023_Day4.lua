--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = 0

local cardsWins = {}

for line in io.lines("my_own/input.txt") do 
  --lines[#lines + 1] = line
  local x = string.find(line, ":")
  local y = string.find(line, "|")
  local wins = {}
  local tmpRes = 0
  for i in string.gmatch(string.sub(line, x, y), "%d+") do
    wins[i] = true
  end
  
  for i in string.gmatch(string.sub(line, y), "%d+") do
    if wins[i] then
      tmpRes = tmpRes + 1
      --if tmpRes == 0 then tmpRes = 1 else tmpRes = tmpRes * 2 end
    end
  end
  cardsWins[tonumber((string.match(string.sub(line, 0, x), "%d+")))] = tmpRes
  --result = result + tmpRes
end

local function evaluateCards(cardNum)
  local res = 0
  for i=1,cardsWins[cardNum] do
    res = res + evaluateCards(cardNum+i)
  end
  return res+1
end

for i=1,#cardsWins do
  result = result + evaluateCards(i)
end
print(result)

