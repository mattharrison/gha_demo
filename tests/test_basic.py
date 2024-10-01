import sk_stepwise as sw
import pytest


def test_initialization():
    model = None
    rounds = []
    optimizer = sw.StepwiseHyperoptOptimizer(model, rounds)
    assert optimizer is not None



@pytest.mark.matt
def test_matt():
    assert 'matt' == 'matt'



