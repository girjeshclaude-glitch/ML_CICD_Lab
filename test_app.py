def test_demo():
    assert 5 + 5 == 10

def test_main_output(capsys):
    from app import main

    main()

    captured = capsys.readouterr()
    assert "Hello Jenkins CI/CD Pipeline" in captured.out
