def test_event_posting(client):
    """Test that an event is posted correctly"""
    login(client, "testuser", "testpass")  # Using login helper function
    
    rv = client.post(
        "/post_event",
        data=dict(event_name="New Event", event_date="2023-11-01", description="This is a new event"),
        follow_redirects=True,
    )
    
    assert b"New Event successfully posted" in rv.data
    assert rv.status_code == 200
    

def test_create_user_account(client):
    """Test creating a new user account"""
    rv = client.post(
        "/register",
        data=dict(username="newuser", password="newpass", email="newuser@email.com"),
        follow_redirects=True,
    )
    assert b"Account successfully created" in rv.data
    assert rv.status_code == 200



def test_event_deletion(client):
    """Test that an event is deleted correctly"""
    login(client, "testuser", "testpass")  # Using login helper function
    
    # First, post an event to delete later
    rv = client.post(
        "/post_event",
        data=dict(event_name="Event to Delete", event_date="2023-11-02", description="This event will be deleted"),
        follow_redirects=True,
    )
    
    # Now delete the event
    rv = client.post(
        "/delete_event",
        data=dict(event_id=1),  # Assuming the event to delete has ID=1
        follow_redirects=True,
    )
    
    assert b"Event successfully deleted" in rv.data
    assert rv.status_code == 200