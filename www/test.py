import orm , asyncio

from models import User

async def test(loop):
    await orm.create_pool(loop=loop,user='root', password='123456ss', db='ASPW')
    u = User(name='王弘剑', email='whj.527@gmail.com', passwd='1234567890', image='about:blank')
    await u.save()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()