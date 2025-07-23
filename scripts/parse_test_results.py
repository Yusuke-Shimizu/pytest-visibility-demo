#!/usr/bin/env python3
"""
JUnit XMLレポートを解析してGitHub Actions用のマークダウンテーブルを生成するスクリプト
"""
import xml.etree.ElementTree as ET
import sys
import os


def parse_junit_xml(xml_file_path):
    """JUnit XMLファイルを解析してテスト結果を返す"""
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        test_results = []
        
        for testcase in root.findall('.//testcase'):
            name = testcase.get('name', 'Unknown')
            classname = testcase.get('classname', '')
            time = testcase.get('time', '0')
            
            # テスト名を表示用に短縮
            display_name = name.replace('test_', '').replace('_', ' ').title()
            
            # 失敗、エラー、スキップをチェック
            failure = testcase.find('failure')
            error = testcase.find('error')
            skipped = testcase.find('skipped')
            
            if failure is not None:
                status = "❌ FAIL"
                details = failure.get('message', 'Failed')[:50] + "..."
            elif error is not None:
                status = "💥 ERROR"
                details = error.get('message', 'Error')[:50] + "..."
            elif skipped is not None:
                status = "⏭️ SKIP"
                details = skipped.get('message', 'Skipped')[:50] + "..."
            else:
                status = "✅ PASS"
                details = "Success"
            
            test_results.append({
                'name': display_name,
                'status': status,
                'time': float(time),
                'details': details
            })
        
        # 統計情報を計算
        total = len(root.findall('.//testcase'))
        failures = len(root.findall('.//failure'))
        errors = len(root.findall('.//error'))
        skipped = len(root.findall('.//skipped'))
        passed = total - failures - errors - skipped
        
        stats = {
            'total': total,
            'passed': passed,
            'failed': failures,
            'errors': errors,
            'skipped': skipped
        }
        
        return test_results, stats
        
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return [], {}


def generate_markdown_table(test_results, stats):
    """テスト結果からマークダウンテーブルを生成"""
    print("### Test Results Table")
    print("")
    print("| Test Name | Status | Time (s) | Details |")
    print("|-----------|--------|----------|---------|")
    
    for result in test_results:
        print(f"| {result['name']} | {result['status']} | {result['time']:.3f} | {result['details']} |")
    
    print("")
    print("### Summary Statistics")
    print("")
    print("| Metric | Count |")
    print("|--------|-------|")
    print(f"| Total Tests | {stats['total']} |")
    print(f"| ✅ Passed | {stats['passed']} |")
    print(f"| ❌ Failed | {stats['failed']} |")
    print(f"| 💥 Errors | {stats['errors']} |")
    print(f"| ⏭️ Skipped | {stats['skipped']} |")


def main():
    """メイン関数"""
    xml_file = 'pytest-report.xml'
    
    if not os.path.exists(xml_file):
        print(f"Error: {xml_file} not found")
        sys.exit(1)
    
    test_results, stats = parse_junit_xml(xml_file)
    
    if test_results or stats:
        generate_markdown_table(test_results, stats)
    else:
        print("No test results found or error occurred")


if __name__ == "__main__":
    main()