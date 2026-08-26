def count_lines(data):
    count = 0

    for line in data.split("\n"):
        if not line.startswith("T"):
            count += 1

    return count


data = """A boys is plying thear.
Thear is a playground.
An airport in the sky.
The sky is pink.
Alphabets and number are in the password."""

print(count_lines(data))