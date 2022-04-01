import itertools
import datetime
import time
import sys
from collections import Counter


def zigzag(s: str, num_rows: int) -> str:
    if num_rows == 1: return s

    s_dict = {i: "" for i in range(num_rows)}
    i = 0

    for j in itertools.cycle(itertools.chain(range(0, num_rows - 1, 1), range(num_rows - 1, 0, -1))):
        s_dict[j] += s[i]
        i += 1
        if i == len(s):
            break

    return "".join([s_dict[k] for k in s_dict])


def full_rounds(login_time: str, logout_time: str) -> int:
    if login_time > logout_time:
        days_delta = 1
    else:
        days_delta = 0

    login_stamp = datetime.datetime(year=2022,
                                    month=1,
                                    day=22,
                                    hour=int(login_time.split(":")[0]),
                                    minute=int(login_time.split(":")[1]))
    logout_stamp = datetime.datetime(year=2022,
                                    month=1,
                                    day=22 + days_delta,
                                    hour=int(logout_time.split(":")[0]),
                                    minute=int(logout_time.split(":")[1]))

    while login_stamp.minute % 15 != 0:
        login_stamp += datetime.timedelta(minutes=1)

    while logout_stamp.minute % 15 != 0:
        logout_stamp -= datetime.timedelta(minutes=1)

    session = datetime.timedelta(minutes=15)

    played = 0
    while login_stamp < logout_stamp:
        played += 1
        login_stamp = login_stamp + session

    return played


def longest_palindromic_substring(s: str) -> str:
    if len(s) == 1:
        return s
    s = " " + s
    se = list(enumerate(s))
    longest_pally = ""
    for i, char in se:
        if char not in s[(i+1):]:
            continue
        else:
            ending_indices = [i[0] for i in se[(i+1):] if i[1] == char]
            for ending_index in ending_indices[::-1]:
                if s[i:ending_index + 1] == s[ending_index:(i-1):-1]:
                    if len(s[i:ending_index + 1]) > len(longest_pally):
                        longest_pally = s[i:ending_index + 1]
                        if len(longest_pally) > len(s) / 2:
                            return longest_pally

    if longest_pally == "":
        return s[1]

    return longest_pally


def min_remove_to_make_valid(s: str) -> str:
    stack = ""
    stack_counter = 0
    invalids = []
    closers_left = True
    for i, c in enumerate(s):
        if ")" not in s[i:]:
            closers_left = False

        if c == "(":
            if not closers_left:
                invalids.append(i)
                continue

            stack_counter += 1
            stack += "("

        elif c == ")":
            stack_counter -= 1

            if stack_counter < 0:
                invalids.append(i)
                stack_counter += 1

    if stack_counter != 0:
        pass

    return "".join(y for x, y in enumerate(s) if x not in invalids)


def validate_stack_sequences(pushed, popped) -> bool:
    stack = []
    j = 0
    for i in range(len(popped)):
        next_pop = popped[i]
        if next_pop not in stack:
            while pushed[j] != next_pop:
                stack.append(pushed[j])
                j += 1

            stack.append(pushed[j])
            j += 1

            popped_val = stack.pop()
            if popped_val != next_pop:
                return False
        else:
            popped_val = stack.pop()
            if popped_val != next_pop:
                return False

    return True


def partition_labels(s: str):
    prev_p = 0
    partitions = []

    for p in range(1, len(s)):
        left_s = set(s[prev_p:p])
        right_s = set(s[p:])

        if len(left_s.union(right_s)) == len(left_s) + len(right_s):
            # valid partition
            partitions.append(p - prev_p)
            prev_p = p

    partitions.append(p - prev_p + 1)
    return partitions


