import logging
import os

# 日志级别等级 CRITICAL > ERROR > WARNING > INFO > DEBUG
class Logger:
    def __init__(self, log_file):
        # 创建一个logger， 创建一个日志的管理者
        logger = logging.getLogger()

        # 我发现这个循环并不能把所有的handle删除，始终还保留了一个，所以我又加了一个循环
        hs = logger.handlers
        if hs:
            for x in hs:
                logger.removeHandler(x)
        if hs:
            logger.removeHandler(logger.handlers[0])

        self.logger = logger
        logger.setLevel(logging.INFO)

         # 创建一个hander，将log写入文件--> 指定记录 log 的文件
        # log_path = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\ArtAppPortProject\log"
        # 存放日志的文件夹 优化为相对路径
        log_path = './log'
        # 组合路径
        self.log_file = os.path.join(log_path, log_file)
        fh = logging.FileHandler(self.log_file, mode="w")
        fh.setLevel(logging.INFO)

        # 再创建一个handler，将log输出到控制台
        print("控制台输出日志开始>>>>>")
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 设置输出格式
        log_format = "%(asctime)s %(filename)s [line:%(lineno)d %(levelname)s: %(message)s]"  # 指定log格式
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        #把handler添加到logger里
        logger.addHandler(fh)
        logger.addHandler(sh)

    def critical(self, msg):
        self.logger.critical(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

if __name__ == '__main__':
    log_file = "log.txt"
    logWrite = Logger(log_file)
    logWrite.critical("critical!!!")
    logWrite.error("error!!!")
    logWrite.warning("warning!!!")
    logWrite.info("info!!!")
    logWrite.debug("debug!!!")