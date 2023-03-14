from smallest_not_in_array import solution

def test_solution():
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    assert solution([-1, -3]) == 1
    assert solution([-3, -1, 0]) == 1
    assert solution([0]) == 1
    assert solution([1, 3, 6, 4, 1, 2, 5, 7, 8, 9]) == 10
    assert solution([1]) != 1