def get_smallest_string(n: int, k: int) -> str:
    def get_remaining_avg(_k, potential_sum, _remaining_n):
        return (_k - potential_sum) / (_remaining_n - 1)

    remaining_n = n
    total_val = 0
    ans_str = ""
    prev_value = 1
    for i in range(n):
        if i != n-1:
            num_to_append = prev_value
            potential_vals_sum = total_val + num_to_append
            test_avg = get_remaining_avg(k, potential_vals_sum, remaining_n)
            while test_avg > 26:
                num_to_append += 1
                potential_vals_sum = total_val + num_to_append
                test_avg = get_remaining_avg(k, potential_vals_sum, remaining_n)

            total_val += num_to_append
            ans_str += chr(num_to_append + 96)
            prev_value = num_to_append
            remaining_n -= 1
        else:
            num_to_append = k - total_val
            total_val += num_to_append
            ans_str += chr(num_to_append + 96)

    return ans_str


def four_sum_count(nums1, nums2, nums3, nums4):
    iterable = [i for i in range(len(nums1))]
    perms = list(itertools.permutations(iterable))
    return


def time_it(func):
    def wrapper(*args):
        start_time = datetime.datetime.now()
        _ans = func(*args)
        print(f"time elapsed: {datetime.datetime.now() - start_time}")
        return _ans

    return wrapper


@time_it
def num_rescue_boats(people: list, limit):
    weight_set = sorted(list(set(people)), reverse=True)
    people_dict = dict(Counter(people))
    boats = 0
    heavy_i = 0
    light_i = -1
    heavy = weight_set[heavy_i]
    light = weight_set[light_i]
    while heavy >= light:
        if heavy + light > limit:
            # all heavies rescued
            boats += people_dict[heavy]
            heavy_i += 1
        elif heavy == light:
            if people_dict[heavy] % 2 == 0:
                boats += people_dict[heavy] / 2
            else:
                boats += 1 + (people_dict[heavy] - 1) / 2
            heavy_i += 1
        elif people_dict[heavy] < people_dict[light]:
            # all heavies rescued
            boats += people_dict[heavy]
            people_dict[light] -= people_dict[heavy]
            heavy_i += 1
        elif people_dict[heavy] > people_dict[light]:
            # all lights rescued
            boats += people_dict[light]
            people_dict[heavy] -= people_dict[light]
            light_i -= 1
        elif people_dict[heavy] == people_dict[light]:
            # all heavies and lights saved
            boats += people_dict[heavy]
            heavy_i += 1
            light_i -= 1

        if heavy_i == len(weight_set):
            break

        heavy = weight_set[heavy_i]
        light = weight_set[light_i]

    return int(boats)

@time_it
def two_city(costs):
    costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
    a = b = total_cost = 0
    for cost in costs:
        if a < len(costs) / 2 and b < len(costs) / 2:
            total_cost += min(cost)
            if cost.index(min(cost)) == 0:
                a += 1
            else:
                b += 1
        elif a == len(costs) / 2:
            total_cost += cost[1]
        elif b == len(costs) / 2:
            total_cost += cost[0]

    return total_cost


@time_it
def pivot_search(nums, target):
    if target == nums[0]:
        return True

@time_it
def longest_substring(s):
    l = 0
    r = 1
    ans = 1
    if s == "":
        return 0

    while r != len(s) + 1:
        test = s[l:r]
        if len(set(test)) == len(test):
            # this is a valid substring
            ans = len(test)
            r += 1
        else:
            l += 1
            r += 1

    return ans


@time_it
def reverse_int(x):
    s_x = list(str(x))
    if s_x[0] != "-":
        s_x.reverse()
    else:
        s_x = s_x[1:]
        s_x.reverse()
        s_x = ["-"] + s_x

    new_x = int("".join(s_x))

    if -2**31 <= new_x < 2**31:
        return new_x
    else:
        return 0


@time_it
def three_sum(nums: list):
    nums.sort()
    l = 0
    r = -1
    ans = []

    if len(nums) >= 3:
        while l < len(nums) + r:
            while nums[r] >= 0 and len(nums) + r > l:
                target = 0 - nums[l] - nums[r]
                if target in nums[l+1:r]:
                    ans.append([nums[l], target, nums[r]])
                r -= 1
            l += 1
            r = -1

    return list(set(ans))


