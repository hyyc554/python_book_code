import logging
import time



SEVERITY = {
    logging.DEBUG:'debug',
    logging.INFO:'info',
    logging.WARNING:'warning',
    logging.ERROR:'error',
    logging.CRITICAL:'critical'
}
a =[(name,name)for name in SEVERITY.values()]
print(a)
SEVERITY.update(a)
print(SEVERITY)
def log_recent(conn,name,message,severity=logging.INFO,pipe=None):
    severity=str(SEVERITY.get(severity,severity)).lower()
    destination = "resent:%s:%s"%(name,severity)
    message = time.asctime()+ " "+ message
    pipe = pipe or conn.pipeline()
    pipe.lpush(destination,message)
    pipe.ltrim(destination,0,99)
    pipe.execute()






