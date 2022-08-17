# Parallel Request Processing with FastAPI

In the standard way, you will be using python uvicorn package to start the FastAPI server. There two main limitations with this approach.
1. Resource under utilizing by starving muti-core CPUs while running everything in a single CPU core.
2. Waiting newly coming requests until currently processing request is completed. You can overcome this to some extent by async defs. But if your threads are CPU bounded (utilizing CPU 100% of the time), asynco cannot help you.

So, you what you need is the help of a third party software which manages mutiple OS threads or processes. This example uses gunicorn for that purpose. So it will associate user requests to OS threads. Then your python code will run as mutiple instances withing different OS threads or processes. Otherwise, python GIL will not let you to do this actual parallellism.

## Installing
> You need Linux or WSL enviroment with python >= 3.8 to run this experiment.
```bash
$ pip install -r requirements.txt
$ sudo apt install gunicorn3
```

## Runnning server

    $ gunicorn3 -k uvicorn.workers.UvicornWorker main:app

    [2022-08-17 13:14:32 +0530] [8698] [INFO] Starting gunicorn 19.7.1
    [2022-08-17 13:14:32 +0530] [8698] [INFO] Listening at: http://127.0.0.1:8000 (8698)
    [2022-08-17 13:14:32 +0530] [8698] [INFO] Using worker: uvicorn.workers.UvicornWorker
    /usr/lib/python3.8/os.py:1021: RuntimeWarning: line buffering (buffering=1) isn't supported in binary mode, the default buffer size will be used
      return io.open(fd, *args, **kwargs)
    [2022-08-17 13:14:32 +0530] [8700] [INFO] Booting worker with pid: 8700
    [2022-08-17 13:14:32 +0530] [8700] [INFO] Started server process [8700]
    [2022-08-17 13:14:32 +0530] [8700] [INFO] Waiting for application startup.
    [2022-08-17 13:14:32 +0530] [8700] [INFO] Application startup complete.
    
 ## Testing application
 This application mimics a rotation of a number wheel which has 0 to 9 numbers. You can stop it randomly to see what is the number currently there in the wheel.
 I'm using terminal with curl for this but you can use postman or your favourite tool for this purpose.
 1. Open one or more new terminals and execute below to start a CPU intensive job. If you request twice, two while loops will run in parellel
     ```
     $ curl http://127.0.0.1:8000/rotate
     ```
 2. In another terminal execute below. You can see the response to this request will come even CPU intensive jobs are running for other user requests. 
      ```
     $ curl http://127.0.0.1:8000/stop
     ```
 3. Above request will stop other jobs. So if you go back to the first terminals you opened you can see the results of the CPU internsive jobs. This concludes, you have  processed user requests parallely without one blocking another! Exploer the gunicorn server parameters and enjoy!
 
