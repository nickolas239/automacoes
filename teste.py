import git

repo = git.Repo('./')

repo.index.add("*")

repo.index.commit("Teste de commit via automacao")

repo.remotes.origin.push()