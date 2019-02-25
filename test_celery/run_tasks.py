from .tasks import longtime_add, longtime_minus
import time

if __name__ == '__main__':

    # result = longtime_add.delay(1,4)
    # # at this time, our task is not finished, so it will return False
    # print ('Task finished? ', result.ready())
    # print ('Task result: ', result.result)
    # # sleep 10 seconds to ensure the task has been finished
    # time.sleep(10)
    # # now the task should be finished and ready method will return True
    # print ('Task finished? ', result.ready())
    # print ('Task result: ', result.result)
    
    #longtime_add.delay(9,8)
    longtime_add.apply_async((0,1),queue='queueA')
    longtime_minus.apply_async((0,1),queue='queueB')

