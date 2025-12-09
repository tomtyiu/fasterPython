import timeit
from openai import OpenAI

my_code = """
from openai import OpenAI

# Create the client once; reuse it if this runs repeatedly
client = OpenAI()

# Keep local variable bindings tight for faster lookups
create = client.responses.create

def main():
    resp = create(
        model="gpt-5-nano",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(resp.output_text)

if __name__ == "__main__":
    main()
"""

time_taken = timeit.timeit(my_code, number=2)

print("Total time taken:", time_taken)


#Total time taken: 31.44917179999993
