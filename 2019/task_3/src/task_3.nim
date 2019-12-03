import math, strutils, strformat, sequtils


proc solveFirst*(input: seq[string]): int
proc solveSecond*(input: seq[string]): int

type 
  Point = object
    x, y: int

  Line = object
    a, b: Point

proc distFromStart(point: Point): int
proc getIntersection(first, second: Line): (Point, bool)
proc isHorizontal(line: Line): bool
proc includesPoint(line: Line, point: Point): bool

proc parseWire(input: string): seq[Line]

when isMainModule:
  let input = readFile("input.txt").strip.splitLines

  echo solveFirst(input)
  echo solveSecond(input)

proc getIntersections(firstWire, secondWire: seq[Line]): seq[Point] =
  var intersections: seq[Point]

  for firstLine in firstWire:
    for secondLine in secondWire:
      let (point, intersected) = firstLine.getIntersection(secondLine)
      if intersected:
        intersections.add(point) 

  return intersections

proc solveFirst*(input: seq[string]): int =
  let firstWire = parseWire(input[0]) 
  let secondWire = parseWire(input[1]) 

  var intersections = getIntersections(firstWire, secondWire)

  var closestIntersection = Point(x: 9001, y: 9001)
  for intersection in intersections:
    if intersection.distFromStart == 0:
      continue

    if intersection.distFromStart < closestIntersection.distFromStart:
      closestIntersection = intersection

  return closestIntersection.distFromStart

proc solveSecond*(input: seq[string]): int =
  return -1

proc distFromStart(point: Point): int =
  return point.x.abs + point.y.abs 

proc includesPoint(line: Line, point: Point): bool =
  let aX = line.a.x
  let aY = line.a.y
  let bX = line.b.x
  let bY = line.b.y

  if line.isHorizontal:
    return line.a.y == point.y and (point.x >= min(aX, bX) and point.x <= max(aX, bX))
  else:
    return line.a.x == point.x and (point.y >= min(aY, bY) and point.y <= max(aY, bY))

proc isHorizontal(line: Line): bool =
  return line.a.y == line.b.y

# TODO use ref on point
proc getIntersection(first, second: Line): (Point, bool) =
  if first.isHorizontal == second.isHorizontal:
    return (Point(x: 0, y: 0), false)

  var x, y: int

  if first.isHorizontal:
    y = first.a.y
    x = second.a.x
  else:
    x = first.a.x
    y = second.a.y

  let point = Point(x: x, y: y)
  return (point, first.includesPoint(point) and second.includesPoint(point))
  
proc parseWire(input: string): seq[Line] =
  let commands = input.split(',')

  var lines: seq[Line]

  var currPoint = Point(x:0 , y: 0)

  for command in commands:
    let commandType = command[0]
    let dist = command[1..^1].parseInt

    var targetPoint: Point
    case commandType:
      of 'U':
        targetPoint = Point(x: currPoint.x, y: currPoint.y - dist) 
      of 'R':
        targetPoint = Point(x: currPoint.x + dist, y:currPoint.y) 
      of 'D':
        targetPoint = Point(x: currPoint.x, y: currPoint.y + dist) 
      of 'L':
        targetPoint = Point(x: currPoint.x - dist, y: currPoint.y) 
      else:
        echo fmt"unknown command type {commandType}"

    lines.add(Line(a: Point(x: currPoint.x, y: currPoint.y), b: targetPoint))

    currPoint = targetPoint
      
  return lines
