#include <OpenCL/opencl.h>
#include <stdio.h>

// Define the OpenCL kernel code as a string
const char *kernelSource = 
"__kernel void helloWorld(__global char *output) {\n"
"    const char message[] = \"Hello, World!\";\n"
"    for (int i = 0; i < sizeof(message); ++i) {\n"
"        output[i] = message[i];\n"
"    }\n"
"}\n";

int main() {
    // Set the size of the output buffer
    const int bufferSize = 15; // Length of "Hello, World!" plus null terminator

    // Output buffer
    char output[bufferSize];

    // Load OpenCL platform
    cl_platform_id platform;
    clGetPlatformIDs(1, &platform, NULL);

    // Load OpenCL device
    cl_device_id device;
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, NULL);

    // Create OpenCL context
    cl_context context = clCreateContext(NULL, 1, &device, NULL, NULL, NULL);

    // Create OpenCL command queue
    cl_command_queue queue = clCreateCommandQueue(context, device, 0, NULL);

    // Create and build OpenCL program
    cl_program program = clCreateProgramWithSource(context, 1, &kernelSource, NULL, NULL);
    clBuildProgram(program, 1, &device, NULL, NULL, NULL);

    // Create OpenCL kernel
    cl_kernel kernel = clCreateKernel(program, "helloWorld", NULL);

    // Create OpenCL buffer
    cl_mem bufferOutput = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(char) * bufferSize, NULL, NULL);

    // Set kernel argument
    clSetKernelArg(kernel, 0, sizeof(cl_mem), &bufferOutput);

    // Execute OpenCL kernel
    size_t globalSize = bufferSize;
    clEnqueueNDRangeKernel(queue, kernel, 1, NULL, &globalSize, NULL, 0, NULL, NULL);
    clFinish(queue);

    // Read the result from the OpenCL buffer
    clEnqueueReadBuffer(queue, bufferOutput, CL_TRUE, 0, sizeof(char) * bufferSize, output, 0, NULL, NULL);

    // Display the result
    printf("Message: %s\n", output);

    // Clean up
    clReleaseMemObject(bufferOutput);
    clReleaseKernel(kernel);
    clReleaseProgram(program);
    clReleaseCommandQueue(queue);
    clReleaseContext(context);

    return 0;
}