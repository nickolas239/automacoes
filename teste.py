import git

repo = git.Repo('./')

repo.index.add("*")

nome_branch_local = repo.active_branch.name

try:
    repo.remotes.origin.refs[nome_branch_local]
except IndexError:
    branch_remota = "dev"

    repo.git.branch(f"--set-upstream-to={branch_remota}", nome_branch_local)

repo.index.commit("Teste de commit via automacao")

repo.remotes.origin.push()