import subprocess


def get_commits(repo_path, branch_name):
    cmd = ['git', '-C', repo_path, 'log', '--name-only', '--pretty=format:%H|%ai|%an|%P', branch_name]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("Ошибка при получении коммитов из репозитория.")

    commits = []
    files=[]
    for line in result.stdout.splitlines():
        
        if '|' in line:
            parts = line.split('|')

        elif line:
            files.append(line)
            
        else:
            commit_data = {
                "hash": parts[0],
                "files": files,
                "dependencies": parts[3].split() if parts[3] else []
            }
            commits.append(commit_data)
            files=[]

    return commits