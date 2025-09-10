def stack_cubes(blocks):
    
    left = 0
    right = len(blocks) - 1
    top = float('inf')

    while left <= right:
        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1
        else:
            chosen = blocks[right]
            right -= 1

        if chosen > top:
            return "No"

        top = chosen

    return "Yes"