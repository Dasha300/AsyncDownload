from git import Repo

import asyncio


async def download_folder(name):
    try:
        git_url = "https://gitea.radium.group/radium/project-configuration"
        Repo.clone_from(git_url, "./tmp/" + str(name))
        await asyncio.sleep(3)
    except Exception as ex:
        print(f"Exception `cause {ex} ")
    print(f'task {name} завершен')


async def main_task():
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(download_folder(i)))
        await asyncio.gather(*tasks)


def start_async():
    asyncio.run(main_task())
