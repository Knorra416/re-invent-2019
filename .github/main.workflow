workflow "PR Workflow" {
  on = "push"
  resolves = ["Lint"]
}

action "Lint" {
  uses = "lgeiger/black-action@master"
  args = ". --check --fast"
}