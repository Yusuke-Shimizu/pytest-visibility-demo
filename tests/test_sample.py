"""サンプルテストファイル - GitHub Actions での見やすさを確認するため"""

import pytest


def add(a, b):
    """簡単な足し算関数"""
    return a + b


def divide(a, b):
    """割り算関数（ゼロ除算エラーのテスト用）"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestBasicOperations:
    """基本的な演算のテストクラス"""
    
    def test_add_positive_numbers(self):
        """正の数の足し算テスト"""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """負の数の足し算テスト"""
        assert add(-1, -2) == -3
        assert add(-5, 5) == 0
    
    def test_divide_normal_case(self):
        """通常の割り算テスト"""
        assert divide(10, 2) == 5.0
        assert divide(9, 3) == 3.0
    
    def test_divide_by_zero_raises_error(self):
        """ゼロ除算エラーのテスト"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    @pytest.mark.slow
    def test_slow_operation(self):
        """時間のかかるテスト（マーカー付き）"""
        import time
        time.sleep(0.1)  # 0.1秒待機
        assert True
    
    def test_intentional_failure(self):
        """意図的な失敗テスト（GitHub Actions での表示確認用）"""
        # このテストは失敗します - コメントアウトして実際のテストでは削除してください
        # assert False, "これは意図的な失敗です - GitHub Actions での表示を確認するため"
        assert True  # 実際は成功させておく
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
        (100, 200, 300),
        (0, 0, 0),
    ])
    def test_add_parametrized(self, a, b, expected):
        """パラメータ化された足し算テスト"""
        assert add(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5.0),
        (15, 3, 5.0),
        (100, 10, 10.0),
        (1, 4, 0.25),
        (0, 5, 0.0),
    ])
    def test_divide_parametrized(self, a, b, expected):
        """パラメータ化された割り算テスト"""
        assert divide(a, b) == expected
    
    @pytest.mark.parametrize("a,b,exception_type", [
        (10, 0, ValueError),
        (5, 0, ValueError),
        (100, 0, ValueError),
    ])
    def test_divide_by_zero_parametrized(self, a, b, exception_type):
        """パラメータ化されたゼロ除算エラーテスト"""
        with pytest.raises(exception_type, match="Cannot divide by zero"):
            divide(a, b)


class TestStringOperations:
    """文字列操作のテストクラス"""
    
    def test_string_concatenation(self):
        """文字列結合のテスト"""
        result = "Hello" + " " + "World"
        assert result == "Hello World"
    
    def test_string_length(self):
        """文字列長のテスト"""
        assert len("Python") == 6
        assert len("") == 0
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hello", "HELLO"),
        ("World", "WORLD"),
        ("PyThOn", "PYTHON"),
        ("python", "PYTHON"),
        ("TEST", "TEST"),
        ("", ""),
    ])
    def test_string_upper(self, input_str, expected):
        """パラメータ化テスト - 大文字変換"""
        assert input_str.upper() == expected
    
    @pytest.mark.parametrize("input_str,expected", [
        ("HELLO", "hello"),
        ("WORLD", "world"),
        ("PyThOn", "python"),
        ("TEST", "test"),
        ("", ""),
    ])
    def test_string_lower(self, input_str, expected):
        """パラメータ化テスト - 小文字変換"""
        assert input_str.lower() == expected
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hello", 5),
        ("world", 5),
        ("python", 6),
        ("", 0),
        ("a", 1),
        ("testing", 7),
    ])
    def test_string_length_parametrized(self, input_str, expected):
        """パラメータ化テスト - 文字列長"""
        assert len(input_str) == expected


class TestListOperations:
    """リスト操作のテストクラス"""
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 3], 3),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5], 5),
    ])
    def test_list_length(self, input_list, expected):
        """パラメータ化テスト - リスト長"""
        assert len(input_list) == expected
    
    @pytest.mark.parametrize("input_list,item,expected", [
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 4, False),
        ([], 1, False),
        (["a", "b", "c"], "b", True),
    ])
    def test_list_contains(self, input_list, item, expected):
        """パラメータ化テスト - リスト包含"""
        assert (item in input_list) == expected
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 1, 2, 2], [2, 2, 1, 1]),
    ])
    def test_list_reverse(self, input_list, expected):
        """パラメータ化テスト - リスト反転"""
        input_list.reverse()
        assert input_list == expected