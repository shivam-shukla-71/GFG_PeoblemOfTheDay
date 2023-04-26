def is_possible_to_get_seats( n : int, m : int, seats : int) -> bool:
        # code here
        if(n==0):return True
        if sum(seats) > len(seats) - n:
            return False  # not enough seats for all people
        prev_seat = -2
        for i, seat in enumerate(seats):
            if seat == 1:
                prev_seat = i
                continue
            if i - prev_seat == 1:
                continue
            if i == len(seats) - 1 or seats[i+1] == 0:
                n -= 1
                prev_seat = i
                if n == 0:
                    return True
        return False

n=2
m=7
seeats=[0,1,0,0,0,1,0]