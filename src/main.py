import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Credit score service")


@app.get("/user_credits/{user_id}")
async def get_user_by_id():
    """
    Метод для отримання інформації про кредити клієнта
    :return:
    """
    pass


@app.post("/plans_insert")
async def post_plans_insert():
    """
    Метод для завантаження планів на новий місяць
    :return:
    """
    pass


@app.get("/plans_performance")
async def get_plans_performance():
    """
    Метод для отримання інформації про виконання планів на певну дату
    :return:
    """
    pass


@app.get("/year_performance")
async def get_year_performance():
    """
    Метод для отримання зведеної інформації за заданий рік. Групування по-місячне.
    :return:
    """
    pass


def main():
    uvicorn.run("src.main:app")


if __name__ == '__main__':
    main()
