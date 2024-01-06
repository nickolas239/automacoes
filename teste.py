import pygit2

repo = pygit2.Repository('./')

index = repo.index
index.add_all()
index.write()

tree_id = index.write_tree()

author = pygit2.Signature('Nickolas', 'teste@github.com')
commiter = author

branch_atual = repo.head.shorthand

print(branch_atual)

commit_id = repo.create_commit(
    f"refs/heads/{branch_atual}",
    author,
    commiter,
    'Teste de commit via automacao',
    tree_id,
    [repo.head.target],
)

credenciais = ('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', "")

remote = repo.remotes["origin"]
remote.credentials = credenciais
remote.push([f"refs/heads/{branch_atual}"])