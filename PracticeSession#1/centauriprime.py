def get_ruler(kingdom):
  ruler = 'nobody'
  vowels = ['a', 'e', 'i', 'o', 'u']
  if kingdom[-1].lower() in vowels:
    ruler = 'Alice'
  elif kingdom[-1].lower() not in vowels and kingdom[-1].lower() != 'y':
    ruler = 'Bob' 
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
