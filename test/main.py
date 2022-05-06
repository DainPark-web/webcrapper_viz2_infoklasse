from stack import getpages, get_stack_page
from save import save_to_csv

last_page = getpages()

jobs = get_stack_page(last_page)

save_to_csv(jobs)
