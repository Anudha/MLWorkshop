#! /usr/bin/env python
from transformers import EncoderDecoderCache, T5ForConditionalGeneration, T5Tokenizer


def main() -> None:
    tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small", legacy=False)
    model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

    input_ids = tokenizer(
        "The <extra_id_0> walks in <extra_id_1> park", return_tensors="pt"
    ).input_ids
    labels = tokenizer(
        "<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt"
    ).input_ids

    # the forward function automatically creates the correct decoder_input_ids
    loss = model(
        input_ids=input_ids,
        labels=labels,
        past_key_values=EncoderDecoderCache.from_legacy_cache(None),
    ).loss
    print(loss)


if __name__ == "__main__":
    main()
