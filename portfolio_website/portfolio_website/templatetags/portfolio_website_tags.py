```python
from django import template

register = template.Library()

@register.simple_tag
def current_year():
    """Returns the current year."""
    import datetime
    return datetime.datetime.now().year

@register.filter
def to_class_name(value):
    """Returns the class name of the value."""
    return value.__class__.__name__
```