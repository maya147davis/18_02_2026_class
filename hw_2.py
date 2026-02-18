
voters: list = []

while True:
    _id = int(input('Enter id [1-100] to exit -999:'))
    if _id == -999:
        break
    if not 1 <= _id <= 100:
        continue
    voters.append(_id)

if len(voters) == 0:
    print('no voters')
else:
    # voters = [1,2,3,3,4]
    valid_voters = set(voters)  # {1,2,3,4}
    invalid_voters = set()

    if len(valid_voters) != len(voters):
        # makes error!
        # for x in voters:
        #     voters.remove(x)
        for _id in voters:
            if voters.count(_id) > 1:
                valid_voters.discard(_id)
                invalid_voters.add(_id)

    print('valid_voters', valid_voters)
    print('invalid_voters', invalid_voters)
    print('attempts', len(voters))