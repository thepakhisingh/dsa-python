"""
Test cases for every drill.

Each case is (function_name, args_tuple, expected_result).
Peeking in here is allowed — the expected outputs are already in the
docstrings. There are no answers in this file, only questions.
"""

GRAPH_A = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": [], "e": []}
GRAPH_B = {"1": ["2"], "2": ["3"], "3": ["1"]}

CASES = {
    1: [
        ("second_largest", ([3, 1, 4, 4, 5],), 4),
        ("second_largest", ([2, 2, 2],), None),
        ("second_largest", ([1],), None),
        ("second_largest", ([],), None),
        ("second_largest", ([5, 5, 4, 3],), 4),
        ("second_largest", ([-1, -2],), -2),

        ("rotate_right", ([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
        ("rotate_right", ([1, 2, 3], 4), [3, 1, 2]),
        ("rotate_right", ([1, 2, 3], 0), [1, 2, 3]),
        ("rotate_right", ([1, 2, 3], 3), [1, 2, 3]),
        ("rotate_right", ([], 3), []),

        ("chunk", ([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
        ("chunk", ([1, 2, 3], 5), [[1, 2, 3]]),
        ("chunk", ([1, 2, 3, 4], 2), [[1, 2], [3, 4]]),
        ("chunk", ([], 3), []),

        ("flatten_once", ([[1, 2], [3], [], [4, 5]],), [1, 2, 3, 4, 5]),
        ("flatten_once", ([[1, [2]], [3]],), [1, [2], 3]),
        ("flatten_once", ([],), []),

        ("running_max", ([3, 1, 4, 1, 5],), [3, 3, 4, 4, 5]),
        ("running_max", ([5, 4, 3],), [5, 5, 5]),
        ("running_max", ([],), []),
        ("running_max", ([7],), [7]),

        ("move_zeros", ([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
        ("move_zeros", ([0, 0],), [0, 0]),
        ("move_zeros", ([1, 2],), [1, 2]),
        ("move_zeros", ([],), []),
    ],

    2: [
        ("char_frequency", ("hello",), {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("char_frequency", ("",), {}),
        ("char_frequency", ("aaa",), {"a": 3}),

        ("two_sum", ([2, 7, 11, 15], 9), [0, 1]),
        ("two_sum", ([3, 2, 4], 6), [1, 2]),
        ("two_sum", ([3, 3], 6), [0, 1]),
        ("two_sum", ([-1, -2, -3], -5), [1, 2]),

        ("common_elements", ([1, 2, 2, 3], [2, 3, 4]), [2, 3]),
        ("common_elements", ([1], [2]), []),
        ("common_elements", ([], [1, 2]), []),
        ("common_elements", ([5, 1, 3], [3, 5]), [3, 5]),

        ("group_by_length", (["hi", "cat", "to", "dog"],),
         {2: ["hi", "to"], 3: ["cat", "dog"]}),
        ("group_by_length", ([],), {}),
        ("group_by_length", (["a"],), {1: ["a"]}),

        ("has_duplicate_within_k", ([1, 2, 3, 1], 3), True),
        ("has_duplicate_within_k", ([1, 2, 3, 1], 2), False),
        ("has_duplicate_within_k", ([1, 0, 1, 1], 1), True),
        ("has_duplicate_within_k", ([1, 2, 3], 5), False),
        ("has_duplicate_within_k", ([], 3), False),

        ("unique_paths_visited", ("RRLL",), 3),
        ("unique_paths_visited", ("",), 1),
        ("unique_paths_visited", ("UD",), 2),
        ("unique_paths_visited", ("RULD",), 4),
    ],

    3: [
        ("squares_of_evens", ([1, 2, 3, 4],), [4, 16]),
        ("squares_of_evens", ([1, 3],), []),
        ("squares_of_evens", ([],), []),

        ("invert_dict", ({"a": 1, "b": 2},), {1: "a", 2: "b"}),
        ("invert_dict", ({},), {}),

        ("sort_by_length_then_alpha", (["pear", "fig", "kiwi", "date"],),
         ["fig", "date", "kiwi", "pear"]),
        ("sort_by_length_then_alpha", ([],), []),
        ("sort_by_length_then_alpha", (["bb", "aa", "c"],), ["c", "aa", "bb"]),

        ("sort_by_frequency", ([4, 4, 1, 2, 2, 2, 3],), [2, 2, 2, 4, 4, 1, 3]),
        ("sort_by_frequency", ([1, 2],), [1, 2]),
        ("sort_by_frequency", ([],), []),
        ("sort_by_frequency", ([9, 9, 1, 1, 5],), [1, 1, 9, 9, 5]),

        ("top_k_frequent", (["a", "b", "a", "c", "b", "a"], 2), ["a", "b"]),
        ("top_k_frequent", (["z", "y"], 2), ["y", "z"]),
        ("top_k_frequent", (["x", "x"], 1), ["x"]),

        ("sort_people", ([("ana", 31), ("bo", 24), ("cy", 31)],),
         [("ana", 31), ("cy", 31), ("bo", 24)]),
        ("sort_people", ([],), []),
        ("sort_people", ([("z", 1), ("a", 1)],), [("a", 1), ("z", 1)]),
    ],

    4: [
        ("is_palindrome", ("A man, a plan, a canal: Panama",), True),
        ("is_palindrome", ("race a car",), False),
        ("is_palindrome", ("",), True),
        ("is_palindrome", (".,",), True),
        ("is_palindrome", ("ab",), False),
        ("is_palindrome", ("0P",), False),

        ("reverse_words", ("the sky  is blue",), "blue is sky the"),
        ("reverse_words", ("  hello world  ",), "world hello"),
        ("reverse_words", ("   ",), ""),
        ("reverse_words", ("one",), "one"),

        ("are_anagrams", ("listen", "silent"), True),
        ("are_anagrams", ("rat", "car"), False),
        ("are_anagrams", ("a", "ab"), False),
        ("are_anagrams", ("", ""), True),

        ("longest_common_prefix", (["flower", "flow", "flight"],), "fl"),
        ("longest_common_prefix", (["dog", "car"],), ""),
        ("longest_common_prefix", ([],), ""),
        ("longest_common_prefix", (["single"],), "single"),
        ("longest_common_prefix", (["ab", "ab"],), "ab"),

        ("compress", ("aaabbc",), "a3b2c"),
        ("compress", ("abc",), "abc"),
        ("compress", ("aabb",), "aabb"),
        ("compress", ("",), ""),
        ("compress", ("aaaa",), "a4"),

        ("first_non_repeating", ("swiss",), "w"),
        ("first_non_repeating", ("aabb",), ""),
        ("first_non_repeating", ("x",), "x"),
        ("first_non_repeating", ("",), ""),
    ],

    5: [
        ("bfs_shortest_path", (GRAPH_A, "a", "d"), 2),
        ("bfs_shortest_path", (GRAPH_A, "a", "a"), 0),
        ("bfs_shortest_path", (GRAPH_A, "a", "e"), -1),
        ("bfs_shortest_path", (GRAPH_A, "a", "b"), 1),
        ("bfs_shortest_path", (GRAPH_B, "1", "3"), 2),

        ("build_adjacency", ([("a", "b"), ("a", "c")],),
         {"a": ["b", "c"], "b": ["a"], "c": ["a"]}),
        ("build_adjacency", ([],), {}),
        ("build_adjacency", ([("y", "x")],), {"y": ["x"], "x": ["y"]}),

        ("top_k_common", (["a", "b", "a", "c", "b", "a"], 2), ["a", "b"]),
        ("top_k_common", (["q"], 1), ["q"]),
        ("top_k_common", ([], 2), []),

        ("group_anagrams", (["eat", "tea", "tan"],),
         {"aet": ["eat", "tea"], "ant": ["tan"]}),
        ("group_anagrams", ([],), {}),

        ("sliding_window_max", ([1, 3, -1, -3, 5, 3], 3), [3, 3, 5, 5]),
        ("sliding_window_max", ([1], 1), [1]),
        ("sliding_window_max", ([], 3), []),
        ("sliding_window_max", ([9, 8, 7], 2), [9, 8]),

        ("is_valid_parentheses", ("([]{})",), True),
        ("is_valid_parentheses", ("(]",), False),
        ("is_valid_parentheses", ("(",), False),
        ("is_valid_parentheses", ("",), True),
        ("is_valid_parentheses", ("]",), False),
        ("is_valid_parentheses", ("([)]",), False),
    ],

    6: [
        ("k_largest", ([7, 2, 9, 4], 2), [9, 7]),
        ("k_largest", ([1], 5), [1]),
        ("k_largest", ([], 3), []),
        ("k_largest", ([3, 3, 3], 2), [3, 3]),

        ("merge_sorted_lists", ([[1, 4, 5], [1, 3], [2, 6]],), [1, 1, 2, 3, 4, 5, 6]),
        ("merge_sorted_lists", ([],), []),
        ("merge_sorted_lists", ([[], [1]],), [1]),
        ("merge_sorted_lists", ([[1, 2, 3]],), [1, 2, 3]),

        ("count_in_range", ([1, 3, 3, 5, 8], 3, 5), 3),
        ("count_in_range", ([1, 3, 3, 5, 8], 4, 4), 0),
        ("count_in_range", ([], 1, 5), 0),
        ("count_in_range", ([1, 2, 3], 0, 10), 3),

        ("insert_position", ([1, 3, 5, 6], 5), 2),
        ("insert_position", ([1, 3, 5, 6], 2), 1),
        ("insert_position", ([1, 3, 5, 6], 7), 4),
        ("insert_position", ([], 1), 0),
        ("insert_position", ([2, 2, 2], 2), 0),

        ("climb_stairs", (2,), 2),
        ("climb_stairs", (3,), 3),
        ("climb_stairs", (0,), 1),
        ("climb_stairs", (1,), 1),
        ("climb_stairs", (45,), 1836311903),

        ("coin_change", ([1, 5, 11], 15), 3),
        ("coin_change", ([2], 3), -1),
        ("coin_change", ([1, 2, 5], 0), 0),
        ("coin_change", ([1, 2, 5], 11), 3),
    ],
}
