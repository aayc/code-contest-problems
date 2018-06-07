# Problem: determine if there are k distinct numbers among students
# Output: "YES" then index of each student in the team /"NO"

n, k = [int(s) for s in raw_input().split(" ")]
students = [int(s) for s in raw_input().split(" ")]

distinct = []
seen = set()
for i in range(0, len(students)):
    if students[i] not in seen:
        distinct.append(i + 1)
        seen.add(students[i])

    if len(distinct) == k:
        print "YES"
        print " ".join([str(id) for id in distinct])
        break
else:
    print "NO"
