from prefect import flow, task

@task
def create_messae(): 
    ms = "This is a test message"
    return(ms)

@flow
def hello_world():
    task_messae = create_messae()
    print(f"The message is: {task_messae}")

if  __name__ == '__main__':
    hello_world()
    
