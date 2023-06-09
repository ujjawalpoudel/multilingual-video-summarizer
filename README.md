
# Video Summarizer

This GitHub repository contains the code and documentation for a comprehensive video summarization system. The project aims to support `English`, `Nepali`, and `Hindi` languages, allowing users to quickly extract relevant information from multi-lingual videos. The system utilizes `Natural Language Processing (NLP)`, video analysis techniques, and generative AI to generate concise summaries and visual representations of video content.


## Installation
1. Clone the repository to your local machine.
  ```bash
  git clone git@github.com:ujjawalpoudel/multilingual-video-summarizer.git
  ```

2. Navigate to the project directory.
  ```bash
  cd multilingual-video-summarizer
  ```

3. Create a virtual environment.
  Use the version number of python installed on your computer.
  check it using python --version
  ```bash
  python3.11 -m venv ytube_summary_venv 
  ```

4. Activate the virtual environment.

    a. For mac:
    ```bash
    source ytube_summary_venv/bin/activate
    ```
    b. For windows:
    ```bash
    ytube_summary_venv\Scripts\activate.bat
    ```

5. Install the required Python packages.
  ```bash
  pip install -r requirements.txt
  ```

## Running the Application
1. Activate the virtual environment.

    a. For mac:
    ```bash
    source ytube_summary_venv/bin/activate
    ```
    b. For windows:
    ```bash
    ytube_summary_venv\Scripts\activate.bat
    ```
    
  2. Start the Flask development server.
  ```bash
  python main.py
  ```

  3. Access the application in a web browser by navigating to `http://localhost:5000`.


    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_USER`

`DB_PASSWORD`

`DATABASE_NAME`

`DB_HOST`


## Contributing

Contributors can participate in developing and improving the video summarization system by submitting pull requests, suggesting enhancements, or reporting issues. The repository encourages collaboration and welcomes contributions from individuals proficient in NLP, video analysis, and generative AI.


## Authors

- [@ujjawalpoudel](https://github.com/ujjawalpoudel)
- [@Sunilrai486](https://github.com/Sunilrai486)
- [@Shanover77](https://github.com/Shanover77)



## Support

For support, please contact one of the authors of this project or email me at ujjawalpoudel@gmail.com

