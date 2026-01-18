def count_message(msg, count=0):
    count += 1
    print(f"{msg} -> count: {count}")
    return count

count_message("heya")
count_message("hello")
count_message("yo")
count_message("hi")