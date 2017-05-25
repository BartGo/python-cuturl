# changelog from git log 
# based on http://brettterpstra.com/2014/08/03/shell-tricks-changelogs-with-git/
# consider also links to commit:
#   git log --pretty=format:'<li> <a href="http://github.com/bartgo/cuturl/commit/%H">view commit &bull;</a> %s</li> ' -- reverse

git log --date=iso --pretty=format:"* %cd - %s%n%b" \
| grep -v ".* - \.\.\." | grep -v "^$" | grep -v ".* - Update .*" \
| grep -v ".* - Merge.*" | grep "[0-9][0-9][0-9][0-9]-.*"  > CHANGELOG.md
