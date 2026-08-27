#https://github.com/nidhaloff/deep-translator#id2
from deep_translator import MyMemoryTranslator

import asyncio


texts = [
    "1.4 레드라인",
    "1.4 LT",
    "1.4 프리미어",
    "1.4 퍼펙트 블랙",
    "1.4 프리미어",
    "1.4 프리미어",
    "1.4 LT",
    "1.4 퍼펙트 블랙",
    "1.4 프리미어",
    "1.4 프리미어",
    "1.6 디젤 LT",
    "1.4 LS",
    "1.4 프리미어",
    "1.4 프리미어",
    "1.4 LTZ",
    "1.6 디젤 LT",
    "1.6 디젤 LT",
    "1.4 LS",
    "1.6 디젤 퍼펙트 블랙",
]


async def translate_with_cache(texts, source="ko-KR", target="en-GB"):
    # Remove duplicates while preserving the first-seen order
    unique_texts = list(dict.fromkeys(texts))

    translator = MyMemoryTranslator(source=source, target=target)

    # MyMemoryTranslator is synchronous, so execute it in a thread
    translated_unique = await asyncio.to_thread(
        translator.translate_batch,
        unique_texts,
    )

    # Build a lookup cache
    cache = dict(zip(unique_texts, translated_unique))

    # Restore the original order, including duplicates
    return [cache[text] for text in texts]


async def main():
	translated = await translate_with_cache(texts)
	print(translated)
	return translated


asyncio.run(main())


