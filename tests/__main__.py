import services
import pydash as _
import test_main

def main():
    test_main.main()
    run_tests(services)

def run_tests(module):
    for key in _.keys(module):
        try:
            if key.index('test_') == 0:
                getattr(module, key).main()
        except ValueError as e:
            pass

if __name__ == '__main__':
    main()
