
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


## Running the Tests

To run the API tests, follow the steps below:

1. Ensure the project API is running and accessible at the base URL specified in the `Running the Application.`

2. Open the imported collection in [Postman](https://www.postman.com/gold-robot-526148/workspace/python-term-project/collection/17813876-06ef068f-56ff-4713-8631-21856ce571d5?action=share&creator=17813876).

3. Select the desired test suite or individual test cases to execute.

4. Click the "Run" button to start the test execution.

5. Monitor the test execution and observe the test results in the Postman Runner.

<br>
![API Endpoint Hit](https://github.com/ujjawalpoudel/multilingual-video-summarizer/blob/youtube-audio-download-fix/API%20Hit%20Endpoint.png)

## Test Results

After executing the tests, you can view the test results and reports generated by Postman. These reports provide information about the test status, request-response details, and any failures encountered.


## Contributing

Contributors can participate in developing and improving the video summarization system by submitting pull requests, suggesting enhancements, or reporting issues. The repository encourages collaboration and welcomes contributions from individuals proficient in NLP, video analysis, and generative AI.


## Authors

- [@ujjawalpoudel](https://github.com/ujjawalpoudel)
- [@Sunilrai486](https://github.com/Sunilrai486)
- [@Shanover77](https://github.com/Shanover77)



## Support

For support, please contact one of the authors of this project or email me at ujjawalpoudel@gmail.com

