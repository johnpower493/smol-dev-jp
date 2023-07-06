```python
from .models import Portfolio

def portfolio(request):
    portfolio_items = Portfolio.objects.all()
    return {'portfolio_items': portfolio_items}
```