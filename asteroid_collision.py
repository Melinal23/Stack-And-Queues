"""
We are given an array asteroids of integers representing
asteroids in a row.

For each asteroid, the absolute value represents its size, and
the sign represents its direction (positive means right and negative
means left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If bot are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

EX:
Input: [5,10,-5]
Output: [5,10]

EX:
Input: [8,-8]
Output: []

EX:
Input: [10,2,-5]
Output: [10]

EX:
Input: [-2,-1,1,2]
Output: [-2,-1,1,2]
"""

def asteroid_collisions(asteroids):

  output = []

  for asteroid in asteroids:
    while output and asteroid < 0 and 0 < output[-1]:
      if output[-1] < abs(asteroid):
        output.pop()
        continue
      elif output[-1] == abs(asteroid):
        output.pop()
      break
    else:
      output.append(asteroid)

  return output

print(asteroid_collisions([8,-8]))
print(asteroid_collisions([10,2,-5]))
print(asteroid_collisions([-2,-1,1,2]))
print(asteroid_collisions([5,10,-5]))
print(asteroid_collisions([10,5,-2,-8,7,14,-15]))

