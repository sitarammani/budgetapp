# Screenshots Directory

This directory contains visual documentation for the BudgetApp user interface and setup process.

## Required Screenshots

### 1. first_time_setup.png
- **When to capture**: During first application launch
- **What to show**: The progress bar and initial setup prompts
- **Instructions**:
  1. Delete any existing config files if testing fresh install
  2. Run the application
  3. Capture the screen when you see "Detecting Ollama installation..." progress bar
  4. Include the full terminal/command prompt window

### 2. main_menu.png
- **When to capture**: After setup completes
- **What to show**: The main menu with numbered options
- **Instructions**:
  1. Complete the setup process
  2. Capture the main menu screen showing all 7 options
  3. Ensure the menu title and all options are visible

### 3. ai_model_setup.png
- **When to capture**: When AI model is not installed
- **What to show**: The prompt asking if user wants to install AI models
- **Instructions**:
  1. Remove Ollama models or simulate missing model scenario
  2. Run the app and trigger the AI setup prompt
  3. Capture the "AI model not found" message and installation prompt

### 4. report_generation.png
- **When to capture**: During report generation process
- **What to show**: The report generation workflow
- **Instructions**:
  1. Prepare a sample CSV file with transaction data
  2. Run option 1 from main menu
  3. Capture the file selection and processing screens

### 5. ai_query.png
- **When to capture**: Using the AI assistant feature
- **What to show**: The natural language query interface
- **Instructions**:
  1. Ensure AI model is installed and working
  2. Select option 2 from main menu
  3. Capture the query input prompt and sample response

### 6. gmail_oauth.png
- **When to capture**: During Gmail OAuth setup
- **What to show**: The OAuth authentication flow
- **Instructions**:
  1. Delete existing token.json if present
  2. Trigger email functionality
  3. Capture the browser OAuth consent screen (if possible) or the app's OAuth prompts

### 7. architecture_diagram.png
- **When to capture**: From the README.md documentation
- **What to show**: The rendered Mermaid architecture diagram
- **Instructions**:
  1. Open README.md in a Markdown viewer that supports Mermaid (GitHub, VS Code with extension, etc.)
  2. Navigate to the Architecture Overview section
  3. Capture the rendered diagram showing all components and connections
  4. Ensure the entire diagram is visible and readable

## Screenshot Guidelines

- **Format**: PNG preferred, high resolution
- **Naming**: Use lowercase with underscores, match the filenames above
- **Size**: Aim for 1200px width minimum for readability
- **Content**: Include full application window/interface
- **Platform**: Capture on the target platform (Windows/macOS/Linux)
- **Tools**: Use built-in screenshot tools (Cmd+Shift+4 on macOS, Snipping Tool on Windows)

## Adding Screenshots

1. Capture screenshots following the guidelines above
2. Save them in this directory with the exact filenames specified
3. Update the README.md references if filenames change
4. Test that images display correctly in the documentation