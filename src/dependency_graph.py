import os
import subprocess

from src.git_helper import get_commits


def generate_dot_content(commits):
    dot_content = ["digraph G {"]
    for commit in commits:
        #commit node
        node_line = f'    "{commit["hash"]}" [label="commit {commit["hash"]}"];'
        dot_content.append(node_line)
        
        #file node
        c = 0
        for file in commit["files"]:
            c+=1
            node_line1 = f'    "file{c}{commit["hash"]}" [label="{file}"] [color="red"];'

            dont_add = False
            for node in dot_content:
                if '"' + file + '"' in node:
                    dont_add = True
                    
            if not dont_add:
                dot_content.append(node_line1)
        

        for dep in commit["dependencies"]:
            
            #connecting commits
            edge_line = f'    "{dep}" -> "{commit["hash"]}"[label="commit"];'
            dot_content.append(edge_line)
            
            #connecting created files
            if not dont_add:
                c = 0
                for file in commit["files"]:
                    c+=1
                    edge_line1 = f'    "{commit["hash"]}" -> "file{c}{commit["hash"]}"[label="create"];'
                    dot_content.append(edge_line1)
                    
            #connecting modified files
            else:
                for node in dot_content:
                    if '"' + file + '"' in node:
                        edge_line1 = f'    "{commit["hash"]}" -> {node.split()[0]}[label="update"];'
                        dot_content.append(edge_line1)
                

    dot_content.append("}")
    return "\n".join(dot_content)


class DependencyGraph:
    def __init__(self, graphviz_path, repo_path, output_path, branch_name):
        self.graphviz_path = graphviz_path
        self.repo_path = repo_path
        self.output_path = output_path
        self.branch_name = branch_name
        self.commits = []

    def build_graph(self):
        self.commits = get_commits(self.repo_path, self.branch_name)

        dot_content = generate_dot_content(self.commits)

        with open("graph.dot", "w") as f:
            f.write(dot_content)

        cmd = [self.graphviz_path, "-Tpng", "graph.dot", "-o", self.output_path]
        subprocess.run(cmd)

    def run(self):
        self.build_graph()
        print(f"Граф зависимостей успешно построен и сохранен в {self.output_path}.")
