# -*- coding: utf-8 -*-
from chatterbot import ChatBot

bot = ChatBot(
    "SQLMemoryTerminal",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance"
        },
        {
            'import_path' : 'chatterbot.logic.LowConfidenceAdapter',
            'threshold' : 0.45,
            'default_response' : "죄송합니다. 정확한 답변을 찾을 수 없습니다. 좀 더 정확히 입력해 주시기 바랍니다. \n자세한 문의사항은 1588-2188이나 홈페이지를 통해 문의해 주시기 바랍니다."
        },
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    read_only= True
)

print("안녕하세요. 정부24 포털 QnA 서비스입니다.")
print("질문을 입력해 주세요.")

while True:
    try:
        print("Q : ",end="")
        bot_input = bot.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break