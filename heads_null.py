import sys
sys.path.append('/corpus/python')
from Annotation import AnnotationEditor
editor = AnnotationEditor('config.ini')
editor.db_cursor.execute('SELECT group_id FROM syntax_groups WHERE head_id = 0')
result = editor.db_cursor.fetchall()

fd = open('result_heads_null.txt', 'w')
for row in result:
    fd.write(str(row['group_id']) + "\n")
fd.close()
print(result)
