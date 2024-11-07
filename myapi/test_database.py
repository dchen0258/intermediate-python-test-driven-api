from database import DataBase

def test_get():
    # GIVEN
    db = DataBase()
    db._data = {"example_key" : "example_value"}

    # WHEN
    result = db.get("example_key")
    
    #THEN
    assert result == "example_value"

def test_put():
    # GIVEN
    db = DataBase()

    # WHEN 
    db.put("some_key", "some_value")

    # THEN
    assert db._data["some_key"] == "some_value"

def test_all():
    # GIVEN
    db = DataBase()
    value = {"example_key" : "example_value", "some_key": "some_value"}
    db._data = value

    # WHEN
    result = db.all()

    #THEN 
    assert result == value

def test_delete():
    # GIVEN
    db = DataBase()
    value = {"example_key" : "example_value"}
    db._data = value

    # WHEN
    db.delete("example_key")

    #THEN 
    assert db._data == {}