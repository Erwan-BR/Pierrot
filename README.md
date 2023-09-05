# How to use Pierrot firmware

## Usage

Using this software is very simple:

1. Run the executable

2. Enter the following information:
   
   1. The complete project path (so that Pierrot knows where the project functions are)
   
   2. The path containing the functions whose return values we want to find.

3. Choose the path to the output file and the file name.

4. You're done!

## Objective

The aim is to retrieve the return values of certain functions in a certain project **automatically** in just a few seconds.

## Which projects?

The software works on projects such as OCEAN, which respect LGM naming rules:

- The name of each .c file is the name of the associated function.

- Only one function is present per file.

- Each function file begins with XXXX_ (XXXX being the quadrinomial of the class).

## Note

This software was created in less than three days, so there are obviously many points to improve to make the application more complete and robust. In particular, we need to look into why some return values are not analyzed.

During use, the output file will be created in the same place as the .exe file.

By way of example, for the OCEAN project, which contains 407 function files, there are only 52 functions that are "incorrectly analyzed", which is of course indicated by the software (incidentally, the errors come from the same functions in different calls).

## How do I recompile after a code update?

For the moment, there's no installer of its own. Simply enter the following command line to compile the code into an .exe file.

```python
pyinstaller --onefile --name Pierrot --noconsole main.py
```

In addition, the following libraries must be installed for those who will be developing the application:

```python
pip install pyinstaller
pip install openpyxl
pip install PyQt5
```

---

# Changes to improve the application:

- Add the ability to "merge" two excels (or even save to an old output) to see differences with an old result.

- In retrieve_return_values, we don't take into account values worth ".c", even though we'd have to find out where they come from.

- Add local variables at the start of the function with type annotations, to make the code clearer.

- Add try / except blocks to capture potential errors.

- Modify "Attention" values, making it clear where the "Attention" would come from.

- Add a log file system.

- Add a configuration XML file, in particular to see how to handle pointers (customize in the application what they are replaced with, and not in a .py file). This is useful if at some point you get "E_ReturnValue = pointer".

- Add the fact that if the file whose values you want to retrieve is not included in (or the same as) the project's scope file, then a window should pop up asking if it wants to continue (unusual behavior).

- Create a real installer.