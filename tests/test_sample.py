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
    ])
    def test_string_upper(self, input_str, expected):
        """パラメータ化テスト - 大文字変換"""
        assert input_str.upper() == expected