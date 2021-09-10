import GPUtil


def GPUPick(num):

    # Get the power of two
    while (num & (num - 1)) != 0:
        num -= 1

    # Get GPU information
    gpus = GPUtil.getGPUs()
    gpusAvailable = GPUtil.getAvailability(gpus)

    # Initialize default variables
    status = False
    gpuList = []
    i = 0

    # Get available gpu list
    for gpuStatus in gpusAvailable:
        if gpuStatus == 1:
            status = True
            gpuList.append(gpus[i].id)
        i += 1

    # Output string
    if status == True:
        string = '-gpu ' + str(gpuList[0:num])[1:-1]
    else:
        string = 'Not Available'

    return status, string


print GPUPick(6)
