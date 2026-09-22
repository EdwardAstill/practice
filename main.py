from pathlib import Path

this_script_dir = Path(__file__).parent
problems_dir = this_script_dir / "problems"

def make_files():
    #make folders named 1-1000 in problems folder
    #put question.md, solution.py, solution.js,solution.cpp in folder
    for i in range(1, 1001):
        folder_path = problems_dir / str(i)
        folder_path.mkdir(parents=True, exist_ok=True)
        question_file = folder_path / "question.md"
        solution_py_file = folder_path / "solution.py"
        solution_js_file = folder_path / "solution.js"
        solution_cpp_file = folder_path / "solution.cpp"
        question_file.touch(exist_ok=True)
        solution_py_file.touch(exist_ok=True)
        solution_js_file.touch(exist_ok=True)
        solution_cpp_file.touch(exist_ok=True)

if __name__ == "__main__":
    make_files()

