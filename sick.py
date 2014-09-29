__author__ = 'cepuuher'


def cold_hard_decisions():
    print "That sucks"
    return None
   
     
def add_malady(condition):
    # write to file
    print "No info yet."
    return None


def main():
    print "Hey"
    is_cold = raw_input("Do you have a cold? [y/n] ")
    if is_cold.lower() == 'y':
        print "I'm sorry. Let's figure out how to feel better."
        cold_hard_decisions()
    else:
        condition = raw_input("What is the problem? ")
        add_malady(condition)
        print "Your illness has been added. Good luck sicko."


if __name__ == main():
    try:
        main()
    except:
        print "Exception occurred, bringing you into the debugger..."
        import pdb
        pdb.set_trace()
    finally:
        print "Bye!"