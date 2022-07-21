from datetime import datetime
from src.core import cli
from src.core.utils import get_vaccination_filename



def test_get_daily_information():
    csv_file = get_vaccination_filename()
    df = cli.get_daily_information(csv_file)
    
    
def test_last_vaccination_date():
    now = datetime.now()
    dates = cli.check_last_update(now)
    print(dates)
