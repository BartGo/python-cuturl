# changelog from git log 
# based on http://brettterpstra.com/2014/08/03/shell-tricks-changelogs-with-git/

git log --date=iso --pretty=format:"* %cd - %s%n%b" \
| grep -v ".* - \.\.\." | grep -v "^$" | grep -v ".* - Update .*" \
| grep -v ".* - Merge.*" | grep "[0-9][0-9][0-9][0-9]-.*"  > CHANGELOG.md
