from polymorf import DatasetProcessor

if __name__ == "__main__":
    input_file = 'var9.csv'
    processor = DatasetProcessor(input_file)
    removed = ~processor
    processor.split_and_save('Cash-back', 'cashback_true.csv', 'cashback_false.csv')