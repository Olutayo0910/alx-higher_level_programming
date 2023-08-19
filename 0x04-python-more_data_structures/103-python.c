#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		fprintf(stderr, "Invalid Python list object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		fprintf(stderr, "Invalid Python bytes object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t max_print = (size > 10) ? 10 : size;
	unsigned char *data = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", data);
	printf("  first %zd bytes:", max_print);

	for (Py_ssize_t i = 0; i < max_print; i++) {
		printf(" %02x", data[i]);
	}
	printf("\n");
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void) {
	Py_Initialize();
	PyObject *list = Py_BuildValue("[i, s, d]", 1, "hello", 3.14);
	PyObject *bytes = PyBytes_FromStringAndSize("Hello", 5);

	print_python_list(list);
	print_python_bytes(bytes);

	Py_XDECREF(list);
	Py_XDECREF(bytes);
	Py_Finalize();

	return (0);
}
