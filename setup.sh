echo 'export HF_HOME="/root/autodl-tmp/huggingface"' >> ~/.bashrc
source ~/.bashrc
pip install --upgrade pip
pip install -r requirements.txt
pip install "unsloth[cu121-torch230] @ git+https://github.com/unslothai/unsloth.git"
wget https://download1323.mediafire.com/9p7au1kucr6gLIVo2S6unekwLMfnBZXOHtPaWQ_xZ_v5uaMTVitV3cfbpoKA7VUaeVOZygsRWpdTnileTeNoDQf9HtEA9l3za7fUnN3sYji2foE4fFe-NB6T3YiRH6Dgy7BNxdZtSF3_8kpNBGiLiFp9Er-_QA0QDScM9olAYFw/no0bi7l46u3k5k2/unified_chip2.jsonl.gz