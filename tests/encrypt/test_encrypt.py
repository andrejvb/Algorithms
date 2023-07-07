from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('ABCBA', 3) == 'CBA_AB'
    assert encrypt_message('DCBA', 6) == 'ABCD'
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('ABCAB', '3')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(3, 3)
