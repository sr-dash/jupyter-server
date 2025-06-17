# Jupyter-server 
Here’s a Python script that will:

1. Start a JupyterLab instance in the background on your cluster.

2. Log the token, start time, job id (i.e., the PID of the Jupyter process), and port to a file.

3. Allow you to later copy the log to your local machine and kill the JupyterLab process using the PID (job id).

Assumptions:
You're running this script on a Linux cluster machine.

* Python and JupyterLab are installed.

* No job scheduler is used.

* You're using SSH port forwarding to connect from your local machine (I'll note how below).

In the cluster, run the python script using nohup and &.

`nohup python3 start_jupyter_lab.py > ~/jupyter_wrapper.log 2>&1 &`

Run the python file after copying it to the cluster account location. Change the location of the log file accordingly. 

In the local system:

`ssh -N -L 8888:localhost:<assigned_port> your_user@cluster_hostname`

Find the port details from the json file and replace it at `<assigned_port>`.

Now in your prefered browser, start using the jupyter server by typing the address,

`http://localhost:8888/?token=abc123...`

Hope this helps.

Author: Soumyaranjan Dash


