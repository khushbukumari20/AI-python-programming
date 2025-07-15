def tower_of_hanoi(num, source, aux, target):
    """
    Solve the Tower of Hanoi puzzle.
    
    Args:
        num (int): Number of disks.
        source (str): The name of the source tower.
        aux (str): The name of the auxiliary tower.
        target (str): The name of the target tower.
    """
    if num == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move num-1 disks from source to auxiliary using target as auxiliary
    tower_of_hanoi(num - 1, source, target, aux)
    print(f"Move disk {num} from {source} to {target}")
    # Move num-1 disks from auxiliary to target using source as auxiliary
    tower_of_hanoi(num - 1, aux, source, target)

# Example usage
num_disks = 3
tower_of_hanoi(num_disks, "A", "B", "C")