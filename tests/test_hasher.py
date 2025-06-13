from services import PasswordHasher

def test_password_hash_and_verify():
    raw_password = "TestPass123"
    hashed = PasswordHasher.hash(raw_password)
    assert hashed != raw_password
    assert PasswordHasher.verify(raw_password, hashed)
    assert not PasswordHasher.verify("WrongPass", hashed)