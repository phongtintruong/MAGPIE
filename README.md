# Synthesis Data Pipeline

This project provides a pipeline for synthesizing Vietnamese conversation data with complex system prompts. Follow the steps below to generate the data:

## Pipeline Steps

1. **Transform English System Prompts to Vietnamese**
    - Run `transform_system_prompt_threading.py`.
    - This script takes the English system prompts from the `systemchat2.0` dataset and translates them into Vietnamese.
    - Output: A set of Vietnamese system prompts.

2. **Generate Conversation Data**
    - Run `gen_conversation`.
    - This script uses the Vietnamese system prompts generated in the previous step to synthesize conversation data.
    - Output: A dataset of conversations based on the Vietnamese system prompts.

## Usage

1. Ensure you have all dependencies installed as specified in the project requirements.
2. Execute the scripts in the following order:
    ```bash
    python transform_system_prompt_threading.py
    python gen_conversation
    ```
3. The final output will be a set of synthesized conversations in Vietnamese, ready for further use or analysis.

## Notes

- Make sure the input data (`systemchat2.0` dataset) is available in the expected location before starting the pipeline.
- Review the output after each step to ensure data integrity.