import asyncio
import time

async def io_bound_task(task_id, delay):
    print(f"Task {task_id} boshlandi")
    await asyncio.sleep(delay)
    print(f"Task {task_id} tugadi")

async def main():
    tasks = [
        io_bound_task(1, 2),
        io_bound_task(2, 3),
        io_bound_task(3, 1)
    ]

    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"Tasklar barchasi tugadi. Vaqt: {end_time - start_time} soniya")

asyncio.run(main())
```

Kodda quyidagilar qo'llangan:

- `asyncio` moduli import qilingan, chunki u bizga asinxron ishlash imkonini beradi.
- `io_bound_task` funksiyasi yaratilgan, u asinxron ishlash uchun `async` kalit so'zidan foydalanadi. Funksiya `delay` parametriga asosan `asyncio.sleep` funksiyasidan foydalanib, bir necha soniya davom etuvchi vazifani bajaradi.
- `main` funksiyasi yaratilgan, u bizga asinxron vazifalarni birlashtirish imkonini beradi. Funksiya `asyncio.gather` funksiyasidan foydalanib, `io_bound_task` funksiyasining uchta nusxasini birlashtiradi.
- `asyncio.run(main())` satrida `main` funksiyasining asinxron ishlashini boshlaymiz.
