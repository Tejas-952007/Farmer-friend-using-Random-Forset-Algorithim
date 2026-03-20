"""
Basic unit tests for the fertilizer advisor (no model needed).
To run: pytest tests/
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from fertilizer import get_fertilizer_advice

def test_known_crop():
    result = get_fertilizer_advice("rice")
    assert "fertilizer" in result
    assert "tip" in result
    assert result["fertilizer"] != ""

def test_unknown_crop_returns_default():
    result = get_fertilizer_advice("xyz_unknown_crop")
    assert result["fertilizer"] == "NPK 10-26-26"

def test_case_insensitive():
    r1 = get_fertilizer_advice("WHEAT")
    r2 = get_fertilizer_advice("wheat")
    assert r1 == r2

def test_all_major_crops():
    crops = ["rice","wheat","maize","cotton","sugarcane","chickpea","mango","banana","grapes"]
    for crop in crops:
        result = get_fertilizer_advice(crop)
        assert result["fertilizer"] != "", f"Missing fertilizer for {crop}"
