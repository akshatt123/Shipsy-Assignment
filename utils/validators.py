def validate_task_data(form_data):
    """Validate task form data"""
    errors = []
    
    title = form_data.get('title', '').strip()
    status = form_data.get('status', '')
    priority = form_data.get('priority', '')
    
    # Title validation
    if not title:
        errors.append('Title is required!')
    elif len(title) > 200:
        errors.append('Title must be less than 200 characters!')
    
    # Status validation
    valid_statuses = ['pending', 'in_progress', 'completed']
    if status not in valid_statuses:
        errors.append('Invalid status selected!')
    
    # Priority validation
    valid_priorities = ['low', 'medium', 'high']
    if priority not in valid_priorities:
        errors.append('Invalid priority selected!')
    
    # Description validation
    description = form_data.get('description', '').strip()
    if len(description) > 1000:
        errors.append('Description must be less than 1000 characters!')
    
    return errors

def validate_user_data(form_data):
    """Validate user registration data"""
    errors = []
    
    username = form_data.get('username', '').strip()
    password = form_data.get('password', '')
    
    # Username validation
    if not username:
        errors.append('Username is required!')
    elif len(username) < 3:
        errors.append('Username must be at least 3 characters long!')
    elif len(username) > 50:
        errors.append('Username must be less than 50 characters!')
    elif not username.isalnum():
        errors.append('Username must contain only letters and numbers!')
    
    # Password validation
    if not password:
        errors.append('Password is required!')
    elif len(password) < 6:
        errors.append('Password must be at least 6 characters long!')
    elif len(password) > 100:
        errors.append('Password must be less than 100 characters!')
    
    return errors