@time_it
def search_matrix(matrix, target):
    def binary_search(arr):
        mid = len(arr) // 2
        if len(arr) != 1:
            if arr[mid] < target:
                return binary_search(arr[mid:])
            elif arr[mid] > target:
                return binary_search(arr[:mid])
            elif arr[mid] == target:
                return True
        elif arr[0] == target:
            return True
        else:
            return False

    def binary_search1(arr):
        if len(arr) == 1:
            return firsts.index(arr[0]), False
        mid = len(arr) // 2
        if arr[mid] == target:
            return 0, True
        elif arr[mid] < target:
            return binary_search1(arr[mid:])
        elif arr[mid] > target:
            return binary_search1(arr[:mid])

    firsts = [i[0] for i in matrix]

    row, found = binary_search1(firsts)

    if not found:
        return binary_search(matrix[row])
    else:
        return True

@time_it
def split_array(nums, m):
    global_splits = []
    num_splits = 0
    def find_winning_split(_splits):
        for split in _splits:
            if split[2] == 0:
                max_sum = max(split[0:2])
                winning_split = split
            else:
                if max(split[0:2]) < max_sum:
                    max_sum = max(split[0:2])
                    winning_split = split
        return winning_split

    def binary_split(arr):
        splits = [(sum(arr[:mid]), sum(arr[mid:]), mid) for mid in range(len(arr))]
        winning_split = find_winning_split(splits)
        arr = [arr[:winning_split[2]], arr[winning_split[2]:]]
        for a in arr:
            return binary_split(a)
        # if num_splits == m - 1:
        #     return max(winning_split[0:2])
        # elif len(arr) == m - 1:
        #     for j in arr:
        #         global_splits.append([j])
        # else:
        #     if winning_split[0] > winning_split[1]:
        #         global_splits.append(arr[winning_split[2]:])
        #         return binary_split(arr[:winning_split[2]], num_splits+1)
        #     elif winning_split[0] < winning_split[1]:
        #         global_splits.append(arr[:winning_split[2]])
        #         return binary_split(arr[winning_split[2]:], num_splits+1)
    if m != 1:
        return binary_split(nums)
    else:
        return sum(nums)


if __name__ == "__main__":
    # print(sys.path)
    # s = "lee(t(c)o)de)"
    # s2 = "a)b(c)d"
    # s3 = "))(("
    # s4 = "))(bing(bop)s(tring(y)pop"
    # pushed1 = [1, 2, 3, 4, 5]
    # popped1 = [4, 5, 3, 2, 1]
    #
    # pushed2 = [1, 2, 3, 4, 5]
    # popped2 = [4, 3, 5, 1, 2]
    # ans = validate_stack_sequences(pushed1, popped1)
    # ans2 = validate_stack_sequences(pushed2, popped2)

    # s = "ababcbacadefegdehijhklij"
    # s2 = "eccbbbbdec"
    # ans = partition_labels(s2)

    # n = 3
    # k = 27
    # ans = get_smallest_string(n, k)

    # nums1 = [1, 2]
    # nums2 = [-2, -1]
    # nums3 = [-1, 2]
    # nums4 = [0, 2]
    # ans = four_sum_count(nums1, nums2, nums3, nums4)

    # people = [3, 4, 5, 1]
    # limit = 5
    #
    # ans = num_rescue_boats(people, limit)

    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    # ans = two_city(costs)

    # nums = [1, 3, 4, 2, 2]
    # ans = find_duplicate(nums)

    # s = "au"
    # ans = longest_substring(s)

    # x = 1563847412
    # ans = reverse_int(x)

    # ans = three_sum(nums)

    # matrix = [[1],[3],[5]]
    #
    # ans = search_matrix(matrix,5)
    nums = [2,3,1,2,4,3]
    m = 5
    ans = split_array(nums, m)

    print(ans)