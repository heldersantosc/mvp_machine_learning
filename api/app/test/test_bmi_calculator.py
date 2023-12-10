from app.models import BMI_Calculator


def test_bmi_calculator_single_input():
    # Teste com um único conjunto de dados
    weight = [70]
    height = [170]

    expected_bmi = [24.221453287197235]

    bmi_calculator = BMI_Calculator()
    calculated_bmi = bmi_calculator.calculate_batch(weight, height)

    assert calculated_bmi == expected_bmi


def test_bmi_calculator_multiple_inputs():
    # Teste com vários conjuntos de dados
    weights = [70, 80, 90]
    heights = [170, 180, 190]

    expected_bmis = [
        24.221453287197235,
        24.691358024691358,
        24.930747922437675,
    ]

    bmi_calculator = BMI_Calculator()
    calculated_bmis = bmi_calculator.calculate_batch(weights, heights)

    assert calculated_bmis == expected_bmis
