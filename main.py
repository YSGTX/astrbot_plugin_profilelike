from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star
from .core.operator import Operator

class Profile_Like(Star):

    def __init__(self, context: Context, operator: Operator):
        super().__init__(context)
        self.operator = operator
        

    @filter.llm_tool() 
    async def submit_like(self, event: AstrMessageEvent, user_id: str, times: int) -> MessageEventResult:
        '''给用户的主页点赞

        Args:
           user_id(str): 用户的 QQ 号
           times(int): 点赞次数
        '''
        result = await self.operator.submit_likes(user_id, times)
        yield event.plain_result(result)
