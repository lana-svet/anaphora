import sys
sys.path.append('/corpus/python')
from Annotation import AnnotationEditor
editor = AnnotationEditor('config.ini')

# определение вершин простых групп из 1 токена
editor.db_cursor.execute('SELECT syntax_groups_simple.group_id, token_id, COUNT(token_id) AS tki FROM syntax_groups_simple INNER JOIN syntax_groups ON syntax_groups_simple.group_id = syntax_groups.group_id WHERE head_id = 0 GROUP BY group_id HAVING tki = 1')
result_simple = editor.db_cursor.fetchall()

for row in result_simple:
    editor.db_cursor.execute('UPDATE syntax_groups SET head_id = ' + str(row['token_id']) + ' WHERE group_id = ' + str(row['group_id']))


# определение вершин сложных групп из 1 ИГ  
editor.db_cursor.execute('SELECT parent_gid, child_gid, COUNT(child_gid) AS chg FROM syntax_groups_complex INNER JOIN syntax_groups ON syntax_groups_complex.parent_gid = syntax_groups.group_id WHERE head_id = 0 GROUP BY group_id HAVING chg = 1')
result_complex = editor.db_cursor.fetchall()

for row in result_complex:
    editor.db_cursor.execute('UPDATE syntax_groups SET head_id = ' + str(row['child_gid']) + ' WHERE group_id = ' + str(row['parent_gid']))

    
# вывод вершин в файл    
editor.db_cursor.execute('SELECT group_id, head_id FROM syntax_groups')
result = editor.db_cursor.fetchall()

fd = open('syntax_groups.txt', 'w')
for row in result:
    fd.write(', '.join("%s = %s" % (k,v) for (k,v) in row.iteritems()) + "\n")
fd.close()