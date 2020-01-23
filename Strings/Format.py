room_text="Welcome to room number {room} and floor number is {floor}"

for i in range(1,21):
    print(room_text.format(room=i,floor=i+1))