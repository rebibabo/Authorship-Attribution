import warnings
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
load_dotenv()
from trainer import Trainer
from my_dataset import MyDataset

if __name__ == '__main__':
    model_name = 'microsoft/codebert-base'
    train_dataset = MyDataset('./dataset/train.jsonl')
    train_dataset.tokenize(model_name, 'code', do_lower_case=True)
    train_dataloader = train_dataset.to_dataloader(8, shuffle=True)

    eval_dataset = MyDataset('./dataset/valid.jsonl')
    eval_dataset.tokenize(model_name, 'code', do_lower_case=True)
    eval_dataloader = eval_dataset.to_dataloader(8, shuffle=False)

    test_dataset = MyDataset('./dataset/test.jsonl')
    test_dataset.tokenize(model_name, 'code', do_lower_case=True)
    test_dataloader = test_dataset.to_dataloader(8, shuffle=False)

    trainer = Trainer(
        model_name=model_name,
        num_labels=2,
        epochs=4,
        lr=2e-5,
        output_dir='saved_models',
        seed=42,
        metric='f1'
    )
    trainer.train(train_dataloader=train_dataloader, eval_dataloader=eval_dataloader)
    trainer.test(test_dataloader)