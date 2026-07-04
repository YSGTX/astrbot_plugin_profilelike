from aiocqhttp import exceptions
from aiocqhttp import CQHttp
from astrbot.api import logger

class Operator:

    def __init__(self, client: CQHttp, exc: exceptions):
        self.client = client
        self.exc = exc
    
    async def submit_likes(self, user_id: str, times: int) -> str:
        try:
            await self.client.send_like(user_id(int), times)
            logger.info(f"给用户 {user_id} 点赞了 {times} 次。")
            return f"已为 {user_id} 点赞 {times} 次。"
        except self.exc.ActionFailed as e:
            logger.error(f"给用户 {user_id} 点赞时出现错误: {e}")
            return f"点赞失败: {str(e)}"