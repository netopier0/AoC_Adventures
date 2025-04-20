--file = io.open("my_own/input.txt", "r")
local lines = {}
local result = {}

local seeds = {}
local seedToSoil = {}
local soilToFertilizer = {}
local fertilizerToWater = {}
local waterToLight = {}
local lightToTemperature = {}
local temperatureToHumidity = {}
local humidityToLocation = {}

local function loadLine(line)
  local res = {}
  for i in string.gmatch(line, "%d+") do
    if not res["to"] then
      res["to"] = tonumber(i)
    elseif not res["from"] then
      res["from"] = tonumber(i)
    else
      res["range"] = tonumber(i)
    end
  end
  return res
end

--Part 1
local function findResectable(value, con)
  for i=1,#con do
    if value >= con[i]["from"] and value < con[i]["from"] + con[i]["range"] then
      return value - con[i]["from"] + con[i]["to"]
    end
  end
  return value
end

local function findResectableInter(inp, con)
  local start, finish = inp[1], inp[2]
  local res = {}
  for i=1,#con do
    if con[i]["from"] < start and con[i]["from"] + con[i]["range"] < start then
    elseif con[i]["from"] <= start and con[i]["from"] + con[i]["range"] >= start and con[i]["from"] + con[i]["range"] <= finish then
      res[#res+1] = { start - con[i]["from"] + con[i]["to"], con[i]["to"] + con[i]["range"]-1}
      start = con[i]["from"] + con[i]["range"]
    elseif con[i]["from"] > start and con[i]["from"] + con[i]["range"] >= start and con[i]["from"] + con[i]["range"] <= finish then
      res[#res+1] = { start, con[i]["from"]}
      res[#res+1] = { con[i]["to"], con[i]["to"] + con[i]["range"]}
      start = con[i]["from"] + con[i]["range"] + 1
    elseif con[i]["from"] > start and con[i]["from"] + con[i]["range"] >= start and con[i]["from"] + con[i]["range"] > finish then
      res[#res+1] = { start, con[i]["from"]-1}
      res[#res+1] = { con[i]["to"], finish - con[i]["from"] + con[i]["to"]}
      start = finish + 1
      return res
    elseif con[i]["from"] > finish and con[i]["from"] + con[i]["range"] > finish then
      res[#res+1] = {start, finish}
      return res
    elseif con[i]["from"] <= start and con[i]["from"] + con[i]["range"] >= finish then
      res[#res+1] = { start - con[i]["from"] + con[i]["to"], finish - con[i]["from"] + con[i]["to"]}
      return res
    else
      print("WELL SHIT")
    end
  end
  if start < finish then res[#res+1] = {start, finish} end
  return res
end

local function tableSort(tab)
  for i=1,#tab do
    for j=1,#tab-i do
      if tab[j]["from"] > tab[j+1]["from"] then tab[j], tab[j+1] = tab[j+1], tab[j] end
    end
  end
end


for line in io.lines("my_own/input.txt") do 
  lines[#lines + 1] = line
end

--[[
--Part 1
for i in string.gmatch(lines[1], "%d+") do
  seeds[#seeds+1] = tonumber(i)
end
--]]
local tmpSeeds = {}
for i in string.gmatch(lines[1], "%d+") do
  if #tmpSeeds ~= 2 then
    tmpSeeds[#tmpSeeds+1] = tonumber(i)
  end
  if #tmpSeeds == 2 then
    seeds[#seeds+1] = tmpSeeds
    tmpSeeds = {}
  end
end

for i=4,23 do
  seedToSoil[#seedToSoil+1] = loadLine(lines[i])
end

for i=26,53 do
  soilToFertilizer[#soilToFertilizer+1] = loadLine(lines[i])
end

for i=56,87 do
  fertilizerToWater[#fertilizerToWater+1] = loadLine(lines[i])
end

for i=90,121 do
  waterToLight[#waterToLight+1] = loadLine(lines[i])
end

for i=124,166 do
  lightToTemperature[#lightToTemperature+1] = loadLine(lines[i])
end

for i=169,202 do
  temperatureToHumidity[#temperatureToHumidity+1] = loadLine(lines[i])
end

for i=205,219 do
  humidityToLocation[#humidityToLocation+1] = loadLine(lines[i])
end

tableSort(seedToSoil)
tableSort(soilToFertilizer)  
tableSort(fertilizerToWater)
tableSort(waterToLight)
tableSort(lightToTemperature)
tableSort(temperatureToHumidity)
tableSort(humidityToLocation)

function TableConcat(t1,t2)
    for i=1,#t2 do
        t1[#t1+1] = t2[i]
    end
    return t1
end

local function runForAllFindResectableInter(x, y)
  local res = {}
  local tmp
  for i=1,#x do
    tmp = findResectableInter(x[i], y)
    res = TableConcat(res, tmp)
  end
  return res
end

for i=1,#seeds do
  seeds[i][2] = seeds[i][2] + seeds[i][1] - 1
end

local Soil = runForAllFindResectableInter(seeds, seedToSoil)
local Fertilizer = runForAllFindResectableInter(Soil, soilToFertilizer)
local Water = runForAllFindResectableInter(Fertilizer, fertilizerToWater)
local Light = runForAllFindResectableInter(Water, waterToLight)
local Temperature = runForAllFindResectableInter(Light, lightToTemperature)
local Humidity = runForAllFindResectableInter(Temperature, temperatureToHumidity)
local Location = runForAllFindResectableInter(Humidity, humidityToLocation)
result = TableConcat(result, Location)
  
local lowest = result[1][1]
for i=1,#result do if result[i][1] < lowest then lowest = result[i][1] end end
print(lowest)

--[[
--Part 1
local minLoc
for i=1,#seeds do
  local Soil = findResectable(seeds[i], seedToSoil)
  local Fertilizer = findResectable(Soil, soilToFertilizer)
  local Water = findResectable(Fertilizer, fertilizerToWater)
  local Light = findResectable(Water, waterToLight)
  local Temperature = findResectable(Light, lightToTemperature)
  local Humidity = findResectable(Temperature, temperatureToHumidity)
  local Location = findResectable(Humidity, humidityToLocation)
  if not minLoc or minLoc > Location then minLoc = Location end
end
print(minLoc)
--]]
