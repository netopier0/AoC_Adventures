--file = io.open("my_own/input.txt", "r")
--local lines = {}
local result = 0
local cards = {}

local function evalHelp(currHand, counterHand)
  local jS = counterHand["J"]
  if not jS then
    if #currHand == 5 then return 1
    elseif #currHand == 4 then return 2
    elseif #currHand == 3 then for i=1,3 do if counterHand[currHand[i]] == 3 then return 4 end end return 3
    elseif #currHand == 2 then for i=1,2 do if counterHand[currHand[i]] == 4 then return 6 end end return 5
    else return 7
    end
  end
  --Part 2
  if #currHand == 5 then return 2
  elseif #currHand == 4 then return 4
  elseif #currHand == 3 then if jS == 3 or jS == 2 then return 6 else for i=1,3 do if counterHand[currHand[i]] == 3 then return 6 end end return 5 end
  else return 7
  end
end

local function evaluate(hand)
  local currHand = {}
  local counterHand = {}
  for c in string.gmatch(hand, ".") do
    if not counterHand[c] then counterHand[c] = 1 currHand[#currHand+1] = c else counterHand[c] = counterHand[c]+1 end
  end
  
  return evalHelp(currHand, counterHand)
end

local function getVal(c)
  if c == "T" then return 10 end
  -- Part 1
  -- if c == "J" then return 11 end
  -- Part 2
  if c == "J" then return 1 end
  if c == "Q" then return 12 end
  if c == "K" then return 13 end
  if c == "A" then return 14 end
  return tonumber(c)
end

local function compareHand(h1, h2)
  for i=1,5 do
    local c1 = string.sub(h1,i,i)
    local c2 = string.sub(h2,i,i)
    if c1 ~= c2 then
      local v1 = getVal(c1)
      local v2 = getVal(c2)
      return v1 > v2
    end
  end
end

local function tableSort(tab)
  for i=1,#tab do
    for j=1,#tab-i do
      if compareHand(tab[j][1], tab[j+1][1]) then tab[j], tab[j+1] = tab[j+1], tab[j] end
    end
  end
end


for line in io.lines("my_own/input.txt") do 
  --lines[#lines + 1]= line
  local value = evaluate(string.sub(line, 1, 5))
  if not cards[value] then cards[value] = {} end
  cards[value][#cards[value]+1] = { string.sub(line, 1, 5), tonumber(string.sub(line, 7)) }
end

local rank = 1
for i=1,7 do if cards[i] then tableSort(cards[i]) end end

for i=1,7 do
  if cards[i] then
    for j=1,#cards[i] do
      result = result + cards[i][j][2] * rank
      rank  = rank + 1
    end
  end
end

print(result)
