#! /usr/bin/env python

from ollama import chat


def main() -> None:
    model = "llama3.2"

    stream = chat(
        model=model,
        messages=[{"role": "user", "content": "Why is the sky blue?"}],
        stream=True,
    )
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

    response = chat(
        model=model,
        messages=[{"role": "user", "content": "Why is the sky orange?"}],
    )
    print(response["message"]["content"])


if __name__ == "__main__":
    main()
